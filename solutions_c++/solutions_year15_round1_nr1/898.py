#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

int d[10005];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("alargeout.txt","w",stdout);
	int T,cas=1;
	int n;
	for(scanf("%d",&T);cas<=T;){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",d+i);
		}
		int ans1=0,maxd=0;
		for(int i=1;i<n;i++){
			if(d[i-1]-d[i]>0){
				ans1+=d[i-1]-d[i];
				maxd=max(maxd,d[i-1]-d[i]);
			}
		}
		long long ans2=0;
		for(int i=0;i<n-1;i++)
			ans2+=min(maxd,d[i]);
		printf("Case #%d: %d %I64d\n",cas++,ans1,ans2);
	}
    return 0;
}

