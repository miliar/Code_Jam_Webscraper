#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#define FOR(i,a,b) for (typeof(b) i=a; i <=b ; i++)
#define FO(i,a,b) for (typeof(b) i=a; i < b ; i++)
#define FORD(i,a,b) for (typeof(a) i=a; i >=b ; i--)
#define SET(arr,c) memset(arr,c,sizeof(arr))
#define LL long long
#define ULL unsigned long long
#define mp make_pair
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define PI 2*acos(0,0)
#define MOD 1000000007
#define infi 1e18
#define oo 1e18
using namespace std;

template <class T> int getbit(int i, T X) { return (X & (1<<(i-1))); }
template <class T> T onbit(int i, T X) { return (X | (1<<(i-1))); }
template <class T> T offbit(int i, T X) { return (X | (1<<(i-1)) - (1<<(i-1))); }
template <class T> T sqr(T x) { return (x*x); }
template <class T> T cube (T x) { return (x*x*x); }
template <class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template <class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int csx[4]={0,0,-1,1};
int csy[4]={-1,1,0,0};

typedef pair <int, int> II;

/******VAR******/
int test, n, tmp, need;
string s;
/***************/

int main() {
	ios::sync_with_stdio(false);
//	freopen("test.in", "r", stdin);
//	freopen("test.out", "w", stdout);
	cin >> test;
	FOR(t, 1, test) {
	    cin >> n;
	    cin >> s;
	    tmp = s[0] - '0';
	    int need = 0;
	    FOR(i, 1, n) {
	        if (tmp >= i) tmp += s[i] - '0';
	        else {
                need += i - tmp;
                tmp += i - tmp + s[i] - '0';
	        }
	    }
	    cout << "Case #" << t << ": " << need << endl;
	}
	return 0;
}
