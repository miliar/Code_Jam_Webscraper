#include<bits/stdc++.h>
#include<ext/rope>
#define f first
#define s second
using namespace std;
using namespace __gnu_cxx;
typedef pair<int,int>par;
typedef pair<int,par>pr;
int mp[105][505];
int dp[105][505];
int dx[]={-1,-1,-1,0,0,1,1,1},dy[]={-1,0,1,-1,1,-1,0,1};
int w,h,b;
bool chk(int x,int y){
	if(x<0||y<0||x>=w||y>=h)return 0;
	return 1;
	}
int main(){
	int T,t=0;
	scanf("%d",&T);
	while(T--){t++;
		scanf("%d%d%d",&w,&h,&b);
		for(int i=0;i<w;i++)
			for(int j=0;j<h;j++)
				mp[i][j]=1;
		while(b--){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int i=x1;i<=x2;i++)
				for(int j=y1;j<=y2;j++)
					mp[i][j]=0;
			}
		priority_queue<pr,vector<pr>,greater<pr> >pq;
		for(int i=0;i<h;i++){
			pq.push(pr(0,par(-1,i)));
			}
		memset(dp,0x3f,sizeof(dp));
		int ans=0;
		while(!pq.empty()){
			par now=pq.top().s;
			int pay=pq.top().f;
			//printf("%d %d %d\n",now.f,now.s,pay);
			pq.pop();
			if(now.f==w-1){ans=pay;break;}
			for(int k=0;k<8;k++){
				if(!chk(now.f+dx[k],now.s+dy[k]))continue;
				if(pay+mp[now.f+dx[k]][now.s+dy[k]]<dp[now.f+dx[k]][now.s+dy[k]]){
					dp[now.f+dx[k]][now.s+dy[k]]=pay+mp[now.f+dx[k]][now.s+dy[k]];
					pq.push(pr(dp[now.f+dx[k]][now.s+dy[k]],par(now.f+dx[k],now.s+dy[k])));
					}
				}
			}
		printf("Case #%d: %d\n",t,ans);

		}
    return 0;
    }
