#include<iostream>
#include<cstdio>
#include <math.h>
using namespace std;

int main(){
	
	long long int test_cases,r,c,w;
	scanf("%lld",&test_cases);
	for(long long int t=0;t<test_cases;t++){
	
		scanf("%lld %lld %lld",&r,&c,&w);
		printf("Case #%lld: %lld\n",t+1,(r*((long long int)ceil(((double)c/(double)w))))+(w-1));
	}
	return 0;
}
