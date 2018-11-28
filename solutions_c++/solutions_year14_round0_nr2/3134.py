#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <fstream>
#include <ctime>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair

using namespace std;

typedef pair<LL,int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const double PI = 2*acos(0.0);
const double eps = 1e-9;
const int infi = 2e9;
const LL Linfi = (LL) 1e18;
#define MOD 1000000007
#define maxn 100005


double C, F, X;

void thuchien(){
	double cur = 2.0;
	double ans = X/cur;
	double add_time = 0.0;
	FOR(i,1,5*1e6){
		add_time += C/cur;
		if(add_time > X/2.0) break;
		cur += F;
		ans = min(ans, add_time + X/cur);
	}
	//cout << add_time - X/2.0 << endl;
	printf("%.7lf\n", ans);
}

int main(){
    //std::ios::sync_with_stdio(0);
    #ifndef ONLINE_JUDGE
    freopen("test.inp","r",stdin);
    freopen("B.out","w",stdout);
    #endif
    int sotest = 0;
    cin >> sotest;
    FOR(test,1,sotest){
		cin >> C >> F >> X;
		cout << "Case #" << test << ": ";
		thuchien();
    }
    return 0;
}


