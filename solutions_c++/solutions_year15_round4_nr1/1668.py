#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>

#define mk make_pair
#define pb push_back
#define inf 99999999
typedef  long long  LL;

using namespace std;

int ans ;
int r,c;
int dx[4]={-1,1,0,0}; 
int dy[4]={0,0,-1,1};
int dir[128][128];
char ge[128][128];

bool place(int x,int y){
	if (x<=0 || x>r || y<=0 || y>c )
		return false;
	return true;
}

int chg(char re){
	if(re=='.')
		return -1;
	if(re=='^')
		return 0;
	if(re=='v')
		return 1;
	if(re=='<')
		return 2;
	if(re=='>')
		return 3;
	return -1;
}

bool check(int x,int y){
	bool ex=false;
	for(int i=1;i<=c;i++)
		if(i!=y)
			if(dir[x][i]!=-1)	return true;
	for(int i=1;i<=r;i++)
		if(i!=x)
			if(dir[i][y]!=-1)	return true;
	return false;
}
int main(){
	int T;
	char re;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d%d",&r,&c);
		printf("Case #%d: ",cas);
		memset(dir,0,sizeof(dir));
		memset(ge,0,sizeof(ge));
		for(int i=1;i<=r;i++)
			scanf("%s",ge[i]+1);
		
		for(int i=1;i<=r;i++)
			for(int j=1;j<=c;j++)
				dir[i][j] = chg(ge[i][j]);
		
	
		bool flag = true;
		for(int i=1;i<=r;i++)
			for(int j=1;j<=c;j++){
				if(dir[i][j]!=-1){
					if(!check(i,j))
						flag=false;
				}
			}
			
		ans = 0;
		for(int j=1;j<=c;j++){
			for(int i=1;i<=r;i++){
				if(dir[i][j]!=-1){
					if(dir[i][j]==0)
						ans++;
					break;
				}
			}
			for(int i=r;i>=1;i--){
				if(dir[i][j]!=-1){
					if(dir[i][j]==1)
						ans++;
					break;
				}
			}
		}
		
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				if(dir[i][j]!=-1){
					if(dir[i][j]==2)
						ans++;
					break;
				}
			}
			for(int j=c;j>=1;j--){
				if(dir[i][j]!=-1){
					if(dir[i][j]==3)
						ans++;
					break;
				}	
			}
		}
		
		
		if(r==1 && c==1){
			if(dir[1][1]!=-1)
				puts("IMPOSSIBLE");
			else
				puts("0");
			continue;
		}
		
		if(!flag){
			puts("IMPOSSIBLE");
			continue;
		}
		

	
		printf("%d\n",ans);
	}
	
	return 0;
}