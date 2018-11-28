//============================================================================
// Name        : gcj0d.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define maxn 1005
double n[maxn],k[maxn];
bool cmpup(double x,double y){
	return x<y;
}
bool cmpdown(double x,double y){
	return x>y;
}
int main() {
	int cas,cnt,num,i,key,sum,ng,dg;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&cas);
	cnt=0;
	while(cas--){
		memset(n,0,sizeof(n));
		memset(k,0,sizeof(k));
		scanf("%d",&num);
		for(i=0;i<num;i++)
			scanf("%lf",&n[i]);
		for(i=0;i<num;i++)
			scanf("%lf",&k[i]);
		sort(k,k+num,cmpup);
		sort(n,n+num,cmpup);
		key=0;
		sum=0;
		for(i=0;i<num;i++){
			if(k[i]<n[key])
				continue;
			else{
				sum+=1;
				key+=1;
			}
		}
		ng=num-sum;

		key=0;
		sum=0;

		for(i=0;i<num;i++){
			if(n[i]<k[key])
				continue;
			else{
				sum+=1;
				key+=1;
			}
		}
		dg=sum;
		printf("Case #%d: %d %d\n",++cnt,dg,ng);


	}
	return 0;

}
