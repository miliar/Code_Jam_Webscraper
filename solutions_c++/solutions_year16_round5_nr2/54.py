#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
vector<int>g[210];
char in[210];
int sz[210];
int dfs(int a){
	int ret=1;
	for(int i=0;i<g[a].size();i++){
		ret+=dfs(g[a][i]);
	}
	return sz[a]=ret;
}
char cur[210];
char str[10][210];
int ans[10];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;scanf("%d",&a);
		for(int i=0;i<210;i++)g[i].clear();
		for(int i=0;i<a;i++){
			int p;scanf("%d",&p);
			g[p].push_back(i+1);
		}
		dfs(0);
		scanf("%s",in);
		int b;scanf("%d",&b);
		for(int i=0;i<b;i++)scanf("%s",str[i]);
		int S=50000;
		for(int i=0;i<b;i++)ans[i]=0;
		for(int i=0;i<S;i++){
			int ind=a;
			vector<int>at;
			for(int j=0;j<g[0].size();j++)at.push_back(g[0][j]);
			for(int j=0;j<a;j++){
				int tmp=rand()%ind;
				for(int k=0;k<at.size();k++){
					if(tmp<sz[at[k]]){
						int pos=at[k];
						cur[j]=in[at[k]-1];
						for(int l=k+1;l<at.size();l++){
							at[l-1]=at[l];
						}
						at.pop_back();
						for(int l=0;l<g[pos].size();l++)at.push_back(g[pos][l]);
						ind--;break;
					}else tmp-=sz[at[k]];
				}
			}
		//	if(cur[0])printf("%s\n",cur);
			for(int j=0;j<b;j++){
				bool OK=false;
				for(int k=0;k<a;k++){
					bool ok=true;
					for(int l=0;str[j][l];l++){
						if(str[j][l]!=cur[k+l]){ok=false;break;}
					}
					if(ok){OK=true;break;}
				}
				if(OK){
					ans[j]++;
				}
			}
		}
		printf("Case #%d:",t);
		for(int i=0;i<b;i++)printf(" %.4f",(double)ans[i]/S);
		printf("\n");
		fprintf(stderr,"%d\n",t);
	}
}