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
	int a[100][100];

	for(int o = 0; o < t; o++) {
		
		int n,m;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> a[i][j];
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++) {
				bool f1 = false, f2 = false;
				for(int k = 0; k < n; k++)
					if(a[i][j] < a[k][j]) f1 = true;
				for(int k = 0; k < m; k++)
					if(a[i][j] < a[i][k]) f2 = true;
				if(f1 && f2) {
					cout << "Case #" << o+1 << ": " << "NO" << endl;
					goto end;
				}
			}
		cout << "Case #" << o+1 << ": " << "YES" << endl;
end:
		;
	}
}