#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <limits>

using namespace std;
typedef std::numeric_limits< double > dbl;

ifstream input("./B-small-attempt0.in");
//#define input cin
ofstream out("./out.txt");
//#define out cout

struct source {
    double r;
    double t;
    double rest;
};

double V, X;

vector<source> sources;

bool possible(double t) {
    for (auto& s : sources)
        s.rest = t;

    int i = 0;
    int j = sources.size() - 1;
    double v = V;

    while (sources[i].t <= X && sources[j].t >= X) 
    {
        auto& h = sources[j];
        auto& c = sources[i];

        double y = (h.t - X) / (X - c.t);
        double v1, v2;
        double t1, t2;
        t1 = h.rest;
        t2 = c.rest;
        
        v1 = t1 * h.r;
        v2 = t2 * c.r;

        if (v2 / v1 > y) {
            t2 *= y * v1 / v2;
        } 

        if (v2 / v1 < y) {
            t1 /= y * v1 / v2;
        }

        v1 = t1 * h.r;
        v2 = t2 * c.r;

        v -= v1;

        if (i != j)
            v -= v2;

        if (v <= 0)
            return true;


        h.rest -= t1;
        c.rest -= t2;

        if (h.rest < 0.00000001)
            j--;

        if (c.rest < 0.00000001)
            i++;
    }

    return false;
}

void solve() {
    int N;
    
    input >> N >> V >> X;

    sources.resize(N);

    double mn = -1;
    for (int i = 0; i < N; i++) {
        source s;
        input >> s.r;
        input >> s.t;

        sources[i] = s;

        if (mn < 0 || mn > s.r)
            mn = s.r;
    }

    auto cmp = [](const source& lhs, const source& rhs) {
        return lhs.t < rhs.t;
    };
    sort(sources.begin(), sources.end(), cmp);

    if (sources.begin()->t > X || (sources.end() - 1)->t < X) {
        out << "IMPOSSIBLE" << endl;
        return;
    }

    double a = 0;
    double b = V / mn;

    for (int i = 0; i < 150; i++) {
        double c = (a + b) / 2.0;
        if (possible(c))
            b = c;
        else
            a = c;

        if (a == b)
            break;
    }

    out << a << endl;
}

int main(int argc, char** argv)
{
    int T;
    input >> T;

    out.precision(dbl::digits10);
    for (int t = 0; t < T; t++) {
        out << "Case #" << t + 1 << ": ";
        solve(); 
    }

    return 0;
}
