#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main(void){
	int t;
	int hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		int n,x;
		scanf("%d %d",&n,&x);
		int i;
		int s[10005];
		for(i=0;i<n;i++)
		  scanf("%d",&s[i]);
		sort(s,s+n);
		int st=0,ed=n-1;
		int ans=0;
		while(st<=ed){
			if(s[st]+s[ed]<=x){
				st++;
				ed--;
				ans++;
			}
			else{
				ans++;
				ed--;
			}
		}
		printf("Case #%d: %d\n",hh,ans);
	}
	return 0;
} 
