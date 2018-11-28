// In the Name of Allah
// AD13

//think --> idea? --> really works? (create test cases) --> code it! --> test again
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long long ll;		//	typedef unsigned long long  ull;
typedef pair <int, int> pii;//	typedef pair <double, double> pdd;
typedef vector <int> VI;
#define MP make_pair
const int INF = 2147483647, MOD = 1000*1000*1000 + 7;
const double eps = 1e-8; // (eps < 1e-15) is the fact (1e-14)
#define For(i, n) for (int i = 0; i < (n); i++)
#define For1(i, n) for (int i = 1; i <= (n); i++)
//#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << "_" << err << "_"; exit(0); }
int gcd(int a, int b) { return (b==0)? a: gcd(b, a%b); }
/*-------------------------------------------------------------------------------------*/

vector<vector<int>> arr;
vector<int> ans;
vector<int> result, res;
bool used[100];

int n, size;

bool f (const int cnt) {
	const int cur = ans[cnt - 1];

	// cerr << "\t" << cnt << " -->";
	// for (int i = 0; i < cnt; i++) cerr << " " << ans[i]; cerr << endl;

	if (cnt == n) {
		int lost = 0;

		for (int col = 0; col < n; col++) {
			for (int i = 0; i < n; i++) {
				res[i] = arr[ans[i]][col];
			}
			bool found = false;
			for (int i = 0; i < size; i++) {
				if (used[i]) continue;
				found = true;
				for (int j = 0; j < n && found; j++) {
					found &= (res[j] == arr[i][j]);
				}
				if (found) break;
			}
			if (!found) {
				for (int i = 0; i < n; i++) result[i] = res[i];
				lost++;
			}
		}

		return lost == 1;
	}

	for (int i = 0; i < size; i++) {
		if (used[i]) continue;
		bool isGood = true;
		for (int j = 0; j < n && isGood; j++) {
			isGood &= arr[cur][j] < arr[i][j];
		}
		if (isGood) {
			used[i] = true;
			ans[cnt] = i;
			bool ok = f(cnt + 1);
			used[i] = false;
			if (ok) return true;
		}
	}

	return false;
}

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		cerr << "--> " << tc << " / " << T << endl;
		cin >> n;
		size = 2 * n - 1;

		arr.clear();
		arr.resize(size, vector<int>(n));
		ans.resize(n);
		res.resize(n);
		result.resize(n);

		For (i, size) For (j, n)
			cin >> arr[i][j];

		For (i, size) {
			used[i] = true;
			ans[0] = i;
			bool ok = f(1);
			used[i] = false;
			if (ok) break;
		}

		cout << "Case #" << tc << ": ";
		for (int i = 0; i < n; i++) cout << result[i] << ' ';
		cout << endl;
	}

	return 0;
}
/*
1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3

*/