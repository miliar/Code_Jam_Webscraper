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
const int nmax = 100;
const double e = 1e-8;
const double pi = acos(-1);
typedef long long ll;
typedef pair<int,int> pii;
int n,m,stest,res,ressl,cal[nmax],c[nmax];
string ss[nmax];
struct node {
    node *next[26];
};
node* s[6];
void add(node *cur, string s,int pos) {
    if (pos==sr(s)) return;
    int tmp = s[pos]-'A';
    if (cur->next[tmp]==NULL) {
        cur->next[tmp] = new node;
        For(i,0,25) cur->next[tmp]->next[i] = NULL;
    }
    add(cur->next[tmp], s , pos+1);
}
int Cal(node *cur) {
    int sol = 1;
    For(i,0,25) if (cur->next[i]!=NULL) sol+=Cal(cur->next[i]);
    return sol;
}
void Del(node *cur) {
    int sol = 1;
    For(i,0,25) if (cur->next[i]!=NULL) Del(cur->next[i]);
    delete cur;
}
void check() {
    For(i,1,n) if (cal[i]==0) return;
    //PR(c,1,m);
    For(i,1,n) {
        s[i] = new node;
        For(j,0,25) s[i]->next[j]=NULL;
    }
    //PR(c,1,n);
    For(i,1,m) add(s[ c[i] ], ss[i],0);
    //PR(c,1,n);
    int sol=0;
    For(i,1,n) sol+=Cal(s[i]);
    //PR(c,1,n);
    For(i,1,n) Del(s[i]);
    if (res<sol) {
        res=sol;ressl=1;
    } else if (res==sol) ressl++;
}
void DFS(int i) {
    if (i==m+1) check(); else  {
        For(j,1,n) {
            c[i]=j;
            cal[j]++;
            DFS(i+1);
            cal[j]--;
        }
    }
}
int main() {
    freopen("D-small-attempt1.in","r",stdin);
    freopen("outputD.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> stest;
    For(test,1,stest) {
        cin >> m >> n;
        For(i,1,m) {
            cin >> ss[i];
        }
        res=0; ressl=0;
        For(i,1,n) cal[i]=0;
        DFS(1);
        cout << "Case #" << test << ": " << res << " "<< ressl << endl;
    }
    return 0;
}




