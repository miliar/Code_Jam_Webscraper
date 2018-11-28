#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

int t;
int n, j;
vector <int> res;
vector <vector <ll> > got;

ll Get(ll x, ll bas)
{
	ll cur = 1;
	ll res = 0ll;
	for (int i = 0; i < 16; i++) {
		if (x & 1 << i) res += cur;
		cur *= bas;
	}
	return res;
}

ll Solve(ll x)
{
	for (ll i = 2; i * i <= x; i++)
		if (x % i == 0) return i;
	return -1;
}

void Print(ll x)
{
	if (!x) return;
	Print(x / 2);
	if (x & 1) printf("1");
	else printf("0");
}

int main()
{
	scanf("%d", &t);
	scanf("%d %d", &n, &j);
	for (int i = (1 << 15) + 1; i < (1 << 16) && res.size() < j; i += 2) {
		vector <ll> V;
		int k = 2;
		for (; k <= 10; k++) {
			ll x = Get(i, k);
			ll dv = Solve(x);
			if (dv != -1) V.push_back(dv);
			else break;
		}
		if (k > 10) {
			res.push_back(i);
			got.push_back(V);
		}
	}
	printf("Case #1:\n");
	for (int i = 0; i < j; i++) {
		Print(res[i]);
		for (int k = 0; k < got[i].size(); k++)
			printf(" %I64d", got[i][k]);
		printf("\n");
	}
	return 0;
}