#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include <algorithm>
#include <cmath>
#include "time.h"
#include "stdlib.h"
using namespace std;
int a[4][4],b[4][4];
int main()
{
	int n,i,txt,l=1,m,j;
	freopen("c:\\A-small-attempt0.in","r",stdin);
	freopen("c:\\A-small-attempt0.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		scanf("%d",&n);
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				scanf("%d",&b[i][j]);
		int cnt=0,k;
		for(i=0;i<4;++i){
			for(j=0;j<4;++j)
				if(a[n-1][i]==b[m-1][j])
				{
					cnt++;
					k=a[n-1][i];
					break;
				}
		}
		if(cnt==0)printf("Case #%d: Volunteer cheated!\n",l++);
		else if(cnt==1)printf("Case #%d: %d\n",l++,k);
		else printf("Case #%d: Bad magician!\n",l++);
	}
	return 0;
}
