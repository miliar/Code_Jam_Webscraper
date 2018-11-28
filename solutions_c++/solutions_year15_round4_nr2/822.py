#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
typedef long long ll;

double R[110], C[110];

const double EPS = 1e-8;

void work()
{
    int N;
    double V, X;
    cin >> N >> V >> X;
    
    for (int i = 0; i < N; ++ i) {
        cin >> R[i] >> C[i];
    }
    
    if (N == 1) {
        if (fabs(C[0] - X) < EPS) {
            cout << V / R[0] << endl;
        }
        else
        {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    else
    {
        if (C[0] > C[1]) {
            swap(C[0], C[1]);
            swap(R[0], R[1]);
        }
        
        if (fabs(C[0] - X) < EPS && fabs(C[1] - X) < EPS) {
            cout << V / (R[0] + R[1]) << endl;
            return;
        }
        
        if (fabs(C[0] - X) < EPS) {
            cout << V / R[0] << endl;
            return;
        }
        
        if (fabs(C[1] - X) < EPS) {
            cout << V / R[1] << endl;
            return;
        }
        
        if (C[0] > X) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        
        if (C[1] < X) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        
        
        //double t1 = (V * X - V * C[0]) / (C[1] - C[0]);
        //double t2 = (V * X - V * C[1]) / (C[0] - C[1]);
        //cout << t1 << " " << t2 << endl;
        cout << max((V * X - V * C[0]) / (C[1] - C[0]) / R[1], (V * X - V * C[1]) / (C[0] - C[1]) / R[0]) << endl;
    }
}

int main()
{
    ios :: sync_with_stdio(false);
    cout << fixed << setprecision(16);
    int T;
    scanf("%d", &T);
    int kase = 1;
    while (T --) {
        printf("Case #%d: ", kase ++);
        work();
    }
    return 0;
}