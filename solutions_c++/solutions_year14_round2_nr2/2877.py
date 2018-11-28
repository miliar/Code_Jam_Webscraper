#include <iostream>
#include <cstdio>
using namespace std;

int T;
int a,b,k;

int main(){

	scanf("%d",&T);
	for(int i=0;i<T;i++){

		scanf("%d %d %d",&a,&b,&k);

		long sum = 0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				//printf("(%d,%d) %d %d\n", i,j, k,(int) (i&j));

				if((i&j) < k) sum++;
			}
		}

		printf("Case #%d: %ld\n",i+1,sum);

	}

	return 0;
}
