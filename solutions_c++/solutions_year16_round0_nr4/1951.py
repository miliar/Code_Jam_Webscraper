#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,K,C,S;

int main() {
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:",kase);
		for (int i = 1;i <= K; i++)
			printf(" %d",i);
		printf("\n");
	}
	return 0;
}