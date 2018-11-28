#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 10100 
int vol[maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cas;
	int n,tot;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		cin>>n>>tot;
		for(int i=1;i<=n;i++){
			scanf("%d",&vol[i]);
		}
		sort(vol+1,vol+n+1);
		int st=1,ed=n,need=0;
		while(ed>st){
			if(vol[ed]+vol[st]<=tot){
				st++;
				need++;
			}else need++;
			ed--;
		}
		if(ed==st)need++;
		
		printf("Case #%d: %d\n",cas,need);
	}
	return 0;
}
 
