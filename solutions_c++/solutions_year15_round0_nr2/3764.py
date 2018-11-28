#include <iostream>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <string.h>
using namespace std;
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define set(a,b) memset(a,b,sizeof(a))
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++) {
		int d;
		cin >> d;
		int arr[1001];
		int x;
		for (int i = 0; i < d; i++) {
			cin >> arr[i];
		}
		int res = 1001;
		for (int i = 1; i <= 1000; i++) {
			int t = 0;
			for (int j = 0; j < d; j++) {
				t += ceil(arr[j] / (double)i) - 1;
			}
			res = min(res, t + i);
		}
		cout << "Case #" << c << ": " << res << endl;
	}
	return 0;
}