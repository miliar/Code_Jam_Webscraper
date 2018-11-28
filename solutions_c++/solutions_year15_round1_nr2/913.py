#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;
int T,b,n,cas=1;
int m[1005];
long long serve(long long t){
	if(t==-1)return 0;
	long long ans=0;
	for(int i=0;i<b;i++)
		ans+=t/m[i]+1;
	return ans;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("blargeout.txt","w",stdout);
	for(scanf("%d",&T);cas<=T;){
		scanf("%d%d",&b,&n);
		int maxx=0;
		for(int i=0;i<b;i++){
			scanf("%d",&m[i]);
			maxx=max(maxx,m[i]);
		}
		long long lb=-1,rb=(long long)maxx*n,mid;
		while(rb-lb>3){
			mid=(lb+rb)/2;
			if(serve(mid)>=n) rb=mid-1;
			else lb=mid;
		}
		//printf("%I64d %I64d\n",lb,rb);
		for(long long i=lb;i<=rb;i++){
			if(serve(i)<n&&serve(i+1)>=n){
				mid=i;
				break;
			}
		}
		mid++;
		int cnt=serve(mid-1),ans;
		for(int i=0;i<b;i++){
			if(mid%m[i]==0){
				cnt++;
				if(cnt==n){
					ans=i+1;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
		fflush(stdout);
	}
    return 0;
}

