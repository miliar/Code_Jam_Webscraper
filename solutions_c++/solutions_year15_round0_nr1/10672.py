#pragma comment (linker,"/STACK:16000000")
#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 
#include <functional>

using namespace std;

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const double pi = 3.1415926;
const ld eps = 1e-9;
const int N = (int)1e5 + 5;
const int INF = (int)1e9 + 7;

const double EPS = 0.00001;


int main() {
	freopen("a", "r", stdin);
	freopen("ans", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int k;
		cin >> k;
		string s;
		cin >> s;
		int ss = 0, d = 0;
		for (int j = 0; j < s.size(); j++)
		{
			if (j <= ss) ss += s[j] - '0';
			else 
			{
				d += j - ss;
				ss += j - ss + s[j] - '0';
			}
		}
		cout << "Case #" << i+1 << ": " << d << endl;
	}
	return 0;
}