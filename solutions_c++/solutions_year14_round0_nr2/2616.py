#include <bits/stdc++.h>
using namespace std;
int main()
{
	int test,it;
	scanf("%d",&test);
	for( it = 1; it <= test; it++ ){
		double c,f,x,a,b,r,prev,min = 999999999;
		scanf("%lf %lf %lf",&c,&f,&x);
		r = 2;
		min = x/r;
		prev = 0;
		while(1){
			prev+= c/r;
			r=r+f;
			a= x/r;
			if(min>prev+a)
			min = prev+a;
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",it,min);
	}
	return 0;
}
