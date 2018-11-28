#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <utility>
#include <algorithm>
#include <cmath>
using namespace std;

int const MAX_N = 200100;
int const MAX_CH = 100100;
int const INT_INF = 1000000000;

char st[MAX_CH];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	gets(st);
	sscanf(st,"%d",&t);
	int ind = 0;
	while (t-->0) {
		ind++;
		printf("Case #%d:",ind);
	
		gets(st);
		int K,C,S;
		sscanf(st,"%d%d%d",&K,&C,&S);

		if (S >= K) {
			for (int i=1; i<=K; i++) printf(" %d",i);
			printf("\n");
		}
		else {
			printf(" IMPOSSIBLE\n");
		}
	}
	return 0;
}