//#pragma comment(linker,"/STACK:102400000,102400000")
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

#define FF first
#define SS second
#define MP make_pair
#define PB push_back
#define lson rt << 1, l, mid
#define rson rt << 1 | 1, mid + 1, r

typedef long long LL;
typedef pair<LL, LL> PLL;
typedef pair<int, int> PII;
typedef unsigned long long ULL;

inline int read(){
    int x = 0; char ch = getchar(); bool positive = 1;
    for (; ch < '0' || ch > '9'; ch = getchar())    if (ch == '-')  positive = 0;
    for (; ch >= '0' && ch <= '9'; ch = getchar())    x = x * 10 + ch - '0';
    return positive ? x : -x;
}

inline char RC (){
    char c = getchar ();
    while (c == ' '||c == '\n')     c = getchar ();
    return c;
}

inline int gcd(int a, int b) {return b?gcd(b, a%b):a;}

inline int ADD(int x, int y, int mod){
    int res = x + y;
    while(res >= mod)  res -= mod; while(res < 0) res += mod;
    return res;
}

inline LL POW_MOD(LL x, LL y, LL mod){
    LL ret = 1;
    while(y){
        if(y & 1)  ret = ret * x % mod;
        x = x * x % mod;
        y >>= 1;
    }
    return ret;
}

/****************************define***************************************/

const LL INF = 9e15;
const int inf = 0x7fffffff;
const int N = 100000+10;
const int M = 500;
const LL MOD = 1000000007;
const double PI = acos(-1.0);
const double G = 9.8;
const double eps = 1e-3;

double radio1, radio2;

struct node{
	int kind;
	double salary, t, fk;
	double ans;
	node(int aa, double a, double b, double c): kind(aa), salary(a), t(b), fk(c){}
	~node(){}
};

vector<node> v;

map<int,double> need;
map<int,double> possible;

void pre(){
	for(int i = 1; i <= 7; ++ i){
		cin >> need[i] >> possible[i];
	}
}

void input(){
	int n; cin >> n;
	cin >> radio1 >> radio2;
	for(int i = 0; i < n; ++ i){
		int aa; cin >> aa;
		double a, b, c; cin >> a >> b >> c;
		v.PB(node(aa, a, b, c));
	}
}

void cal(){
	for(int i = 0; i < v.size(); ++ i){
		v[i].ans = v[i].salary - radio1 * v[i].t * need[v[i].kind] / possible[v[i].kind] + radio2 * v[i].fk;
	}
	for(int i = 0; i < v.size(); ++ i){
		cout << v[i].ans << endl;
	}
}

void solve(){
	pre();
	input();
	cal();
}

int main(){
	freopen("/Users/w/Desktop/in.txt", "r", stdin);
	freopen("/Users/w/Desktop/out.txt", "w", stdout);
	solve();
	return 0;
}