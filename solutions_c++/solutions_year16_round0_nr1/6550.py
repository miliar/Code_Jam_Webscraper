#include<iostream>
#include<bits/stdc++.h>
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)
#define ss(n) scanf("%s",s)
#define f(n) for(int i=0;i<n;i++)
//Counting Sheep-GCJ < A-small-attempt0.in > A-small-output0.txt
using namespace std;
int main(){
	int test; sd(test);
	for(int t=1;t<=test;t++){
		long long int n; sld(n);
		printf("Case #%d: ",t);
		int a[10]={0},c=10,i=1;
		long long int num=n,s;
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		while(c!=0){
			num=i*n;
			s=num;
			i++;
			while(num>0){
				int d=num%10;
				if(!a[d-1]){
					c--;
					a[d-1]=1;
				}
				num/=10;
			}
		}
		printf("%lld\n",s);
	}
	return 0;
}
