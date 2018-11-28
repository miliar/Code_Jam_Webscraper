#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1);

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

void solve(int nowCase) {
	int n, c;
	cin >> n >> c;
	vector<int> s(n);
	REP(i, n) scanf("%d", &s[i]);
	SORT(s);
	// REP(i, n) cout << s[i] << endl;
	int answer = -1;
	for (int single = 0; single <= n; ++single) {
		int last = n - single;
		bool isValid = true;
		for (int i = 0; i < last - 1 - i; ++i) {
			if (s[i] + s[last - 1 - i] > c) {
				//cout << "i = " << i << "last - 1 - i = " << last - 1 - i << endl;
			//	cout << s[i] + s[last - 1 - i] << endl;
				isValid = false;
				break;
			}
		}

		if (isValid) {
			answer = single + (n - single + 1) / 2;
			break;
		}
	}

	cout << "Case #" << nowCase << ": " << answer << endl;
}

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
		solve(nowCase);
	}
	return 0;
}