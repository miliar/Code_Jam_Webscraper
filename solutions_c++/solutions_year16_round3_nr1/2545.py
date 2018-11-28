#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using std::scanf;
using std::printf;
using std::vector;

struct party {
	short count;
	char name;

	bool operator<(const party& b) const {
		return count < b.count;
	}
};

template <typename V>
static bool valid(int sum, const V& P) {
	return P.empty() || P.back().count * 2 <= sum;
}

template <typename V>
static void dec0(int& sum, V& P, int j) {
	auto m = P.begin() + j;
	m->count--;
	sum--;
	if(m->count == 0) {
		P.erase(m);
	} else {
		for(int i = j; i > 0 && P[i] < P[i - 1]; --i)
			std::swap(P[i], P[i - 1]);
	}
}

template <typename V>
static void dec0(int& sum, V& P, int j, int k) {
	auto m = P.begin() + j;
	m->count--;
	sum--;
	auto n = P.begin() + k;
	n->count--;
	sum--;
	if(n->count)
		for(int i = k; i > 0 && P[i] < P[i - 1]; --i)
			std::swap(P[i], P[i - 1]);
	else {
		P.erase(n);
		--j;
		--m;
	}
	if(m->count)
		for(int i = j; i > 0 && P[i] < P[i - 1]; --i)
			std::swap(P[i], P[i - 1]);
	else
		P.erase(m);
}

template <typename V>
static void dec(int& sum, V& P, int j) {
	printf(" %c", P[j].name);
	dec0(sum, P, j);
}

template <typename V>
static void dec(int& sum, V& P, int j, int k) {
	printf(" %c%c", P[j].name, P[k].name);
	dec0(sum, P, j, k);
}

template <typename V>
static void testcase(int t, int N, int sum, V& P) {
	std::sort(P.begin(), P.end());
	printf("Case #%d:", t);
	while(!P.empty()) {
		if(P.back().count == 1) {
			if((P.size() % 2) == 1) {
				dec(sum, P, P.size() - 1);
			} else {
				dec(sum, P, P.size() - 1, P.size() - 2);
			}
		} else if(P.size() >= 2 && P[P.size() - 2] < P[P.size() - 1]) {
			dec(sum, P, P.size() - 1);
		} else if(P.size() >= 3 && P[P.size() - 2].count == P[P.size() - 1].count && P[P.size() - 3].count > 1) {
			dec(sum, P, P.size() - 3);
		} else {
			dec(sum, P, P.size() - 1, P.size() - 2);
		}
		assert(valid(sum, P));
	}
	putchar('\n');
}

static void testcase(int t) {
	int N;
	scanf("%i", &N);
	vector<party> P(N);
	int sum = 0;
	for(int i = 0; i < N; ++i) {
		int c;
		scanf("%i", &c);
		P[i].count = c;
		P[i].name = 'A' + i;
		sum += c;
	}
	testcase(t, N, sum, P);
}

int main() {
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
