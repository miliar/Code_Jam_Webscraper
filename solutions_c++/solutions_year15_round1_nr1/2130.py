
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <list>
using namespace std;
inline int toInt(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string toString(T x) { ostringstream sout; sout << x; return sout.str(); }
template<class T> inline T sqr(T x) { return x*x; }
typedef pair<int, int> P;
typedef long long ll;
typedef unsigned long long ull;

#define For(i,a,b)	for(int (i) = (a);i < (b);(i)++)
#define rep(i,n)	For(i,0,n)
#define clr(a)		memset((a), 0 ,sizeof(a))
#define mclr(a)		memset((a), -1 ,sizeof(a))
#define all(a)		(a).begin(),(a).end()
#define rall(a)		(a).rbegin(), (a).rend()
#define sz(a)		(sizeof(a))
#define Fill(a,v)	fill((int*)a,(int*)(a+(sz(a)/sz(*(a)))),v)

bool cheak(int x, int y, int xMax, int yMax){ return x >= 0 && y >= 0 && xMax > x && yMax > y; }
const int dx[4] = { -1, 0, 1, 0 }, dy[4] = { 0, 1, 0, -1 };
const int mod = 1000000007;
const int INF = 1e9;


int main()
{
	int N;
	cin >> N;

	rep(Case, N){
		int n;
		cin >> n;
		ll m[10100];
		rep(i, n)cin >> m[i];
		ll Min = 0;
		ll Max = 0;
		ll tm = 0;

		rep(i, n-1){
			ll t = m[i] - m[i + 1];
			if (t > 0){
				Min += t;
				tm = max(tm, t);
			}
		}

		rep(i, n){
			if (i != n-1)
			Max += min(m[i], tm);
		}
		

		cout << "Case #" << Case + 1 << ": " << Min << " " << Max << endl;
	}


	return 0;
}
