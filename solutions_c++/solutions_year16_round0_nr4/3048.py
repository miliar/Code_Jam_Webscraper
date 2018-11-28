#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 100000 + 7;
const int INF = 1000000000;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int s,c,k;

	cin >> t;
	for (int testNumber = 1; testNumber <= t; testNumber++) {
		cin >> k >> c >> s;
		cout << "Case #" << testNumber << ":";
		ll pw = 0;
		for (int i=1;i<=c;i++) {
			pw *= k;
			pw ++;
		}
		for (int i=1;i<=s;i++) {
			cout << " " << 1 + (i-1)*pw;
		}
		cout << endl;
	}
	return 0;
}