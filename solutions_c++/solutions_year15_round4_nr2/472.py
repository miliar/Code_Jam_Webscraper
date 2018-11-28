#include <string.h>
#include <assert.h>
#include <stdio.h>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

const double EPS = 1e-5;

void solve(const int t)
{
    int N;
    double V, X;
    vector<double> R, C;
    assert(cin >> N >> V >> X);
    R.resize(N);
    C.resize(N);
    for(int i = 0; i < N; ++i)
        assert(cin >> R[i] >> C[i]);
    
    double _max, _min;
    if(N == 1)
    {
        _max = _min = C[0];
    }
    else
    {
        _min = min(C[0], C[1]);
        _max = max(C[0], C[1]);
    }
    if((X < _min - EPS) || (X > _max + EPS))
    {
        printf("Case #%d: IMPOSSIBLE\n", t);
        return;
    }
    
    for(int i = 0; i < N; ++i)
        C[i] -= X;
    
    double res;
    if(N == 1)
    {
        res = V / R[0];
    }
    else if(fabsl(C[0] - C[1]) < EPS)
    {
        res = V / (R[0] + R[1]);
    }
    else if(fabsl(C[0]) < EPS || fabsl(C[1]) < EPS)
    {
        res = V / ((fabsl(C[0]) < EPS) ? R[0] : R[1]);
    }
    else
    {
        double t1 = V / ((1.0 - C[0] / C[1]) * R[0]);
        double t2 = -t1 * R[0] * C[0] / (R[1] * C[1]);
        cerr << t1 << " " << t2 << "\n";
        assert(t1 >= -EPS && t2 >= -EPS);
        res = max(t1, t2);
    }
    printf("Case #%d: %.9f\n", t, res);
}

int main()
{
    int T;
    
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        cerr << "Solving #" << t << "\n";
        solve(t);
    }
    return 0;
}
