#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------

#ifdef cin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif


double dp[400][200][200];
int vis[200][200][200];
double a[600];
int n, k;
int m;
double f(int i, int yes, int no){
	if (i == m){
		if (yes == no) return 1;
		return 0;
	}
	if (vis[i][yes][no]) return dp[i][yes][no];
	double ans = 0;
	double r1 = f(i + 1, yes + 1, no) * a[i];
	double r2 = f(i + 1, yes, no + 1) * (1 - a[i]);
	ans = r1 + r2;
	return dp[i][yes][no] = ans;
}
int main(){
	ios::sync_with_stdio(0);

	int t, z = 1;
	cin >> t;
	while (t--){
		cout << "Case #" << z++ << ": ";

		cin >> n >> k;

		for (int i = 0; i < n; i++) cin >> a[i];
		sort(a, a + n);
		for (int i = n; i < 2 * n; i++) a[i] = a[i - n];

		double ans = 0;
		for (int i = 0; i < n; i++){
			memset(vis, 0, sizeof(vis));
			m = i + k;
			ans = max(ans, f(i, 0, 0));
		}
		cout.precision(16);

		cout << fixed << ans << endl;

	}


#undef cin
	int ______________;
	cin >> ______________;
	return 0;
}