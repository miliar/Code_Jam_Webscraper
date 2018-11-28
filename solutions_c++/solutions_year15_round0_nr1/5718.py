
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
const int INF = 2147483647;


int main()
{
	int T;
	cin >> T;

	rep(Case, T){
		cout << "Case #" << Case + 1 << ": ";
		int n;
		cin >> n;
		string s;
		cin >> s;

		int ans = 0;
		int sum = s[0] - '0';
		For(i, 1, n + 1){
			if (s[i] != '0'){
				if (i > sum){
					ans += i - sum;
					sum += i - sum;
				}
				sum += s[i] - '0';
			}
		}
		cout << ans << endl;
	}

	return 0;
}
