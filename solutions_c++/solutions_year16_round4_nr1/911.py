/***************************************
      zzblack                         **
      2016-05-28                      **
      Orz                             **
****************************************/
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<int,int> pii ;
const int maxn = 1e5 + 50 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

inline int read(){
    char c = getchar();
    while (!isdigit(c)) c = getchar();
    int x = 0;
    while (isdigit(c)) {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x;
}

int dfs(int a, int b, int c){
    int tot = a + b + c;
    if (tot == 1) {
        if (a) return 1;
        if (b) return 2;
        return 0;
    }
    if(a << 1 > tot || b << 1 > tot || c << 1 > tot) throw 1;
    int na = a + b - c >> 1, nb = c + b - a >> 1, nc = a + c - b >> 1;
    return dfs(na, nb, nc);
}

char ch[3] = {'P', 'R', 'S'};

int n, a, b, c;

string print(int Win, int dep) {
    if(!dep) {
        string s = "";
        return s + ch[Win];
    }
    string s = print(Win, dep-1);
    string t = print((Win+1)%3, dep-1);
//    cout << "t = " << t << "\n";
//    cout << "s = " << s << "\n";
    if (s > t) swap(s,t);
    return s + t;
}

int main () {
#ifdef LOCAL
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
      freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
    int T = read(), cas = 1;
    while (T--) {
        printf("Case #%d: ", cas++);
        n = read(), a = read(), c = read(), b = read();  // a = rock, b = scissor, c = paper
//        cout << (1 << n) << " " << a << " " << b << " " << c << "\n";
        try {
            int ans = dfs(a, b, c);
//            printf("%c\n", ch[ans]);
           cout << print(ans, n) << "\n";
        } catch(int) {
            puts("IMPOSSIBLE");
        }
    }


	return 0;
}
