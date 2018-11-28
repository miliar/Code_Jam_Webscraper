#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

const int MAXN = 11000;

int T, N, X, S[MAXN];

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d%d", &N, &X);
		REP(i,N) scanf("%d", S+i);
		int ans = 0;

		vector<int> usedVec;
		REP(i,N) {
			if (S[i] > X / 2) {
				usedVec.push_back(S[i]);
				swap(S[i], S[N-1]);
				--N;
				--i;
			}
		}

		sort(S, S+N, greater<int>());

		multiset<int, greater<int>> used(usedVec.begin(), usedVec.end());

		REP(i,N) {
			bool merged = false;
			auto it = used.begin();
			while (it != used.end()) {
				if (S[i] + *it <= X) {
					used.erase(it);
					++ans;
					merged = true;
					break;
				}
				++it;
			}

			if (!merged) {
				used.insert(S[i]);
			}
		}

		ans += used.size();

		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
