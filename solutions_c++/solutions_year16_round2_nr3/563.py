#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int N, cnt_a, cnt_b;
map<string, int> mapping_a, mapping_b;
int pd[16][1 << 16];
vector<pair<int,int> > pairs;
int used_a[20], used_b[20];

int extra;

void read(){
	scanf("%d", &N);

	mapping_a.clear();
	mapping_b.clear();

	pairs.clear();

	cnt_a = cnt_b = 0;

	extra = 0;

	for (int i = 0; i < N; i++) {
		char A[30], B[30];
		scanf("%s%s", A, B);

		if (mapping_a.find(A) == mapping_a.end()) {
			mapping_a[A] = cnt_a++;
		}
		if (mapping_b.find(B) == mapping_b.end()) {
			mapping_b[B] = cnt_b++;
		}

		pairs.push_back(pair<int,int>(mapping_a[A], mapping_b[B]));
	}
}

int go(int pos, int mask) {
	if (pos == N) {
		return 0;
	}
	if (pd[pos][mask] != -1)
		return pd[pos][mask];

	int best = 0;

	for (int i = 0; i < N; i++) {
		if ((mask&(1 << i)) == 0) {
			int t;
			if (used_a[pairs[i].first] > 0 && used_b[pairs[i].second] > 0) {
				used_a[pairs[i].first]++;
				used_b[pairs[i].second]++;
				t = 1 + go(pos + 1, mask | (1 << i));
				used_a[pairs[i].first]--;
				used_b[pairs[i].second]--;
			} else {
				used_a[pairs[i].first]++;
				used_b[pairs[i].second]++;
				t = go(pos + 1, mask | (1 << i));
				used_a[pairs[i].first]--;
				used_b[pairs[i].second]--;
			}
			if (best < t) {
				best = t;
			}
		}
	}
	pd[pos][mask] = best;
	return best;
}

void process() {
	memset(pd, -1, sizeof(pd));
	memset(used_a, 0, sizeof(used_a));
	memset(used_b, 0, sizeof(used_b));
	printf("%d\n", go(0, 0));
}

int main() {
	
	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}

	return 0;
}