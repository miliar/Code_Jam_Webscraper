// CodeJam
// Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/20

#include <iostream>
#include <fstream>
#include <string>
// #include <set>
// #include <map>
#include <vector>
#include <utility>
#include <algorithm>

#include <cstdlib>
// #include <gmpxx.h>

using namespace std;

// typedef mpz_class mpzc_t;
typedef unsigned long ul_t;
// typedef vector<ul_t> vul_t;

static unsigned dbg_flags;

typedef pair<unsigned, unsigned> uu_t;
typedef vector<uu_t> vuu_t;
typedef vector<string> vstr_t;

class Senate
{
 public:
    Senate(istream& fi);
    void solve();
    void print_solution(ostream&) const;
 private:
    void check_no_major() const;
    vuu_t parties;
    vstr_t solution;
};

Senate::Senate(istream& fi)
{
    unsigned N;
    fi >> N;
    for (unsigned i = 0; i < N; ++i)
    {
        unsigned n;
        fi >> n;
        parties.push_back(uu_t(n, i));
    }
}

void Senate::solve()
{
    static const char *AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    sort(parties.begin(), parties.end());
    char b3[3];
    b3[2] = '\0';

    unsigned n_senators = 0;
    for (auto i = parties.begin(); i != parties.end(); ++i)
    {
        n_senators += (*i).first;
    }
    bool even = (n_senators % 2 == 0);
    while (!parties.empty())
    {
        b3[1] = '\0';
        unsigned nk = 2;
        if (!even)
        {
            nk = 1;
            even = true;
        }
        for (unsigned k = 0; k < nk; ++k)
        {
            unsigned sz = parties.size();
            if (sz > 0)
            {
                uu_t &party_max = parties[sz - 1];
                b3[k] = AZ[party_max.second];
                --party_max.first;
                if (party_max.first == 0)
                {
                    parties.pop_back();
                }
                else
                {
                    for (unsigned d = sz - 1; 
                        d > 0 && parties[d].first < parties[d - 1].first;
                        --d)
                    {
                        swap(parties[d - 1], parties[d]);
                    }
                }
            }
        }
        check_no_major();
        string s2(b3); 
        solution.push_back(s2);
    }
}

void Senate::check_no_major() const
{
    unsigned total = 0;
    unsigned np = parties.size();
    for (unsigned i = 0; i < np; ++i)
    {
        total += parties[i].first;
    }
    unsigned half = total/2;
    for (unsigned i = 0; i < np; ++i)
    {
        unsigned psz = parties[i].first;
        if (psz > half)
        {
            cerr << "We have an error in " << __LINE__ << "\n";
            exit(1);
        }
    }
    
}

void Senate::print_solution(ostream &fo) const
{
    for (unsigned i = 0, n = solution.size(); i < n; ++i)
    {
        fo << " " << solution[i];
    }
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

    if ((!pfi) || (!pfo) || pfi->fail() || pfo->fail())
    {
        cerr << "Open file error\n";
        exit(1);
    }

    if (argc > 3) { dbg_flags = strtoul(argv[3], 0, 0); }
    // bool large = (argc > 4) && !strcmp(argv[4], "-large");

    unsigned n_cases;
    *pfi >> n_cases;

    ostream &fout = *pfo;
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        Senate problem(*pfi);
        // cerr << "Case ci="<<ci << " (ci+1)="<<ci+1 << "\n";
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
