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
int a[5][5],b[5][5];
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cout << "Case #" << test << ": ";
        cin >> n;
        For(i,1,4) For(j,1,4) cin >> a[i][j];
        cin >> m;
        For(i,1,4) For(j,1,4) cin >> b[i][j];
        int res=0,vt=0;
        For(i,1,4) For(j,1,4) if (a[n][i] == b[m][j]) {
            res++;
            vt = a[n][i];
        }
        if (res==1)cout << vt << endl;
        else if (res==0) cout << "Volunteer cheated!" << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}




