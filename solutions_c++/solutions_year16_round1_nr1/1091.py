#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1000006
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;
string s;
deque<char> ans;
int main () {
	int tc;
	sc1(tc);
	FN (itc, tc) {
		cin >> s;
		ans.clear();
		ans.push_back(s[0]);
		FOR (i, 1, SZ(s)) {
			if (s[i] < ans[0]) ans.push_back(s[i]);
			else ans.push_front(s[i]);
		}
		printf("Case #%d: ", (itc + 1));
		FN (i, SZ(s)) putchar(ans[i]);
		puts("");
	}
}
