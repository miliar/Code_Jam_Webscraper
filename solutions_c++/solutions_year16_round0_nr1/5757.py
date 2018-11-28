#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

long long countSheeps(int N) {
	int sol = (1 << 10) - 1;
	int visited = 0;
	long long curName = 0;
	set<long long> visitedNumbers;
	while (visited != sol) {
		curName += N;
		if (visitedNumbers.find(curName) != visitedNumbers.end()) {
			return -1;
		}
		visitedNumbers.insert(curName);
		long long temp = curName;
		while (temp) {
			visited |= 1 << (temp % 10);
			temp /= 10;
		}
	}
	return curName;
}

int main() {

#ifndef ONLINE_JUDGE
		freopen("input.in", "rt", stdin);
		freopen("output.out", "wt", stdout);
#endif
	int N, T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d", &N);
		long long sol = countSheeps(N);
		printf("Case #%d: ", t + 1);
		(sol == -1) ? printf("INSOMNIA\n") : cout<<sol<<endl;
	}
	return 0;
}
