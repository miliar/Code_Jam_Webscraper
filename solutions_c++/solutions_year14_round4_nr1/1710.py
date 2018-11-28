/*
#include "template.h"
#include "point.h"
#include "math.h"
#include "line.h"
#include "edge.h"
#include "graph.h"
#include "distance.h"
#include "dsu.h"
#include "mst.h"
#include "convex hull.h"
*/
#ifndef TEMPLATE_H
#define TEMPLATE_H
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll,ll> pii;
typedef pair<ld,ll> pdi;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<ld> vd;
typedef vector<vd> vvd;

#define mp make_pair
#define pb push_back
#define det(a, b, c, d) a * d - b * c

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int inf = 1234567890;
#endif

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int n, x;
		scanf("%d%d", &n, &x);
		multiset<int> S;
		for (int j = 0; j < n; ++j)
		{
			int f;
			scanf("%d", &f);
			S.insert(-f);
		}
		int answer = 0;
		while(S.size())
		{
			answer++;
			int now = *S.begin();
			now *= -1;
			S.erase(S.begin());
			int diff = x - now;
			diff *= -1;
			auto it = S.lower_bound(diff);
			if(it != S.end())
			{
				S.erase(it);
			}
		}
		printf("Case #%d: %d\n", i + 1, answer);
	}
	return 0;
}