#pragma comment linker("/STACK:16000000");
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
const int N = (int)1e5+5;
const int INF = (int)1e9+10;

const double EPS = 0.00001;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
	cin >> t;
	ll mas[] = { 
0,
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004 
	};
	for(int o = 0; o < t; o++) {
		
		int a,b;
		cin >> a >> b;
		int s = 0;
		for(int i = 0; i < 27; i++) {
			if(mas[i] >= a && mas[i] <= b) s++;
		}
		cout << "Case #" << o+1 << ": " << s << endl;

	}
}