#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
#include <string>
using namespace std;
typedef long long ll;
ll pos[200];
void solve(int t) {
	int k,c,s;
	scanf("%d%d%d",&k,&c,&s);
	for (int i=1;i<=s;i++) {
		pos[i]=i;
	}
	for (int t=2;t<=c;t++) {
		for (int i=1;i<=s;i++)
			pos[i]=1ll*(pos[i]-1)*k+i;
	}
	printf("Case #%d:", t);
	for (int i=1;i<=s;i++)
		printf(" %lld", pos[i]);
	printf("\n");
}

int main() {
	int tst;
	scanf("%d",&tst);
	for (int t=1;t<=tst;t++) {
		solve(t);
	}
	return 0;
}