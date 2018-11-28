#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
struct atom{
	int a,b;
}ans[1<<20];
atom operator + (atom k1,atom k2){
	return (atom){k1.a+k2.a,k1.b+k2.b};
}
int dp[1<<16][26][26],num[1<<16],extraA[1<<16],extraB[1<<16],len,w[(1<<16)],size[(1<<16)],pd[100],go[60][60],n;
int num1,num2,num3,b[50][50];
int limA,limB;
char ch[10];
void dfs(int k){
	pd[k]=1; if (k>n) num2++; else num1++;
	for (int i=1;i<=n*2;i++)
		if (go[k][i]){
			num3++; if (pd[i]==0) dfs(i);
		}
}
int check(){
	len=0; limA=0; limB=0;
	memset(go,0x00,sizeof go);
	memset(pd,0x00,sizeof pd);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++) go[i][j+n]=b[i][j],go[j+n][i]=b[i][j];
	for (int i=1;i<=n*2;i++)
		if (pd[i]==0){
			num1=0; num2=0; num3=0;
			dfs(i); //cout<<len<<endl;
			if (num1==1&&num2==1) continue;
			if (num1==0&&num2==1) {limB++; continue;}
			if (num1==1&&num2==0) {limA++; continue;}
			len++;
			ans[(1<<len-1)]=(atom){num1,num2}; w[(1<<len-1)]=num3/2;
		}
}
void update(int &k1,int k2){
	k1=min(k1,k2);
}
int solve(){
	scanf("%d",&n);
	memset(dp,0x3f,sizeof dp);
	memset(w,0x00,sizeof w);
	for (int i=1;i<=n;i++){
		scanf("%s",ch+1);
		for (int j=1;j<=n;j++) b[i][j]=ch[j]-'0';
	}
	check();
//	for (int i=1;i<=len;i++) cout<<ans[(1<<i-1)].a<<" "<<ans[(1<<i-1)].b<<" "<<w[1<<i-1]<<endl;
	for (int i=1;i<(1<<len);i++){
		int k1=i&(-i);
		w[i]=w[k1]+w[i-k1];
		ans[i]=ans[k1]+ans[i-k1];
	}
	for (int i=0;i<(1<<len);i++){
		extraB[i]=max(ans[i].a-ans[i].b,0);
		extraA[i]=max(ans[i].b-ans[i].a,0);
		int k1=max(ans[i].a,ans[i].b);
		w[i]=k1*k1-w[i];
	}
//	cout<<w[1]<<" "<<extraA[1]<<" "<<extraB[1]<<" "<<ans[1].a<<" "<<ans[1].b<<endl;
	dp[0][0][0]=0; int pre=n*n;
	for (int now=0;now<(1<<len);now++){
		int k1=(1<<len)-1-now;
		for (int i=0;i<=limA;i++)
			for (int j=0;j<=limB;j++)
				if (dp[now][i][j]<pre){
				//	cout<<"fa "<<now<<" "<<i<<" "<<j<<" "<<dp[now][i][j]<<endl;
					int ww=dp[now][i][j];
					for (int k=k1;k;k=(k-1)&k1)
						if (i+extraA[k]<=limA&&j+extraB[k]<=limB){
						//	cout<<"update "<<k<<endl;
							update(dp[now+k][i+extraA[k]][j+extraB[k]],ww+w[k]);
						}
				}
	}
	int ans=n*n;
	for (int i=0;i<=limA;i++)
		for (int j=0;j<=limB;j++)
			if (limA-i==limB-j){
			//	cout<<"fa "<<i<<" "<<j<<" "<<dp[(1<<len)-1][i][j]<<endl;
				ans=min(ans,dp[(1<<len)-1][i][j]+limA-i);
			}
	return ans;
}
int main(){
	freopen("Dl.in","r",stdin);
	freopen("Dl.out","w",stdout);
	int t; scanf("%d",&t);
	for (int tt=1;tt<=t;tt++){
		printf("Case #%d: %d\n",tt,solve());
	}
}
