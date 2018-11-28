#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;
typedef long long LL;
#define mod 1000000007
#define N 60
#define DEBUG 1

int T,n,ans,tp;
int f[N][N],st[N];
struct row{
	int a[N];
	bool operator<(const row ff) const{
		for(int i=1;i<=n;i++){
			if(a[i]!=ff.a[i]) return a[i]<ff.a[i];
		}
	}
}x[N*2];

void dfs(int i){
	if(ans||n*2-i<n-tp) return;
	dfs(i+1);
	st[tp++]=i;
	if(tp==n){
		for(int j=0;j<tp;j++){
			for(int k=1;k<=n;k++) f[j+1][k]=x[st[j]].a[k];
		}
		int res=0,idx=0,col=0;
		for(int j=1;j<n*2;j++){
			if(j==st[idx]) idx++;
			else{
				col++;
				for(int k=1;k<=n;k++){
					if(f[k][col]!=x[j].a[k]){
						res=col;
						break;
					}
				}
				if(res){
					for(col++;col<=n;col++){
						for(int k=1;k<=n;k++){
							if(f[k][col]!=x[j].a[k]){
								res=-1;
								break;
							}
						}
						if(res<0) break;
						while(j<n*2){
							j++;
							if(j==st[idx]) idx++;
							else break;
						}
					}
					break;
				}
			}
		}
		if(res>=0){
			if(res==0) res=n;
			ans=1;
			for(int k=1;k<=n;k++) printf(" %d",f[k][res]);
		}
	}else dfs(i+1);
	if(ans) return;
	tp--;
}

int main() {
	if(DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%d",&n);
    	for(int i=1;i<n*2;i++){
	    	for(int j=1;j<=n;j++) scanf("%d",&x[i].a[j]);
	    }
	    sort(x+1,x+n+n);
	    printf("Case #%d:",t);
	    ans=tp=0;
	    dfs(1);
	    printf("\n");
    }
    return 0;
}
