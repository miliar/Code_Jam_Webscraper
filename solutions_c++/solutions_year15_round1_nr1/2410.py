#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <string.h>
using namespace std;
int n;

int a[10005];
int ans1,speed,ans2;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
    	ans1=0,speed=0;ans2=0;
    	scanf("%d",&n);
    	for(int t=0;t<n;t++){
			scanf("%d",&a[t]);
    	}
    	for(int t=1;t<n;t++){
			if(a[t]<a[t-1]){
				ans1+=(a[t-1]-a[t]);
				speed = max(speed,a[t-1]-a[t]);
			}
    	}
    	for(int t=0;t<n-1;t++){
			ans2+=min(a[t],speed);
    	}
        printf("Case #%d: %d %d\n",cas++,ans1,ans2);
    }
    return 0;
}
