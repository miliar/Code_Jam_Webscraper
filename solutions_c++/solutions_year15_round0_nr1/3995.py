#include <cstdio>
#include <algorithm>
#include <iostream>

#define rep(k,a) for(int k = 0; k < (a); k++)

using namespace std;
int shy[10000];

int main()
{
	int T;
	scanf("%d", &T);
	rep(i, T){
		int max;
		int have = 0;
		int need = 0;
		scanf("%d",&max);
		getchar();
		rep(j, max+1){
			int ia = getchar() - '0';
			shy[j]=ia;
		}
		rep(j, max+1){
			if(have >= j)
				have+=shy[j];
			if(have < j && shy[j]>0){
//				printf("fak, i have %d have and there are %d-shy people(%d)\n", have, j, shy[j]);
				need += j-have;
				have += j-have;
				have += shy[j];
			}
		}
		printf("Case #%d: %d\n",i+1, need);
	}
	return 0;
}

