#include<bits/stdc++.h>
using namespace std;
/*char bord[25][25];
bool ok(int h,int w,int y,int x){
	// pre-check
	for(int i=0;i<h;i++)for(int j=0;j<w;j++){
		if(i>y || (i==y&&j>x))continue;
		int dy[]={0,1,0,-1},dx[]={1,0,-1,0};
		int cnt=0;
		for(int dir=0;dir<4;dir++){
			int i2=i+dy[dir],j2=(j+dx[dir]+w)%w;
			if(i2>y || (i2==y&&j2>x))continue;
			if(0<=i2&&i2<h&&bord[i2][j2]==bord[i][j])cnt++;
		}
		if(cnt>(bord[i][j]-'0')){
			return false;
		}
	}
	return true;
}
void dfs(int h,int w,int y,int x){
	for(int i=0;i<h;i++)for(int j=0;j<w;j++)if(i<y||(i==y&&j<x))assert(bord[i][j]=='1'||bord[i][j]=='2');
	if(y==h){
		// check
		for(int i=0;i<h;i++)for(int j=0;j<w;j++){
			int dy[]={0,1,0,-1},dx[]={1,0,-1,0};
			int cnt=0;
			for(int dir=0;dir<4;dir++){
				int i2=i+dy[dir],j2=(j+dx[dir]+w)%w;
				if(0<=i2&&i2<h){
					if(bord[i2][j2]=='.')goto nxt;
					if(bord[i2][j2]==bord[i][j])cnt++;
				}
			}
			if(cnt!=(bord[i][j]-'0'))return;
			nxt:;
		}
		puts("SOL:");
		for(int i=0;i<h;i++){bord[i][w]=0;printf("%s\n",bord[i]);}
		return;
	}
	bord[y][x]='1';
	if(ok(h,w,y,x)){if(x==w-1)dfs(h,w,y+1,0);else dfs(h,w,y,x+1);}
	bord[y][x]='2';
	if(ok(h,w,y,x)){if(x==w-1)dfs(h,w,y+1,0);else dfs(h,w,y,x+1);}
	bord[y][x]='.';
}*/
int main(){
	/*for(int h=2;h<=5;h++)for(int w=3;w<=15;w++){
		printf("%d x %d\n",h,w);
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)bord[i][j]='.';
		dfs(h,w,0,0);
	}*/
	static int dp_12[105][105][105], dp_3[105][105][105];
	memset(dp_12,0,sizeof dp_12);
	memset(dp_3,0,sizeof dp_3);
	const int mod = 1000000007;
	#define ADD(x,y)x=(x+(y))%mod
	for(int w=3;w<=100;w++){
		dp_12[0][w][w]=dp_3[0][w][w]=1;
		for(int h=0;h<=100;h++){
			for(int g=1;g<=w;g++)ADD(dp_3[h+2][w][g],dp_12[h][w][g]);
			
			for(int g=1;g<=w;g++)ADD(dp_12[h+1][w][g],dp_3[h][w][g]);
			if(w%3==0)for(int g=1;g<=w;g++)ADD(dp_12[h+2][w][__gcd(g,w/3)],(long long)dp_3[h][w][g]*3);
			if(w%6==0)for(int g=1;g<=w;g++)ADD(dp_12[h+2][w][__gcd(g,w/6)],(long long)dp_3[h][w][g]*6);
			if(w%4==0)for(int g=1;g<=w;g++)ADD(dp_12[h+3][w][__gcd(g,w/4)],(long long)dp_3[h][w][g]*4);
		}
	}
	// elke oplossing komt 1, 2, 3, 4 of 6 keer voor.
	int T;cin>>T;
	for(int tc=1;tc<=T;tc++){
		int h,w;cin>>h>>w;
		int ans=0;
		for(int g=1;g<=w;g++){
			int v=(dp_12[h][w][g]+dp_3[h][w][g])%mod;
			ans+=v/(w/g);
			ans%=mod;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}
