#include "stdafx.h"
#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt,s=0,n,cnt;
	char si[1000];
	scanf("%d",&tt);
	for (int qq=1;qq<=tt;qq++) {
		scanf("%d %s",&s,&si);
		if(s==0)
			n=0;
		else{
			cnt=0;
			if((si[0]-'0')==0)
				n=1;
			else
				n=0;
			for(int i=0;i<=s;i++){
				
				if(i>(n+cnt))
					n++;
				cnt+=(si[i]-'0');
			}
		}
		printf("Case #%d: %d\n",qq,n);
	}
	return 0;
}