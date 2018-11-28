#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>  // File RW
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#define FILL(a, v) (memset(a, v, sizeof(a)))
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Int2;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const int MOD = 1000000007;
const double eps = 1e-10;
const double pi = acos(-1.0);

inline void AddMod(int &x, int det) { x += det; if( x >= MOD ) x -= MOD; }
inline int CompareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }
template<typename T> int sz(const T &a) { return a.size(); }
template<typename T> T str2num(string s) { istringstream i(s); T x; i>>x; return x; }
template<typename T> string x2str(T x) { ostringstream o; o<<x; return o.str(); }

int main()
{
	int cas;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		int r1, r2;
		int a[4][4], b[4][4];
		cin>>r1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>a[i][j];
		cin>>r2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>b[i][j];

		set<int> st;
		int cnt=0, ans=0;
		for(int j=0; j<4; j++)
			st.insert(a[r1-1][j]);
		for(int j=0; j<4; j++)
			if( st.find(b[r2-1][j]) != st.end() )
			{
				cnt++;
				ans = b[r2-1][j];
			}
		printf("Case #%d: ", c);
		if( cnt == 0 )
			puts("Volunteer cheated!");
		else if( cnt > 1 )
			puts("Bad magician!");
		else
			printf("%d\n", ans);
	}

	return 0;
}
