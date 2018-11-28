#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define PB              push_back
#define SIZE(x)         (int)x.size()
#define clr(x,y)        memset(x,y,sizeof(x))
#define MP(x,y)         make_pair(x,y)
#define RS(n)           scanf ("%s", n)
#define ALL(t)          (t).begin(),(t).end()
#define FOR(i,n,m)      for (int i = n; i <= m; i ++)
#define ROF(i,n,m)      for (int i = n; i >= m; i --)
#define IT              iterator
#define FF              first
#define SS              second

typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long      ull;
typedef vector<int>             vint;
typedef vector<string>          vstring;
typedef pair<int, int>          PII;

void RI (int& x){
        x = 0;
        char c = getchar ();
        while (!(c>='0' && c<='9' || c=='-'))     c = getchar ();
        bool flag = 1;
        if (c == '-'){
                flag = 0;
                c = getchar ();
        }
        while (c >= '0' && c <= '9'){
                x = x * 10 + c - '0';
                c = getchar ();
        }
        if (!flag)      x = -x;
}
void RII (int& x, int& y){RI (x), RI (y);}
void RIII (int& x, int& y, int& z){RI (x), RI (y), RI (z);}
void RC (char& c){
        c = getchar ();
        while (c == ' '||c == '\n')     c = getchar ();
}
char RC (){
        char c = getchar ();
        while (c == ' '||c == '\n')     c = getchar ();
        return c;
}

/**************************************END define***************************************/

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

PII a[10005];
int b[10005];
int c[10005];

int n;

int main (){
        freopen ("11.txt", "r", stdin);
        freopen ("out1.txt", "w", stdout);
        int T, cass = 1;
        RI (T);
        while (T --){
                printf ("Case #%d: ", cass ++);
                RI (n);
                FOR (i, 1, n){
                        RI (a[i].FF);
                        a[i].SS = i;
                        b[i] = a[i].FF;
                }
                sort (a+1, a+n+1);
                int ans = 0;
                FOR (i, 1, n){
                        int p = a[i].SS;
                        int num = 0;
                        FOR (j, 1, p){
                                if (b[j] > b[p]){
                                        num ++;
                                }
                        }
                        ans += min (num, n-i-num);
                }
                
                printf("%d\n", ans);
        }
}
