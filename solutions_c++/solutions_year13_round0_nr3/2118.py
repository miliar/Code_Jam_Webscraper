#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
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
#define sz(a) ((int)(a).size())
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int compareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

int main()
{
	set<int> st;
	int cas, a, b;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	st.insert(1);  st.insert(4);  st.insert(9);
	st.insert(121);  st.insert(484);
	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		cin>>a>>b;
		int ans = 0;
		foreach(ptr, set<int>, st)
			if( (*ptr)>=a && (*ptr)<=b )
				ans++;
		printf("Case #%d: %d\n", c, ans);
	}

	return 0;
}
