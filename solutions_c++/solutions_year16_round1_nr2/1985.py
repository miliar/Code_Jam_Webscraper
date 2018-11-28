#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

struct dsu
{
	vector <int> S, P;	
	void root(int &x);
	void join(int a, int b);
	int find(int a, int b);
	dsu(int N);
};

int main()
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		int N;
		scanf("%d", &N);
		dsu comp(N), incomp(N);
	}
}

dsu::dsu(int N)
{
	S.resize(N + 1);
	P.resize(N + 1);
	for (int i = 1; i <= N; ++i)
		S[i] = 1, P[i] = i;	
}

void dsu::root(int &x)
{
	while(x != P[x])
		x = P[x];
}

void dsu::join(int a, int b)
{
	root(a); root(b);
	assert(a != b);
	if (S[a] >= S[b]) {
		S[a] += S[b];
		P[b] = a;
	} else {
		S[b] += S[a];
		P[a] = b;
	}
}

int dsu::find(int a, int b)
{
	root(a); root(b);
	return (a == b);
}
