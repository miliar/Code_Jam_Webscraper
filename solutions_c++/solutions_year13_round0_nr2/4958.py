#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <math.h>
#include <string>
using namespace std;

int ma[100+5][100+5];
int used[100+5][100+5];
int main(){
	int t,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int n,m;
		scanf("%d%d",&n,&m);
		memset(used,0,sizeof(used));
		for(int i=0;i<n;i++)for(int j=0;j<m;j++)scanf("%d",&ma[i][j]);
		int f=0;
		while(1){
			int Min = 1000,di,dj;
			for(int i=0;i<n;i++)for(int j=0;j<m;j++){
				if(used[i][j]==0&&ma[i][j]<Min){
					Min=ma[i][j];
					di=i;dj=j;
				}
			}
			if(Min==1000){
				break;
			}
		//	printf("%d\n",Min);
			int fc=0;
			for(int i=0;i<m;i++)
				if(used[di][i]==0&&ma[di][i]>Min){
				fc=1;break;
			}
			if(fc==1){}
			else{
				for(int i=0;i<m;i++)used[di][i]=1;
				continue;
			}
			fc=0;
			for(int i=0;i<n;i++)if(used[i][dj]==0&&ma[i][dj]>Min){
				fc=1;break;
			}
			if(fc==1){f=1;break;}
			else{
				for(int i=0;i<n;i++)used[i][dj]=1;
				continue;
			}
		}
		if(f==0)
		printf("Case #%d: YES\n",++cas);
		else printf("Case #%d: NO\n",++cas);
	}
	return 0;
}