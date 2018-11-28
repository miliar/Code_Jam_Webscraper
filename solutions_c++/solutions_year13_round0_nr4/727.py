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

string fileName = "D-small-attempt4";

int dp[1 << 22];
int n, k;
int cnt[40];

int need[20];
vector<int> keys[20];

vector<int> answer;

int solve(int mask) {
	if (mask == 0) return true;
	int& res = dp[mask];
	if (res != -1) return res;
	
	int have[40] = {0};
	for (int i = 0; i < 40; i++) have[i] = cnt[i];
	
	for (int i = 0; i < n; i++)
		if (!(mask & 1 << i)) {
			have[need[i]]--;
			for (int j = 0; j < keys[i].size(); j++)
				have[keys[i][j]]++;
		}
	
	for (int i = 0; i < n; i++)
		if (mask & 1 << i) {
			if (have[need[i]] && solve(mask ^ 1 << i)) {
				answer.pb(i + 1);
				return res = 1;
			}
		}
	return res = 0;
}

void solveSingle(int testNumber) {
	memset(cnt, 0, sizeof(cnt));
	cin >> k >> n;
	for (int i = 0; i < k; i++) {
		int x;
		cin >> x;
		cnt[x - 1]++;
	}
	
	for (int i = 0; i < n; i++) {
		cin >> need[i];
		need[i]--;
		int c;
		cin >> c;
		keys[i].clear();
		for (int j = 0; j < c; j++) {
			int x;
			cin >> x;
			keys[i].pb(x - 1);
		}
	}
	
	printf("Case #%d: ", testNumber);
	
	answer.clear();
	memset(dp, -1 ,sizeof(dp));
	
	if (!solve((1 << n) - 1)) cout << "IMPOSSIBLE\n";
	else  {
		for (int i = answer.size() - 1; i > 0; i--)
			cout << answer[i] << " ";
		cout << answer[0] << endl;
	}
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
		fflush(stdout);
		
	}
	return 0;
}
