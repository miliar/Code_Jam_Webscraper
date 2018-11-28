// CodeJam
// Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/20

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>

#include <cstdlib>

using namespace std;

static unsigned dbg_flags;

typedef vector<unsigned> vu_t;
typedef vector<vu_t> vvu_t;

unsigned isqrt(unsigned n)
{
    unsigned low = 1, high = n + 1;
    while (low < high - 1)
    {
        unsigned mid = (low + high)/2;
        if (mid * mid <= n)
        {
            low = mid;
        }
        else
        {
            high = mid;
        }
    }
    return low;
}

class Pan
{
 public:
    Pan(istream& fi);
    void solve();
    void print_solution(ostream&);
 private:
    // unsigned sub_solve(vu_t, vvu_t &steps, int depth) const;
    unsigned sub_solve(vu_t) const;
    unsigned heap_solve();
    unsigned sub_heap_solve();
    vu_t diners;
    unsigned result;
};

Pan::Pan(istream& fi)
{
    unsigned n;
    fi >> n;
    result = n;
    for (unsigned i = 0; i < n; ++i)
    {
        unsigned p;
        fi >> p;
        diners.push_back(p);
    }
    sort(diners.begin(), diners.end());
}

void Pan::solve()
{
    // result = (dbg_flags & 0x1) ? heap_solve() : sub_solve(diners);
    // vvu_t steps;
    // result = sub_solve(diners, steps, 0);
    result = sub_solve(diners);
#if 0
    if (dbg_flags & 0x8)
    {
        for (unsigned s = 0; s < steps.size(); ++s)
        {
            const vu_t &step = steps[s];
            cerr << "step " << s << " { #=" << step.size();
            for (unsigned i = 0; i < step.size(); ++i)
            {
                cerr << "  " << step[i];
            }
            cerr << "}\n";
        }
    }
#endif
}

unsigned Pan::sub_solve(vu_t sub_diners) const
{
    unsigned sz = sub_diners.size();
    unsigned pmax = sub_diners[sz - 1];
    unsigned sub_result = pmax;

    if (dbg_flags & 0x2)
    {   
        cerr << "{ #=" << sz;
        for (unsigned i = 0; i < sub_diners.size(); ++i)
        {
            cerr << " ["<<i<<"]="<<sub_diners[i]; 
        }
        cerr << "}  pmax=" << pmax << "\n";
    }

    // unsigned low = sz > 2 ? sub_diners[sz - 2] : 2;
    // unsigned low = isqrt(pmax);
    // unsigned low = 1;
    unsigned low = (pmax > 3 ? isqrt(pmax) : 3);
    // vu_t best_step(sub_diners);
    sub_diners.push_back(0); // dummy
    const vu_t sub_diners_orig(sub_diners);
    for (unsigned nd = low; nd <= pmax/2; ++nd)
    {
        vvu_t sub_steps;
        sub_diners = sub_diners_orig;
        sub_diners[sz - 1] = nd;
        sub_diners[sz] = pmax - nd;
        sort(sub_diners.begin(), sub_diners.end());
        // unsigned res = sub_solve(sub_diners, sub_steps, depth + 1) + 1;
        unsigned res = sub_solve(sub_diners) + 1;
        if (sub_result > res)
        {
            // best_step = sub_diners;
            if (dbg_flags & 0x2)
            {   
                cerr << "{ #=" << sz;
                for (unsigned i = 0; i < sub_diners.size(); ++i)
                {
                    cerr << " ["<<i<<"]="<<sub_diners[i]; 
                }
                cerr << "}  pmax=" << pmax << ", sRes=" << res << "\n";
            }
            // steps = sub_steps;
            sub_result = res;
        }
    }
    // steps.push_back(best_step);
    return sub_result;
}


unsigned Pan::heap_solve()
{
    make_heap(diners.begin(), diners.end());
    return sub_heap_solve();
}

unsigned Pan::sub_heap_solve()
{
    unsigned in_sz = diners.size();
    unsigned pmax = diners.front();
    if (dbg_flags & 0x2)
    {   
        cerr << "{ #=" << in_sz;
        for (unsigned i = 0; i < diners.size(); ++i)
        {
            cerr << " ["<<i<<"]="<<diners[i]; 
        }
        cerr << "}  pmax=" << pmax << "\n";
    }
    unsigned sub_result = pmax;
    // unsigned low = isqrt(pmax);
    unsigned low = 1;
    pop_heap(diners.begin(), diners.end());  diners.pop_back();
    for (unsigned nd = low; nd <= pmax/2; ++nd)
    {
        diners.push_back(nd);        push_heap(diners.begin(), diners.end());
        diners.push_back(pmax - nd); push_heap(diners.begin(), diners.end());
        unsigned res = sub_heap_solve() + 1;
        if (sub_result > res)
        {
            sub_result = res;
            if (dbg_flags & 0x4)
            {
                 cerr << "#="<<in_sz<< ", pmax="<<pmax <<
                     ", nd="<<nd << ", sub_res="<<sub_result<<"\n";
            }
        }
        // These 2 pops are wrong !!
        pop_heap(diners.begin(), diners.end());  diners.pop_back();
        pop_heap(diners.begin(), diners.end());  diners.pop_back();
    }
    diners.push_back(pmax); push_heap(diners.begin(), diners.end());
    return sub_result;
}

void Pan::print_solution(ostream &os)
{
    os << " " << result;
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

    if (argc > 3) { dbg_flags = strtoul(argv[3], 0, 0); }

    unsigned n_cases;
    *pfi >> n_cases;

    ostream &fout = *pfo;
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        Pan problem(*pfi);
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

