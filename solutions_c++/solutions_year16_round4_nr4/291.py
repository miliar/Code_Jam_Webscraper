#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;
typedef long long LL;
const int N=10;
int e[N][N],perm[N],n;
char ch[N];
bool used[N],syf[N],flag;
int ans;
bool check(int x){
	if(x==n+1) return 1;
	bool ff = 0;
	for(int i=1;i<=n;i++)
		if(e[perm[x]][i] && !syf[i]){
			ff = 1;
			syf[i]=1;
			if(!check(x+1)) return 0;
			syf[i]=0;
		}
	return ff;
}
void work_per(int x){
	if(x==n+1){
		for(int i=1;i<=n;i++)
			syf[i]=0;
		//cout<<perm[1]<<' '<<perm[2]<<' '<<perm[3]<<endl;
		if (!check(1)) flag=0;
	}else{
		for(int i=1;i<=n;i++)
			if(!used[i]){
				used[i]=1;
				perm[x]=i;
				work_per(x+1);
				used[i]=0;
			}
	}
}
void dfs(int x,int y,int now){
	if(now >= ans) return;
	if(x==n+1){
		flag = 1;
		/*cout<<now<<endl;
		for(int i=1;i<=3;i++){
			for(int j=1;j<=3;j++)
				cout<<e[i][j];
			cout<<endl;
		}*/
		work_per(1);
		if(flag) {
			//cout<<"now="<<now<<endl;
			ans = now;
		}
	}else{
		int xx = x,yy = y;
		yy++;
		if(yy==n+1){
			yy=1;
			xx++;
		}
		dfs(xx,yy,now);
		if(e[x][y]==0){
			e[x][y]=1;
			dfs(xx,yy,now+1);
			e[x][y]=0;
		}
	}
}
int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++){
		scanf("%d\n",&n);
		for(int i=1;i<=n;i++){
			scanf("%s",ch);
			for(int j=0;j<4;j++){
				e[i][j+1]=(ch[j]=='1');
			}
		}
		ans = n * n;
		dfs(1,1,0);
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}
/*
1
3
000
000
000
*/
