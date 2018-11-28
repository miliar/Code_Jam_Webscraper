#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int getAllDigitNumber(int x ){
	int v[10] = {0};
	int d;
	int sw = true;
	int num ;
	int c = 0;
	while(sw){
		num = x;
		c ++;
		num = num * c;
		while(num > 0){
			d = num%10;
			v[d] = 1;
			num = num /10;
		}
		int c1 = 0;
		for(int i = 0 ; i < 10 ; i++){

			c1 = c1 + v[i];
		}
		if(c1 == 10){
			sw = false;
		}
		
	}
	return x*c;
}

int main(){
	
	freopen("a.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,x,i,y;
	scanf("%d",&n); 
	for (int i = 1; i <= n; ++i)
	{
		scanf("%d",&x); 

		if (x == 0){
			printf("Case #%d: INSOMNIA\n", i);
		}else {
			y = getAllDigitNumber(x);
			printf("Case #%d: %d\n", i,y);
		}
		
	}
	return 0; 
}