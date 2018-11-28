#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<time.h>
#define MAXRUN 100000
using namespace std;
int n,m;
int son[111][111],ls[111];
double c[111][111];
int sz[111];
double dp[111];
char s[111],ss[111];
char q[9][99];int len[9];
void dfs(int x){
	dp[x] = 1;
	sz[x] = 0;
	for(int i=0; i<ls[x]; i++){
		int y=son[x][i];
		dfs(y);
		dp[x]*=dp[y];
		dp[x]*=c[sz[x]+sz[y]][sz[y]];
		sz[x]+=sz[y];
	}
	sz[x]++;
}

bool f[111];
double res[9];
int main(){
	for(int i=0; i<=100; i++)
		for(int j=0; j<=i; j++)
			c[i][j]=j==0||j==i?1:c[i-1][j]+c[i-1][j-1];
	srand(time(0));
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		printf("Case #%d: ",T);
		fprintf(stderr,"Case #%d: ",T);
		scanf("%d",&n);
		memset(ls,0,sizeof(ls));
		for(int i=1; i<=n; i++){
			int x;
			scanf("%d",&x);
			son[x][ls[x]++]=i;
		}
		dfs(0);
		scanf("%s",s+1);
		scanf("%d",&m);
		for(int j=0; j<m; j++){
			scanf("%s",q[j]);
			len[j] = strlen(q[j]);
		}
		memset(res,0,sizeof(res));
		for(int run=0; run<MAXRUN; run++){
			
			for(int j=0; j<ls[0]; j++)
				f[son[0][j]] = true;
			for(int i=1; i<=n; i++){
				double prob = 0;
				double p = rand()/(double)RAND_MAX;
				for(int k=1; k<=n; k++)
					if(f[k]){
						prob += (double)sz[k]/(n-i+1);
						if(prob >= p){
							ss[i] = s[k];
							f[k] = false;
							for(int j=0; j<ls[k]; j++)
								f[son[k][j]] = true;
							break;
						}
					}
			}
			for(int j=0; j<m; j++){
				bool flag=false;
				for(int i=1; i+len[j]-1<=n; i++)
					if(memcmp(ss+i, q[j],sizeof(char)*len[j])==0){
						flag=true;
						break;
					}
				if(flag)
					res[j]+=1.0;
			}
		}
		for(int j=0; j<m; j++)
			printf("%lf%c",res[j]/MAXRUN,j<m-1?' ':'\n');
	}
	return 0;
}
