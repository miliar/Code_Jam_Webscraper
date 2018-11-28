#include <queue>
#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#define MAX 1024
#define PI pair<int, int>
using namespace std;

int B, N;
int times[MAX];

class mycomparison {
public:
  bool operator() (const PI& lhs, const PI&rhs) const {
  	return lhs < rhs;
  }
};

int gcd(int a, int b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}

int lcm(int a, int b) {
	return (a * b) / gcd(a, b);
}

int solve() {
	priority_queue<PI, vector<PI>, mycomparison> Q;

	for(int i = 0; i < B; i++) {
		Q.push(make_pair(times[i], i));
	}

	for(int i = 1; i < N; i++) {
		PI res = Q.top(); Q.pop();
		res.first += times[res.second];
		Q.push(res);
	}
	return Q.top().second + 1;
}

int solve2() {
	int L = 1;
	for(int i = 0; i < B; i++) {
		L = lcm(L, times[i]);
	}

	if(L > N) {
		return solve();
	}

	//printf("LCM = %d\n", L);
	vector<int> V;
	//V.push_back(-1);
	for(int i = 0; i < B; i++) {
		V.push_back(i + 1);
	}

	for(int i = 1; i < L; i++) {
		for(int j = 0; j < B; j++) {
			if(i % times[j] == 0) {
				V.push_back(j + 1);
			}
		}
	}

	// for(int i = 0; i < V.size(); i++) {
	// 	printf("%d ", V[i]);
	// }
	// puts("");
	//V[0] = V[V.size() - 1];
	return V[(N - 1) % (V.size())];
}

int main(int argc, char const *argv[]) {
	int cases;

	scanf("%d", &cases);
	for(int i = 1; i <= cases; i++) {
		scanf("%d %d", &B, &N);
		for(int i = 0; i < B; i++) {
			scanf("%d", &times[i]);
		}
		printf("Case #%d: %d\n", i, solve2());

	}
	return 0;
}