#include <stdio.h>
#include <cassert>
#include <iostream>

using namespace std;

#define JUDGE 1
#define MAXSIZE 10000005

int index;
long long fair[100];

bool check(long long n){
	long long temp=n,rev=0;
	while(temp){
		rev=rev*10+temp%10;
		temp/=10;
	}
	return rev == n;
}

void initialise(){
	index=0;
	for(long long i=1;i<=MAXSIZE;i++)
		if(check(i))
			if(check(i*i))
				fair[index++]=i*i;
}

int main(){
	
	if(JUDGE){
		freopen("input","r",stdin);
		freopen("output","w",stdout);
	}
	
	initialise();
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		long long a,b;
		int count=0;
		scanf("%lld %lld",&a,&b);
		for(int i=0;i<index;i++)
			if(fair[i]>=a && fair[i] <= b)
				count++;
		printf("Case #%d: %d\n",tt,count);
	}
	return 0;	

}