#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<utility>
#include<iostream>
#include<sstream>
#include<fstream>

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);
const int maxn = 600000;
const long long mod = 1000002013;

int ntest;
long long answer;
long long total;
int n, m, o, e, p;

map<int, int> T;
map<int, int> E, O;
set<int> id;

int main() {
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++) {

		O.clear(); E.clear(); T.clear(); id.clear();

		total = 0;

		scanf("%d%d", &n, &m);
		for(int i=0; i<m; i++) {
			scanf("%d%d%d", &o, &e, &p);

			id.insert(o);
			id.insert(e);
			O[o] += p;
			E[e] += p;

			long long dis = e - o;
			total += (dis * n - dis * (dis+1) / 2) % mod * p % mod;
			total %= mod;
		}
		
		answer = 0;
		for(set<int>::iterator it = id.begin(); it != id.end(); it++) {
			int x = *it;

			if(O[x] > 0) T[x] += O[x];
			int amount = E[x];

			while(amount > 0) {
				pair<int,int> u = *T.rbegin();
				int t = min(amount, u.second);
				long long dis = x - u.first;
				answer += ((dis * n - dis * (dis+1) / 2) % mod * t) % mod;
				answer %= mod;

				if(u.second != t) {
					T[u.first] = u.second - t;
				} else {
					T.erase(u.first);
				}

				amount -= t;
			}
		}

		printf("Case #%d: %d\n", test, (total % mod - answer % mod + mod) % mod);
	}
	return 0;
}
