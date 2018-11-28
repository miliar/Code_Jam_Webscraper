#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main() {
	int t,n,i,k,x;
	long long ans,temp,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n); 
	 if(n)
	 {
		int a[10]={0}; j=1;
		while(1)
		{
			ans=(j++)*n; temp=ans; x=1;
			while(temp)
			{
				a[temp%10]=1;
				temp=temp/10;
			}
			for(k=0;k<10;k++) if(!a[k]) {x=0;break;}
			if(x) break;
		}
	printf("Case #%d: %lld\n",i,ans);	
	 }
	 else printf("Case #%d: INSOMNIA\n",i);	
	}
	return 0;
}
