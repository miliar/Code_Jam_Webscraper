#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
const int oo=1073741819;
using namespace std;
int n,t;
int p[5000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int Case=1;t;t--,Case++) {
		printf("Case #%d: ",Case);
		scanf("%d",&n);
		int Max=-oo;
		for (int i=1;i<=n;i++) {
			scanf("%d",&p[i]);
			Max=max(Max,p[i]);
		}
		int ans=oo;
		for (int i=1;i<=Max;i++) {
			int sum=0;
			for (int j=1;j<=n;j++)
				sum+=(p[j]-1)/i;
			ans=min(ans,sum+i);
		}
		printf("%d\n",ans);
	}
	return 0;
} 
