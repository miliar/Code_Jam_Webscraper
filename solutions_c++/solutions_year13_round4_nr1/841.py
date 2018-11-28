#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const LL BASE = (LL)1000000000 * (LL)1000000000;
const LL INF = BASE;
const int MAXM = 1024;

struct Bignum {
	LL h, l;
	void set(LL x ) { h = 0; l = x; }
	void add(LL x ) {
		l += x;
		if (l >= BASE) { ++h; l -= BASE; }
	}
	void add(const Bignum & b ) {
		h += b.h;
		l += b.l;
		if (l >= BASE) { ++h; l -= BASE; }
	}
	void sub(const Bignum & b ) {
		h -= b.h;
		l -= b.l;
		if (l < 0) { --h; l += BASE; }
	}
	void mul(LL x ) {
		h *= x;
		l *= x;
		h += l / BASE;
		l %= BASE;
	}
	void print() {
		if (h > 0) cout << h;
		cout << l;
	}
};


Bignum originCost, newCost;
int src[MAXM], tar[MAXM], pers[MAXM];
int lst[MAXM<<1], tot;
LL persons[MAXM<<1];
int cases, cas, N, M;

void init() {
	originCost.set(0);
	tot = 0;
	scanf("%d%d",&N,&M);
	for (int i = 0; i < M; i++ ) {
		int a, b, c;
		scanf("%d%d%d",&a,&b,&c);
		Bignum tmp;
		tmp.set((LL)(N + N-(b-a-1))*(b-a)/2);
		tmp.mul(c);
		originCost.add(tmp);
		src[i] = a;
		tar[i] = b;
		pers[i] = c;
		lst[tot++] = a;
		lst[tot++] = b;
	}
}

int getindex(int x ) {
	int l = 0, r = tot - 1;
	while (l <= r) {
		int mid = (l + r) >> 1;
		if (lst[mid] <= x) l = mid + 1;
		else r = mid - 1;
	}
	return l - 1;
}

void resort() {
	memset(persons, 0, sizeof(persons));
	sort(lst, lst+tot);
	tot = unique(lst, lst + tot) - lst;
	for (int i = 0; i < M; i++ ) {
		int pa = getindex(src[i]), pb = getindex(tar[i]);
		for (int j = pa; j < pb; j++ )
			persons[j] += pers[i];
	}
}

int getMinPersonsIndex() {
	int index = -1;
	LL minpersons = INF;
	for (int i = 0; i < tot - 1; i++ )
		if (persons[i] > 0 && persons[i] < minpersons) {
			minpersons = persons[i];
			index = i;
		}
	return index;
}

void work() {
	newCost.set(0);
	while (true) {
		int index = getMinPersonsIndex();
		if (index == -1) break;
		int pa = index, pb = index;
		while (pa - 1 >= 0 && persons[pa-1] > 0) --pa;
		while (pb + 1 <= tot-2 && persons[pb+1] > 0) ++pb;
		LL minpersons = persons[index];
		int a = lst[pa], b = lst[pb+1];
		Bignum tmp;
		tmp.set((LL)(N + N-(b-a-1))*(b-a)/2);
		tmp.mul(minpersons);
		newCost.add(tmp);
		for (int i = pa; i <= pb; i++ )
			persons[i] -= minpersons;
	}
	originCost.sub(newCost);
	printf("Case #%d: ",cas);
	originCost.print();
	printf("\n");
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	for (scanf("%d",&cases), cas = 1; cas <= cases; ++cas ) {
		init();
		resort();
		work();
	}
	return 0;
}
