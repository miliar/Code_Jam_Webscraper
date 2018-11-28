#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <complex>
#include <queue>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define fi first
#define se second
#define sr(x) (int)x.size()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define Bit(s,i) ((s&(1<<i))>0)
#define Two(x) (1<<x)
const int modul = 1000000007;
const int nmax = 10000;
const double e = 1e-8;
const double pi = acos(-1);
typedef long long ll;
typedef pair<int,int> pii;
int n,m,stest;
double C,F,X;
int main() {
    freopen("input.txt","r",stdin);
    freopen("outputB.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cin >> C >> F >> X;
        double rate = 2.0;
        double time = 0;
        double res = X/2;
        while (time<res) {
            time += C/rate;
            rate += F;
            res = min(res, time + X/rate );
        }
        printf("Case #%d: %.7lf\n",test,res);
    }
    return 0;
}




