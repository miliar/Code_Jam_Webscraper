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
int n,m,stest,a[nmax],c[nmax],b[nmax],res,Fre[nmax];
int rr[nmax],pos[nmax];
void check() {
    int sol=0;
    int i=1;
    while (i<n && a[c[i]] < a[c[i+1]]) i++;
    while (i<n && a[c[i]] > a[c[i+1]]) i++;
    if (i!=n) return;
    For(i,1,n) b[i]=i;
    For(i,1,n) {
        int pos=0;
        For(j,i,n) if (c[i] == b[j]) {
            pos=j;
            break;
        }
        while (pos>i) {
            swap(b[pos-1],b[pos]);
            pos--;
            sol++;
        }
    }
    res = min(res,sol);
}
void DFS(int i) {
    if (i>n) check(); else  {
        For(j,1,n) if (Fre[j]) {
            c[i]=j;
            Fre[j]=0;
            DFS(i+1);
            Fre[j]=1;
        }
    }
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("outputB.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cin >> n;
        For(i,1,n) cin >> a[i];
        res = n*n;
        For(i,1,n) Fre[i]=1;
        //DFS(1);

        For(i,1,n) rr[i] = a[i];
        sort(rr+1,rr+n+1);
        For(i,1,n) a[i] = lower_bound(rr+1,rr+n+1,a[i])-rr;
        For(i,1,n) pos[ a[i] ] = i;
        //PR(a,1,n);
        res = 0;
        Ford(i,n-1,1) {
            if (pos[i]<pos[n]) {
                int sol1 = 0;
                For(j,pos[i]+1,pos[n]-1) if (a[j]<i) sol1++;
                int sol2 = sol1;
                For(j,i+1,n) if (pos[j]<pos[i]) sol2--; else sol2++;
                res+=min(sol1,sol2);
            } else {
                int sol1 = 0;
                For(j,pos[n]+1,pos[i]-1) if (a[j]<i) sol1++;
                int sol2 = sol1;
                For(j,i+1,n) if (pos[j]>pos[i]) sol2--; else sol2++;
                res+=min(sol1,sol2);
            }

        }
        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}




