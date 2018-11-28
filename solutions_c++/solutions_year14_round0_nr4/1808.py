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
double a[nmax],b[nmax];
int dp[1111][1111];
int main() {
    freopen("input.txt","r",stdin);
    freopen("outputD.txt","w",stdout);
    //ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cin >> n;
        For(i,1,n) cin >> b[i];
        For(i,1,n) cin >> a[i];
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int res1 = 0;
        For(i,0,n) For(j,0,n) dp[i][j] = 0;
        dp[0][0] = 1;
        For(i,0,n-1) For(j,0,n) if (dp[i][j]) {
            int head = j+1;
            int tail = n-j;
            if (b[i+1]>a[head]) dp[i+1][j+1] = true;
            if (b[i+1]<a[tail]) dp[i+1][j] = true;
        }
        For(j,1,n) if (dp[n][j]) res1 = j;
        int j = n;
        int res2 = 0;
        Ford(i,n,1){
             while (j>0 && b[j]>a[i]) j--;
             res2+=(j>0);
             j--;
        }
        printf("Case #%d: %d %d\n",test,res1,n-res2);
    }
    return 0;
}




