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

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("A.txt", "wt", stdout);
#endif
	int T, S;
	char shy[1011];
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d %s", &S, shy);
		int cnt = 0;
		int stp = 0;
		for (int i = 0; i <= S; ++i) {
			if (cnt < i)
				cnt++,stp++;
			cnt+= (shy[i]-'0');
		}
		printf("Case #%d: %d\n", t + 1, stp);
	}
	return 0;
}
