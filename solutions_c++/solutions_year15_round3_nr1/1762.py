
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
	int n;
	cin >> n;

	rep(Case, n){

		int ans;
		int r, c, w;
		cin >> r >> c >> w;
		if (c == 1){
			ans = 1;
		}
		if (c == 2){
			if (w == 1)ans = 2;
			if (w == 2)ans = 2;
		}
		if (c == 3){
			if (w == 1)ans = 3;
			if (w == 2)ans = 3;
			if (w == 3)ans = 3;
		}
		if (c == 4){
			if (w == 1)ans = 4;
			if (w == 2)ans = 3;
			if (w == 3)ans = 4;
			if (w == 4)ans = 4;
		}
		if (c == 5){
			if (w == 1)ans = 5;
			if (w == 2)ans = 4;
			if (w == 3)ans = 4;
			if (w == 4)ans = 5;
			if (w == 5)ans = 5;
		}
		if (c == 6){
			if (w == 1)ans = 6;
			if (w == 2)ans = 4;
			if (w == 3)ans = 4;
			if (w == 4)ans = 5;
			if (w == 5)ans = 6;
			if (w == 6)ans = 6;
		}
		if (c == 7){
			if (w == 1)ans = 7;
			if (w == 2)ans = 5;
			if (w == 3)ans = 5;
			if (w == 4)ans = 5;
			if (w == 5)ans = 6;
			if (w == 6)ans = 7;
			if (w == 7)ans = 7;
		}
		if (c == 8){
			if (w == 1)ans = 8;
			if (w == 2)ans = 5;
			if (w == 3)ans = 5;
			if (w == 4)ans = 5;
			if (w == 5)ans = 6;
			if (w == 6)ans = 7;
			if (w == 7)ans = 8;
			if (w == 8)ans = 8;
		}
		if (c == 9){
			if (w == 1)ans = 9;
			if (w == 2)ans = 6;
			if (w == 3)ans = 5;
			if (w == 4)ans = 6;
			if (w == 5)ans = 6;
			if (w == 6)ans = 7;
			if (w == 7)ans = 8;
			if (w == 8)ans = 9;
			if (w == 9)ans = 9;
		}
		if (c == 10){
			if (w == 1)ans = 10;
			if (w == 2)ans = 6;
			if (w == 3)ans = 6;
			if (w == 4)ans = 6;
			if (w == 5)ans = 6;
			if (w == 6)ans = 7;
			if (w == 7)ans = 8;
			if (w == 8)ans = 9;
			if (w == 9)ans = 10;
			if (w == 10)ans = 10;
		}
		

		cout << "Case #" << Case + 1 << ": " << ans << endl;
	}

	return 0;
}
