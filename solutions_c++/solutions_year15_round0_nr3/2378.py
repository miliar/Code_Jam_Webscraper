// CodeJam
// Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/20

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <utility>

#include <cstdlib>

using namespace std;

static unsigned dbg_flags = 0; // 0xff;

typedef enum {U, I, J, K, mU, mI, mJ, mK} Q_t;
const char *qname[8] = {"1","i", "j", "k", "-1","-i", "-j", "-k"};

static Q_t  mult[8][8];
static const Q_t  Q_IJK = mU; // -1

static Q_t qinv(Q_t q)
{
    Q_t mq = Q_t((q + 4) % 8);
    return mq;
}

enum { MAX_L = 10000 };

static void mult_init()
{
    for (int i = 0; i < 8; ++i)
    {
        mult[U][i] = mult[i][U] = Q_t(i);
    }

    mult[int(I)][int(I)] = mU;
    mult[int(I)][int(J)] = K;
    mult[int(I)][int(K)] = mJ;

    mult[int(J)][int(I)] = mK;
    mult[int(J)][int(J)] = mU;
    mult[int(J)][int(K)] = I;

    mult[int(K)][int(I)] = J;
    mult[int(K)][int(J)] = mI;
    mult[int(K)][int(K)] = mU;

    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            Q_t q = mult[i][j];
            // int mq = (q + 4) % 8;
            Q_t mq = qinv(q);

            mult[i + 4][j + 4] = Q_t(q);
            mult[i][j + 4] = Q_t(mq);
            mult[i + 4][j] = Q_t(mq);
        }
    }


    if (dbg_flags & 0x1)
    {
        cout << "    ";
        for (int j = 0; j < 8; ++j)
        {
            cout << " " << setw(2) << qname[j];
        }
        cout << "\n   -----------------------------\n";

        for (int i = 0; i < 8; ++i)
        {
            cout << setw(2) << qname[i] << "| ";
            for (int j = 0; j < 8; ++j)
            {
                cout << " " << setw(2) << qname[mult[i][j]];
            }
            cout << "\n";
        }
    }
}


class IJK
{
 public:
    IJK(istream& fi);
    ~IJK()
    {
        delete [] argue;
        delete [] mult_head;
    }
    void solve();
    void print_solution(ostream&);
 private:
    unsigned L;
    unsigned X;
    // Q_t argue[MAX_L];
    // Q_t mult_head[MAX_L];
    Q_t *argue;
    Q_t *mult_head;
    int qFirstIndex[8];
    int qLastIndex[8];
    const char *result;
};

IJK::IJK(istream& fi) :
    result("NO")
{
    fi >> L >> X;
    if (dbg_flags & 0x2) { cout << "L="<<L << ", X="<<X << "\n"; }
    argue = new Q_t[L];
    mult_head = new Q_t[L];
    for (unsigned ci = 0; ci < L; ++ci)
    {
        char c;
        fi >> c;
        if (dbg_flags & 02) { cout << "ci=" << ci << ", c='" << c << "'\n"; }
        Q_t q = mU;
        switch (c)
        {
         case 'i': q = I; break;
         case 'j': q = J; break;
         case 'k': q = K; break;
         default:
             cerr << "Bad ijk char: '" << c << "'\n";
        }
        argue[ci] = q;
    }
}

// Ideas:
// For each q, we have q^4 = q*q*q*q = 1.
// for the tail to be K, its complementary head must be mK.
void IJK::solve()
{
    Q_t q = U;

    for (unsigned i = 0; i < L; ++i)
    {
        q = mult[q][argue[i]];
        mult_head[i] = q;
    }

    const Q_t multL = q;
    // const Q_t inv_multL = qinv(multL);
    const unsigned xmod4 = X % 4;    


    Q_t mult_all = U; // compute:  mult_head[Last] ^ X
    for (unsigned x = 0; x < xmod4; ++x)
    {
        mult_all = mult[mult_all][multL];
    }
    if (dbg_flags & 0x4) { cout << "mult_all: " << qname[mult_all] << "\n"; }

    if ((L*X >= 3) && mult_all == Q_IJK)
    {
        for (int i = 0; i < 8; ++i)
        {
            qFirstIndex[i] = -1;
            qLastIndex[i] = -1;
        }
        for (unsigned i = 0; i < L; ++i)
        {
            Q_t qh = mult_head[i];
            if (qFirstIndex[qh] == -1) { qFirstIndex[qh] = i; }
            qLastIndex[qh] = i;
        }

        int xI = 0, xK = 0;
        int iI = -1, iK = -1;
        // bool foundI = false, foundK = false;
        Q_t pre_mult = U;
        int xLimit = (X < 4 ? X : 4);
        while ((xI <xLimit) && iI == -1) // Search for first I
        {
            Q_t  pI = mult[pre_mult][I];
            if (qFirstIndex[pI] >= 0)
            {
                iI = qFirstIndex[pI];
            } 
            else
            {
                ++xI;
                pre_mult = mult[pre_mult][multL];
            }
        }
        if (dbg_flags & 0x8)
        {
            cout << "xI="<<xI << ", iI="<<iI << "\n";
        }

        pre_mult = U;
        while ((xK <xLimit) && iK == -1) // Search for last K (via mK)
        {
            Q_t  pK = mult[pre_mult][K]; // (K)K = -1 = (IJ)K
            if (qLastIndex[pK] >= 0)
            {
                iK = qLastIndex[pK];
            } 
            else
            {
                ++xK;
                pre_mult = mult[pre_mult][multL];
            }
        }
        xK = (X-1) - xK;
        if (dbg_flags & 0x8)
        {
            cout << "xK="<<xK << ", iK="<<iK << "\n";
        }
        
        if ((iI >= 0) && (iK >=0) &&
            ((xI < xK) || ((xI == xK) && (iI < iK))))
        {
            result = "YES";
        }
    }
}

