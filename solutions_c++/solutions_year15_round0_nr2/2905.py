#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

int data[1005];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		int n;
		scanf("%d",&n);
		int maxh=0;
		for(int i=0;i<n;i++) scanf("%d",&data[i]),maxh=max(maxh,data[i]);
		int ans=maxh;
		for(int i=1;i<maxh;i++){
			int cnt=0;
			for(int j=0;j<n;j++)
				cnt+=(data[j]-1)/i;
			ans=min(cnt+i,ans);
		}
		printf("Case #%d: %d\n",Case,ans);
	}
    return 0;
}

