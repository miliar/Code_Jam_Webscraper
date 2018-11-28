
#include <iostream>
#include <inttypes.h>
#include <vector>
#include <algorithm>
using namespace std;

class pass
{
public:
    int o, e, p;
};

bool operator<(const pass &l, const pass &r)
{
    return (l.e - l.o) > (r.e - r.o);
}

ostream& operator<<(ostream &os, const pass &r)
{
    os << "(" << r.o << " " << r.e << " " << r.p << ")";
    return os;
}

bool operator==(const pass &l, const pass &r)
{
    return l.o == r.o && l.e == r.e && l.p == r.p;
}

int main(int argc, char *argv[])
{
    int problems;
    cin >> problems;

    for (int prob=1; prob<=problems; ++prob) {
        int n, m;
        vector<pass> passes;

        cin >> n >> m;

        for (int i=1; i<=m; ++i) {
            pass p;

            cin >> p.o >> p.e >> p.p;
            passes.push_back(p);
        }

        // cerr << passes.size() << " passes\n";
        sort(passes.begin(), passes.end());

        // cerr << "start\n";

        int loss = 0;

        vector<pass> prev;

        do {
            prev = passes;
            for (int i=0; i<passes.size(); ++i) {
                // cerr << "loss " << loss << "\n";
                // cerr  << passes.size() << "\n";
                for (int j=0; j<passes.size(); ++j) {
//                if (!(o[i] < o[j] && o[j] <= e[i] && e[i] < e[j])) {
                    if (!(passes[i].o < passes[j].o && passes[j].o <= passes[i].e && passes[i].e < passes[j].e)) {
                        continue;
                    }

//                int l = ((e[i]-o[i])-(e[i]-o[j]))*(e[j]-e[i]);
                    int l = (passes[j].o-passes[i].o)*(passes[j].e-passes[i].e);
                    int pp = min(passes[i].p, passes[j].p);
                    loss += pp * l;

                    // cerr << i << " " << j << "\n";
                    // cerr << passes[i].o << " " << passes[i].e << " " << passes[i].p << ", "
                    //      << passes[j].o << " " << passes[j].e << " " << passes[j].p << ". "
                    //      << l << "x" << pp << "\n";
                    // cerr << "==================================================\n";
                    // for (int k=0; k<passes.size(); ++k) {
                    //     cerr << k << ":" << passes[k] << " ";
                    // }
                    // cerr << "\n--------------------------------------------------\n";

                    if (passes[j].o < passes[i].e) {
                        pass newp;
                        newp.o = passes[j].o;
                        newp.e = passes[i].e;
                        newp.p = pp;
                        passes.push_back(newp);
                    }

                    if (passes[i].p == passes[j].p) {
                        passes[i].e = passes[j].e;

                        passes.erase(passes.begin() + j);
                    }
                    else if (passes[i].p < passes[j].p) {
                        passes[i].e = passes[j].e;
                        passes[i].p = pp;

                        passes[j].p -= pp;
                    } else {
                        passes[j].o = passes[i].o;
                        passes[j].p = pp;

                        passes[i].p -= pp;
                    }
                
                    // for (int k=0; k<passes.size(); ++k) {
                    //     cerr << k << ":" << passes[k] << " ";
                    // }
                    // cerr << "\n==================================================\n";
                }
            }
        } while (prev != passes);
        cout << "Case #" << prob << ": " << (loss % 1000002013) << "\n";
    }
    return 0;
}
