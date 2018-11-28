#if 1
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
//#include <deque>
#include <map>
#include <set>
//#include <bitset>
#include <algorithm>
//#include <cctype>
//#include <cstring>
//#include <locale>
//#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<long long, long long> pii;
#define mp make_pair
#define X first 
#define Y second 
#define PROBLEM "river"

const long long inf = 1e9 + 100;
const LD eps = 1e-9;

const int MAX_N = 101;
const int MAX_K = 11;
const int MODUL = 100000000;



void solve()
{
	int test_cnt;
	cin >> test_cnt;

	for (int i = 0; i < test_cnt; ++i) {
		int smax;
		cin >> smax;

		string ss;
		cin >> ss;

		int tmp = 0;
		int ans = 0;
		for (int i = 0; i < ss.length(); ++i) {
			if (tmp < i) {
				ans += (i - tmp);
				tmp = i;
			}

			tmp += (ss[i] - '0');
		}

		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}


int main()
{

	freopen("A-large.in", "r", stdin); freopen("output23.txt", "w", stdout);
	//freopen("gcm.in", "r", stdin); freopen("gcm.out", "w", stdout);

	//freopen("input.txt", "r", stdin);
	// clock_t t1 = clock();

	//ios_base::sync_with_stdio(false);
	solve();
	// clock_t t2 = clock();

	// cerr << "time = " << LD(t2 - t1) / CLOCKS_PER_SEC << endl;

	return 0;
}
#endif