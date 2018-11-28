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


map<int, int> mmap;
int n, m;
string s[100];
int a[100];

int chd[10000][26];
int top;

void insert (string s){
        //cout << s << endl;
        int now = 0;
        FOR (i, 0, SIZE (s)-1){
                int x = s[i] - 'A';
                if (!chd[now][x])       chd[now][x] = top ++;
                now = chd[now][x];
        }
}

void dfs (int p){
        if (p > m){

                bool flag[5] = {0};
                FOR (i, 1, m){
                        flag[a[i]] = 1;
                }
                int tt = true;
                FOR (i, 1, n){
                        if (!flag[i]){
                                tt = false;
                        }
                }
                if (!tt)        return;
                        /*FOR (i, 1, m){
                        cout << a[i] << " ";
                }
                cout << endl;*/
                
                int ans = 0;
                FOR (i, 1, n){
                        clr (chd, 0);
                        top = 1;
                        FOR (j, 1, m){
                                if (a[j] == i){
                                        insert (s[j]);
                                }
                        }
                        //cout << top << endl;
                        ans += top;
                }
                mmap[ans] ++;
                return;
        }
        FOR (i, 1, n){
                a[p] = i;
                dfs (p+1);
        }
}

int main (){
        freopen ("in.txt", "r", stdin);
        freopen ("out.txt", "w", stdout);
        int T, cass = 1;
        RI (T);
        while (T --){
                printf ("Case #%d: ", cass ++);
                mmap.clear ();
                RII (m, n);
                FOR (i, 1, m){
                        cin >> s[i];
                }
                dfs (1);
                map<int, int>::IT it = mmap.end ();
                it --;
                printf("%d %d\n", it->FF, it->SS);
        }
}
