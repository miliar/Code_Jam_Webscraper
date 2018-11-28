#include <stdio.h>
#include<iostream>
using namespace std;
int main()
{
	
	
	int i,j,k,l,t,a,b;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	
	
	long long int ans;
	for(i=1;i<=t;i++)
	{
		scanf("%d%d%d",&a,&b,&k);
		ans = 0;
		for(j=0;j<a;j++){
			for(l=0;l<b;l++){
				if((j&l) < k ){
				ans++;
				}
			}
		}
		printf("Case #%d: %lld\n",i,ans);
	}
	//fclose(we);
	return 0;
}
