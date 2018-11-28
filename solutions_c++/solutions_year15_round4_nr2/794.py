/* Divanshu Garg */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
ill ABS(ill a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

/* Input opener ends */

#define EPS 1e-8


int main() {
    input();

    int t, kase = 1; cin >> t;
    while ( t-- ) {

        int n; double V, X;
        cin >> n >> V >> X;
        // cout << n << " " << V << " " << X << endl;
        double R[5], C[5];
        F(i,0,n) {
            cin >> R[i] >> C[i];
            // cout << R[i] << " " << C[i] << endl;
        }


        if ( n == 1 ) {

            if ( abs(C[0]-X) < EPS ) {
                printf("Case #%d: %.9lf\n", kase++, (V/R[0]) );  
            } else {
                printf("Case #%d: IMPOSSIBLE\n", kase++);  
            }

        } else {

            double mnt = min(C[0],C[1]);
            double mxt = max(C[0],C[1]);

            if ( X+EPS < mnt || X-EPS > mxt ) {
                printf("Case #%d: IMPOSSIBLE\n", kase++);  
            } else {

                if ( abs(C[0]-C[1]) < EPS ) {
                    // cout << "enter" << endl;
                    double Rm = R[0]+R[1];
                    printf("Case #%d: %.9lf\n", kase++, (V/Rm) ); 
                } else {

                    double Rc = R[0] + R[1];
                    double Cc = (R[0]*C[0] + R[1]*C[1])/(R[0]+R[1]);

                    double V0 = V*(X-C[1]);
                    V0 /= (C[0]-C[1]);
                    // assert(V0>=0.0);
                    double V1 = V-V0;

                    // cout << "V -- " << V0 << " " << V1 << endl;
 
                    double ans = max( V0/R[0], V1/R[1] );
                    printf("Case #%d: %.9lf\n", kase++, ans); 
                }

            }

        }

        // cout <<endl << endl;

              

    }

    return 0;
}


