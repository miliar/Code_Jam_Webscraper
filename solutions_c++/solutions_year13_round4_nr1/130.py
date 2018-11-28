#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int z_codejam_testcase;
#define SIZE(A) ((int)(A).size())
#define PB push_back
#define MP make_pair
#define gout printf("Case #%d: ", ++z_codejam_testcase), cout

const long long mod = 1000002013LL;

int N, m;
int o[2000], e[2000], w[2000];

long long getval(long long x) {
 	return (1LL*x*(x+1)/2)%mod;
}

map <int, long long> d;
set <int> was;
pair <int, int> q[2000];


void main2() {
	scanf("%d%d", &N, &m);
	int t = 0;
	for (int i = 0; i < m; i++) {
	 	scanf("%d%d%d", o+i, e+i, w+i);
	 	q[t++] = MP((o[i]<<1)+0, i);
	 	q[t++] = MP((e[i]<<1)+1, i);
	}
	sort(q, q+t);

	long long toadd = 0;
	was.clear(); d.clear();

	for (int i = 0; i < t; i++) {
	 	int curt = q[i].first>>1, j = q[i].second;
	 	if (was.find(j)==was.end()) {
	 	 	was.insert(j);
	 	 	d[-curt] += w[j];
	 	 	continue;
	 	}
	 	was.erase(was.find(j));
	 	long long x = w[j];
	 	while (x) {
	 	 	int val = d.begin()->first, y = min(d.begin()->second, x);
	 	 	x -= y; d[val] -= y;
	 	 	if (!d[val]) d.erase(d.find(val));
	 	 	toadd = (toadd + 1LL*getval(N-e[j]-val)*y)%mod;
	 	}
	}
	for (int i = 0; i < m; i++) {
	 	toadd = (toadd - 1LL*getval(N-e[i]+o[i])*w[i])%mod;
	}
	gout << (toadd+mod)%mod << endl;
}




int main() {
	int test_num;
	scanf("%d", &test_num);
	for (; test_num--;) {
	 	main2();
	}


	return 0;
}
