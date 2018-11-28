#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
char ch[210],s[210][210];
int n,head,m,size[210],ans[210],father[210],pd[210];
double C[210][210],w[10],num[210],f[210],A[210],B[210];
int way[210],N;
vector<int>go[210];
void treedp(int k1){
	size[k1]=1; num[k1]=1;
	for (int i=0;i<go[k1].size();i++){
		treedp(go[k1][i]);
		size[k1]+=size[go[k1][i]];
		num[k1]=num[k1]*num[go[k1][i]]*C[size[k1]-1][size[go[k1][i]]];
	}
}
int ti=20000,inf=(1e9);
double getrand(){
	return 1.0*rand()/RAND_MAX;
}
void get(){
	way[1]=0; f[1]=1; N=1;
	for (int now=0;now<=n;now++){
		int where=0; double k1=getrand(); //cout<<"fa "<<k1<<endl;
		for (int i=1;i<=N;i++){
			if (pd[way[i]]) continue;
		//	cout<<"rem "<<i<<" "<<f[i]<<endl;
			if (f[i]>=k1){
				where=way[i]; break;
			} else k1-=f[i];
		}
		double tot=0;
		for (int i=1;i<=N;i++){
			if (pd[way[i]]==0) tot+=f[i];
		}
		pd[where]=1; //cout<<where<<endl;
		if (now) ans[now]=ch[where];
		for (int i=0;i<go[where].size();i++) way[++N]=go[where][i];
		int presize=0; 
		for (int i=1;i<=N;i++)
			if (pd[way[i]]==0){
				presize+=size[way[i]];
			//	cout<<"fafa "<<i<<" "<< C[presize-1][size[way[i]]-1]*C[N-now-1][presize-1]<<" "<<C[N-now][presize]<<" "<<C[presize][size[way[i]]]<<endl;
				f[i]=C[presize-1][size[way[i]]-1]*C[n-now-1][presize-1]/C[n-now][presize]/C[presize][size[way[i]]];
			}
	//	for (int i=1;i<=N;i++) cout<<way[i]<<" "<<f[i]<<endl; cout<<endl;
	}
//	for (int i=1;i<=n;i++) cout<<ans[i]<<" "; cout<<endl;
	for (int i=1;i<=m;i++){
		int len=strlen(s[i]+1); int flag=0;
		for (int j=1;j<=N-len+1;j++){
			int k1=0;
			for (int k=1;k<=len;k++) if (ans[j+k-1]!=s[i][k]) {k1=1; break;}
			if (k1==0){
				flag=1; break;
			}
		}
		w[i]+=flag;
	}
}
int solve(){
	scanf("%d",&n);
	for (int i=0;i<=n;i++) go[i].clear();
	for (int i=1;i<=n;i++){
		int k1; scanf("%d",&k1); go[k1].push_back(i); father[i]=k1;
	}
	scanf("%s",ch+1);
	scanf("%d",&m);
	for (int i=1;i<=m;i++) scanf("%s",s[i]+1);
	treedp(0);
	memset(w,0x00,sizeof w);
	for (int i=1;i<=ti;i++){
		memset(pd,0x00,sizeof pd);
		get();
	}
	for (int i=1;i<=m;i++) printf("%.5lf ",(double)w[i]/(double)ti);
	printf("\n");
}
int main(){
	freopen("Bs3.in","r",stdin);
	freopen("Bs4.out","w",stdout);
	for (int i=0;i<=130;i++){
		C[i][0]=1;
		for (int j=1;j<=i;j++) C[i][j]=C[i-1][j]+C[i-1][j-1];
	}
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}