void IJK::print_solution(ostream &os)
{
    os << ' ' << result;
}


static Q_t mult_abe(const Q_t *a, unsigned b, unsigned e)
{
    Q_t m = U;
    for (unsigned i = b; i < e; ++i)
    {
        m = mult[m][a[i]];
    }
    return m;
}

static int gen_tests()
{
    enum {L=6, Xmin = 1, Xmax=11, N_YES=4, N_NO = 4};
    Q_t q_argue[L*Xmax];
    char argue[L + 1];
    unsigned n_no = 0, n_yes = 0;
    unsigned qtry = 0, icase = 0;

    cout << (N_YES + N_NO) << "\n";
    while (n_yes < 4 && qtry < 0x10000)
    {
        unsigned X = (rand() % Xmax) + 1;
        argue[L] = '\0';
        for (int i = 0; i < L; ++i)
        {
            static Q_t  qrand[3] = {I, J, K};
            unsigned q = rand() % 3;
            argue[i] = "ijk"[q];
            for (unsigned x = 0; x < X; ++x)
            {
                q_argue[x*L + i] = qrand[q];
            }
        }
        // cerr << "Qtry: " << qtry << "\n";
        bool isYES = false;
        for (unsigned int i = 1; (i < X*L-1) && !isYES; ++i)
        {
            Q_t maybeI = mult_abe(q_argue, 0, i);
            if (maybeI == I)
            {
                for (unsigned j = i + 1; (j < X*L) && !isYES; ++j)
                {
                    Q_t maybeJ = mult_abe(q_argue, i, j);
                    Q_t maybeK = mult_abe(q_argue, j, X*L);
                    isYES = (maybeJ == J) && (maybeK == K);
                }
            }
        }
        bool outit = false;
        if (isYES)
        {
            outit = (++n_yes <= N_YES);
        }
        else
        {
            outit = (++n_no <= N_NO);
        }
        if (outit)
        {
            ++icase;
            cout << L << " " << X << "\n" <<
                 argue << "\n";
            cout << "Case #"<< icase << ": " << (isYES ? "YES" : "NO") << "\n";
        }
        ++qtry;
    }
    int rc = 0;
    if (icase < N_YES + N_NO)
    {
        cerr << "generated only " << icase << " < " << 
             (N_YES + N_NO) << " cases\n";
        rc = 1;
    }
    return rc;
}

int main(int argc, char ** argv)
{
    const string dash("-");

    istream *pfi = (argc < 2 || (string(argv[1]) == dash))
         ? &cin
         : new ifstream(argv[1]);
    ostream *pfo = (argc < 3 || (string(argv[2]) == dash))
         ? &cout
         : new ofstream(argv[2]);

    mult_init();
    if (argc > 3) { dbg_flags = strtoul(argv[3], 0, 0); }

    if (dbg_flags & 0x100)
    {
        int rc = gen_tests();
        return rc;
    }

    unsigned n_cases;
    *pfi >> n_cases;

    ostream &fout = *pfo;
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        IJK problem(*pfi);
        if (dbg_flags) { cerr << "Case ci="<<ci << " (ci+1)="<<ci+1 << "\n"; }
        problem.solve();
        fout << "Case #"<< ci+1 << ":";
        problem.print_solution(fout);
        fout << "\n";
        fout.flush();
        
    }
    
    if (pfi != &cin) { delete pfi; }
    if (pfo != &cout) { delete pfo; }
    return 0;
}
