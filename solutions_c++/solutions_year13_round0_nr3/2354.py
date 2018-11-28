#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

//string fileName = "B-small-attempt0";
string fileName = "C-large-1";

bool ispal(string s) {
	for (int i = 0; i < s.size(); i++)
		if (s[i] != s[s.size() - i - 1]) return false;
	return true;
}

	vector<long long> p;

void pre() {
	int pow10[10];
	pow10[0] = 1;
	for (int i = 1; i < 10; i++)
		pow10[i] = pow10[i - 1] * 10;

	for (int d = 1; d <= 7; d++) {
		int first = (d + 1) / 2;
		int second = d / 2;

		for (int i = pow10[first - 1]; i < pow10[first]; i++) {
			string s = tostring(i);
			string t = s.substr(0, second);
			reverse(t.begin(), t.end());

			long long num = toint(s + t);
			if (ispal(tostring(num * num)))
				p.pb(num * num);
		}
	}
}

void solveSingle(int testNumber) {
	long long a, b;
	cin >> a >> b;
	int cnt = 0;
	for (int i = 0; i < p.size(); i++)
		if (a <= p[i] && p[i] <= b) cnt++;
	printf("Case #%d: %d\n", testNumber, cnt);
}

int main() {

	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);

	pre();

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
		fflush(stdout);
	}
	return 0;
}
