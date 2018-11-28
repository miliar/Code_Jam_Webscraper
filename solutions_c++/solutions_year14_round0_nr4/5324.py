#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include <algorithm>
#include <cmath>
#include "time.h"
#include "stdlib.h"
using namespace std;
double a[1004],b[1004];
bool v[1004];
int main()
{
	int n,i,txt,l=1,j;
//	freopen("c:\\D-small-attempt0.in","r",stdin);
//	freopen("c:\\D-small-attempt0.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%lf",&a[i]);
		for(i=0;i<n;++i)
			scanf("%lf",&b[i]);
		printf("Case #%d: ",l++);
		sort(a,a+n);
		sort(b,b+n);
		int cnt=0;
		memset(v,0,sizeof(bool)*n);
		for(j=n-1;j>=0;--j){
			for(i=0;i<n;++i){
				if(v[i]==0&&a[i]>b[j])
				{
					cnt++;
					v[i]=1;
					break;
				}
			}
			if(i>=n){//no found!
				for(i=0;i<n;++i)
					if(v[i]==0)
						break;
				v[i]=1;
			}
		}
		printf("%d ",cnt);
		cnt=0;
		memset(v,0,sizeof(bool)*n);
		for(i=0;i<n;++i){
			for(j=0;j<n;++j){
				if(v[j]==0&&b[j]>a[i])
				{
					v[j]=1;
					break;
				}
			}
			if(j>=n){//no found!
				for(j=0;j<n;++j)
					if(v[j]==0){
						cnt++;
						break;
					}
				v[j]=1;
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}
