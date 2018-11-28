//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <stdlib.h>
#include <assert.h>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define SZ(cont) (int)(cont.size())
#define ALL(cont) (cont).begin(), (cont).end()
#define DEBUG(x) cerr << ">" << #x << ":" << x << endl

typedef long long int64;
typedef pair<int64, int64> ii;
typedef vector<int64> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo32 = 1ll << 30, oo64 = 1ll << 60;
const double pi = acos(-1.0), eps = 1e-9;
inline bool equal(const double &a, const double &b){return abs(a - b) < eps;}

template<class T> 
string to_string(const T &element)
{
	stringstream ss;
	ss << element;
	return ss.str();
}
bool palindrome(int64 n)
{
	//DEBUG(n);
	string s = to_string(n);
	int t = s.size() / 2;
	for(int i = 0; i < t; i++)
	{
		if(s[i] != s[s.size() - 1 - i])
			return false;
	}
	return true;
}
int64 mem[] = {
1l,
4l,
9l,
121l,
484l,
10201l,
12321l,
14641l,
40804l,
44944l,
1002001l,
1234321l,
4008004l,
100020001l,
102030201l,
104060401l,
121242121l,
123454321l,
125686521l,
400080004l,
404090404l,
10000200001l,
10221412201l,
12102420121l,
12345654321l,
40000800004l,
1000002000001l,
1002003002001l,
1004006004001l,
1020304030201l,
1022325232201l,
1024348434201l,
1210024200121l,
1212225222121l,
1214428244121l,
1232346432321l,
1234567654321l,
4000008000004l,
4004009004004l,
};
int calculate(int64 n)
{
	int c = 0;
	int64 a = 1;
	while(a * a <= n)
	{
		if(palindrome(a) && palindrome(a * a))
		{
			c++;
			//cout << (int64)a*a << "l," << endl;
		}
		a++;
	}
	return c;
}

int main()
{
//	freopen ("in.txt", "rt", stdin);
//	freopen ("out.txt", "wt", stdout);
	//cout << calculate(100000000000000l) << endl;
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		int64 a, b;
		cin >> a >> b;
		int ans = 0;
		for(int i = 0; i < 39; i++)
		{
			if (a <= mem[i] && mem[i] <= b)
			{
				ans++;
			}
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
