//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <ctime>
using namespace std;

#define mp make_pair
#define rep(i,n) for(int i=0,_n=n;i<_n;i++)
#define reps(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define pi 2.0*acos(0.0)
#define MAX 2147483647
#define MIN -2147483647
#define torad(a) (a*pi)/180.0;

#define eps 0.00000001
#define m_eps 0.00000000001
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front

typedef long long ll;
typedef vector<int>VI;
typedef map<string,int> MSI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    double C, F, X;
    int T, cas = 1;
    cin >> T;
    while(T --) {
        cin >> C >> F >> X;
        double ret  = m_eps;
        double hi   = 1e9, low = 0;
        C += m_eps;
        F += m_eps;


        for(int iter = 0; iter <= 500; iter ++) {
            double mid = (hi + low)/2;
            double jump = min(mid, C/2.0), pp = 2.0;
            double points = 2.0 * mid, time = jump + eps;

            while(1) {
                if(!(points < X))break;
                double x = mid - time;
                if( x < 0 ) break;

                if( x * F < C) {
                    break;
                } else {
                    pp += F;
                    points = pp * x;
                    jump = C/pp;
                    time = min(mid, time + jump);
                }
            }

            if(!(points < X) ) {
                ret = mid;
                hi = mid - eps;
            } else {
                low = mid + eps;
            }
        }
        printf("Case #%d: %.8lf\n", cas ++, ret);
        //cout << ret << endl;
    }
    return 0;
}
