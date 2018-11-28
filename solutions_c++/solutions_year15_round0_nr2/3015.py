#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;

int z,q,n,i,res, tab[2005];

bool ok(int x, int cut) {
	int res = 0;
	for (int i=0;i<n;i++) {
		res += tab[i] / x;
		if (tab[i] % x) res++;
		res--;
	}
	return (res <= cut);
}

int find(int a, int b, int cut) {
	int index;
	while (a < b) {
		index = (a + b) / 2;
		if (ok(index, cut)) {
			b = index;
		} else {
			a = index + 1;
		}
	}
	return b;
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
	scanf("%d",&n);
	for (i=0;i<n;i++) {
		scanf("%d",&tab[i]);
	}
	sort(tab, tab + n);
	res = tab[n - 1];
	i = 1;
	for (i = 1;i < res;i++) {
		res = min(res, i + find(1, tab[n-1], i));
	}
	printf("Case #%d: %d\n", q, res);
}
return 0;
}

