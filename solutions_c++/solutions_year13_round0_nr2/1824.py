//#pragma comment(linker, "/STACK:16777216")
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

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define pb push_back
#define f first
#define s second
#define mp make_pair
#define y0 y32479
#define y1 y95874

typedef long long ll;
typedef long double ld;

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-9;
const int INF = (int)1e9;
const int N = (int)200 + 10;

int t, n, m, a[N][N], row[N], st[N];

int main() {
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cout.flags(ios::fixed);
	cout.precision(2);
	ios_base::sync_with_stdio(0);
	cin >> t;
	for (int q = 0; q < t; q++) {
		cin >> n >> m;
		for (int i =0 ; i < n; i++)
			for (int j =0; j < m; j++) 
				cin >> a[i][j];
		for (int i = 0; i < n; i++)
			row[i] = 0;
		for (int i = 0; i < m; i++)
			st[i] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++)
				row[i] = max(row[i], a[i][j]);
		}
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n; i++)
				st[j] = max(st[j], a[i][j]);
		}
		/*cout << "ROW = " << endl;
		for (int i = 0; i < n; i++)
			cout << row[i] << ' ';
		cout << endl << endl;
		cout << "ST = " << endl;
		for (int i = 0; i < m; i++)
			cout << st[i] << ' ';
		cout << endl << endl;*/
		
		bool f = 1;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j] != st[j] && a[i][j] != row[i])
					f = 0;
		if (f)
			cout << "Case #" << q + 1 << ": YES\n";
		else
			cout << "Case #" << q + 1 << ": NO\n";
	}
	return 0;
}


