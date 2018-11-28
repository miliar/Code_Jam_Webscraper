#include<cstdio>
#include<set>
#include<vector>
#include<algorithm>
#include<string.h>
#include<map>
using namespace std;

#define MAX_V 5000
#define INF 100000

map<vector<int>,int> memo;
int n;


int go(vector<int> v) {
	if (v[0] < 4) return v[0];
	if(memo.count(v)) return memo[v];


	vector<int> v2;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > 1) v2.push_back(v[i]-1);
	}



	int best = go(v2) + 1;
	int cand = best;


	for (int i = 1; i<= v[0]/2; i++) {
		v2 = v;
		v2.push_back(i);
		v2[0] -= i;
		sort(v2.rbegin(), v2.rend());

		cand = go(v2) + 1;
		if (best > cand) best = cand;
	}
	



	return memo[v] = best;
}

int main() {
	int tests;
	scanf("%d",&tests);
	for(int test = 1; test <= tests; test++) {
		int t;
		vector<int> val;
		scanf("%d",&n);
		for(int i = 0;i < n; i++) {
			scanf("%d",&t);
			val.push_back(t);
		}
		sort(val.rbegin(), val.rend());
		printf("Case #%d: %d\n", test, go(val));
	}
	return 0;
}