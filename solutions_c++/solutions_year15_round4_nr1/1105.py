#include<iostream>  
#include<stdio.h>
#include<string.h>
using namespace std;  
char a[105][105];
int cnt[105],cnt2[105],dk[105],rk[105];
int main(){  
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int nn,n,m,i,j,r=1,ans;
	cin>>nn;
	while(nn--){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;++i)
			for(j=1;j<=m;++j)
				scanf(" %c",&a[i][j]);
		cout<<"Case #"<<r<<": ";
		r++;
		memset(cnt,0,sizeof(cnt));
		memset(cnt2,0,sizeof(cnt2));
		for(i=1;i<=n;++i)
			for(j=1;j<=m;++j)
				cnt[i]+=(a[i][j]!='.'?1:0);
		for(j=1;j<=m;++j)
			for(i=1;i<=n;++i)
				cnt2[j]+=(a[i][j]!='.'?1:0);
		for(i=1;i<=n;++i){
			for(j=1;j<=m;++j)
				if(a[i][j]!='.'&&cnt[i]==1&&cnt2[j]==1) break;
			if(j<=m) break;
		}
		if(i<=n){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		for(i=1,ans=0;i<=n;++i){
			for(j=1;j<=m;++j){
				if(a[i][j]!='.'){
					if(a[i][j]=='<') ans++;
					break;
				}
			}
			for(j=m;j>=1;--j){
				if(a[i][j]!='.'){
					if(a[i][j]=='>') ans++;
					break;
				}
			}
		}
		for(j=1;j<=m;++j){
			for(i=1;i<=n;++i){
				if(a[i][j]!='.'){
					if(a[i][j]=='^') ans++;
					break;
				}
			}
			for(i=n;i>=1;--i){
				if(a[i][j]!='.'){
					if(a[i][j]=='v') ans++;
					break;
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}