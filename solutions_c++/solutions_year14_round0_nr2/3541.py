#include<iostream>
#include<limits.h>
#include<cstdio>
using namespace std;
int main()
{
	int t,i;
		freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for( i=1;i<=t;i++ ){
		double c,f,x,a,b,time,check,sum;
		cin>>c>>f>>x;
		time = 2;
		sum = x/time;
		check = 0;
		while(1){
			check+= c/time;
			time=time+f;
			a= x/time;
			if(sum>check+a)
			sum = check+a;
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",i,sum);
	}
	return 0;
}
