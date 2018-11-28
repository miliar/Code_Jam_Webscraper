#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<int> Vint;
typedef vector<LL> VLL;

void printV(Vint& v)
{
	for (int i=0;i<v.size();i++) {
		printf("%d\n", v[i]);
	}
}

void solve()
{
	int N;
	Vint P;
	int sum=0;
	int max1=-1;
	int max2=-1;
	int v1=-1;
	int v2=-1;

	scanf("%d", &N);
	P.resize(N);
	for (int i=0;i<N;i++) {
		scanf("%d", &P[i]);
		sum+=P[i];

		if (P[i]>max1) {
			if (max1>max2) {
				max2=max1;
				v2=v1;
			}
			max1=P[i];
			v1=i;
		} else if (P[i]>max2) {
			max2=P[i];
			v2=i;
		}
	}

//	printf("SUM=%d, max1=%d, max2=%d\n", sum, v1,v2);


	while (sum>P[v2]*2) {
		while(P[v1]>P[v2]) {
			if (P[v1]-P[v2]==1) {
				printf(" %c", 'A'+v1);
				P[v1]--;
				sum--;
			} else {
				printf(" %c%c", 'A'+v1, 'A'+v1);
				P[v1]-=2;
				sum-=2;
			}
		}

		printf(" ");
		for (int i=0;i<N;i++) {
			if (i!=v1 && i!=v2 && P[i]>0) {
				printf("%c", 'A'+i);
				P[i]--;
				sum--;
				break;
			}
		}

		if (sum>P[v2]*2) {
			for (int i=0;i<N;i++) {
				if (i!=v1 && i!=v2 && P[i]>0) {
					printf("%c", 'A'+i);
					P[i]--;
					sum--;
					break;
				}
			}
		}
	}

	for (int i=0;i<P[v2];i++) {
		printf(" %c%c", 'A'+v1, 'A'+v2);
	}
	printf("\n");
}

int main() 
{
	int T=0;
	scanf("%d", &T);
	for (int i=1;i<=T;i++) {
		printf("Case #%d:", i);
		solve();
	}
	
	return 0;
}
