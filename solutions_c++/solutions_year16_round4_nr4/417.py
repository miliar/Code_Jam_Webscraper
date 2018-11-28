#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#define LL long long
#define MAXN 100050
using namespace std;
char s[5][5];
char b[5][5];
bool bo[5];
int n;
int ans;
void dfs(int x,int y,int cnt){
	if(y>=n){
		x++;
		y=0;
	}
	if(x>=n){
//		printf("%d\n",cnt);
//		for(int i=0;i<n;++i){
//			printf("%s\n",b[i]);
//		}

		memset(bo,0,sizeof(bo));
		for(int i=0;i<n;++i){
			if(b[0][i]=='1')
				bo[i]=true;
		}
		for(int i=0;i<n;++i){
			int flag=0;
			for(int j=0;j<n;++j){
				if(b[i][j]=='1')
					flag=1;
			}
			if(flag==0)return;
		}
		for(int i=1;i<n;++i){
			for(int j=0;j<i;++j){
				int flag=0;
				for(int x=0;x<n;++x){
					if(b[i][x]=='1')
						bo[x]=true;
					if(b[i][x]=='1'&&b[j][x]=='1')
					{
						bo[x]=true;
						flag=1;
					}
				}
				if(flag==1){
					for(int x=0;x<n;++x){
						if(b[i][x]!=b[j][x])
						{

							return;
						}
					}
				}
			}
		}
		for(int i=0;i<n;++i)
			if(bo[i]==false)
			{
				return ;
			}
		if(ans>cnt)
			ans=cnt;
		return ;
	}
	b[x][y]=s[x][y];
	dfs(x,y+1,cnt);
	if(b[x][y]=='0'){
		b[x][y]='1';
		dfs(x,y+1,cnt+1);
	}
}
int main() {
	freopen("D-small-attempt1.in","r",stdin);
	freopen("outputD2.txt","w",stdout);
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d",&n);
		ans=n*n+1;
		for(int i=0;i<n;++i){
			scanf(" %s",s[i]);
		}
		dfs(0,0,0);
		printf("Case #%d: %d\n",++ri,ans);
	}
	return 0;
}
