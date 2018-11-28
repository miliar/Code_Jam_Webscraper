#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;



int main(){

	freopen("C-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);

	int test,c=1;
	scanf("%d",&test);

	while(test--){
		int A,B,count=0;
		scanf("%d %d",&A,&B);
		int a[33]={ 0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0 } ;
		for(int i=sqrtf(A) ; i<=sqrtf(B) ; i++){

			if(i*i>=A && i*i <=B && a[i]){
			count++;
			a[i]=0;
			}
		}
		printf("Case #%d: %d\n",c++,count);

	}
	return 0;


}
