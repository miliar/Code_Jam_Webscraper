// CodeJam
// Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/20

#include <iostream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

static unsigned dbg_flags;

class Problem
{
 public:
    Problem(int vr, int vc, int vw) : r(vr), c(vc), w(vw), result(-1) {}
    ~Problem() {}
    void solve();
    void print_solution(ostream&);
 private:
    int r, c, w;
    int result;
};

void Problem::solve()
{
    int result1 = 0;
    if (c == w)
    {
        result1 = w;
    }
    else if (w == 1)
    {
        result1 = c;
    }
    else
    {
        int d = c / w;
        if ((c % w) == 0)
        {
            if (d > 2)
            {
                result1 = d - 2 + w + 1;
            }
            else
            {
                result1 = w + 1;
            }
        }
        else
        {
            if (d > 1)
            {
                result1 = d - 1 + w + 1;
            }
            else
            {
                result1 = w + 1;
            }
        }
    }
    result = r * result1;   
}

void Problem::print_solution(ostream &fo)
{
    fo << " " << result << "\n";
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

    unsigned testnum = 0;
    ofstream *ftee = 0;
    
    if (argc > 3) { dbg_flags = strtoul(argv[3], 0, 0); }
    if (argc > 5)
    {
        testnum = strtoul(argv[4], 0, 0);
        ftee = new ofstream(argv[5]);
        *ftee << "1\n";
    }

    unsigned n_cases;
    *pfi >> n_cases;

    if (dbg_flags & 0x1) { cerr << "n_cases=" << n_cases << "\n"; }

    ostream &fout = *pfo;
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        int r, c, w;
        *pfi >> r >> c >> w;
        if (ci + 1 == testnum) { *ftee << r << ' ' << c << ' ' << w << '\n'; }
        Problem problem(r, c, w);
        // cerr << "Case ci="<<ci << " (ci+1)="<<ci+1 << "\n";
        problem.solve();
        fout << "Case #"<< ci+1 << ":";
        problem.print_solution(fout);
        fout.flush();
    }
    
    if (pfi != &cin) { delete pfi; }
    if (pfo != &cout) { delete pfo; }
    if (ftee) { delete ftee; }
    return 0;
}

