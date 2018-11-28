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
const int nmax = 10010;
const double e = 1e-8;
const double pi = acos(-1);
typedef long long ll;
typedef pair<int,int> pii;
int n,X,stest;
int bit[nmax],s[nmax],Fre[nmax];
void add(int i,int x) {
    for ( ; i<=n; i+=i&(-i)) bit[i]+=x;
}
int query(int i) {
    int x=0;
    for (; i>0; i-=i&(-i)) x+=bit[i];
    return x;
}
int Find(int x) {
    int l=1,r=n,res=-1;
    while (l<=r) {
        int mid = (l+r) >> 1;
        if (s[mid]<=x) {
            res=mid;
            l=mid+1;
        } else r=mid-1;
    }
    return res;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cin >> n >> X;
        For(i,1,X) bit[i]=0;
        For(i,1,n) Fre[i]=true;
        For(i,1,n) cin >> s[i];
        sort(s+1,s+n+1);
        //PR(s,1,n);
        For(i,1,n) add(i,1);
        int res=0;
        Ford(i,n,1) if (Fre[i]) {
            Fre[i]=false;
            add(i,-1);
            res++;
            int j = Find(X-s[i]);
            //BUG(j);
            if (j!=-1) {
                int l = 1, r = j;
                int cur=-1;
                while (l<=r) {
                    int mid = (l+r) >> 1;
                    if (query(j)-query(mid-1)>0) {
                        cur = mid;
                        l=mid+1;
                    } else r=mid-1;
                }
                if (cur!=-1) {
                    Fre[cur]=false;
                    add(cur,-1);
                }
            }
        }
        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}




