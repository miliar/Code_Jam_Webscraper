#include<cstdio>
#include<string>
#include<cstring>
#include<unordered_map>
#include<vector>
#include<cctype>
#define inf 1023456789
#define M 11000
#define N 30
using namespace std;
char m[3010];
unordered_map<string,int> id;
char s[M],t[M];
vector<int> g[N];
int main(){
	int T,cs,n,i,j,k,sz,now,ans,num;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		ans=inf;
		scanf("%d",&n);
		getchar();
		id.clear();
		num=0;
		for(i=0;i<n;i++){
			g[i].clear();
			gets(s);
			sz=0;
			for(j=0;s[j];j++){
				if(islower(s[j])){
					t[sz++]=s[j];
				}
				else if(sz){
					t[sz]=0;
					if(!id.count(string(t))){
						id[string(t)]=num++;
					}						
					g[i].push_back(id[string(t)]);
					sz=0;
				}
			}
			if(sz){
				t[sz]=0;
				if(!id.count(string(t))){
					id[string(t)]=num++;
				}						
				g[i].push_back(id[string(t)]);
				sz=0;
			}
		}
		for(i=0;i<(1<<n);i+=4){
			memset(m,0,sizeof(m));
			now=0;
			for(j=0;j<g[0].size();j++) m[g[0][j]]|=1;
			for(j=0;j<g[1].size();j++) m[g[1][j]]|=2;
			for(j=2;j<n;j++){
				if(i&(1<<j)){
					for(k=0;k<g[j].size();k++) m[g[j][k]]|=1;
				}
				else{
					for(k=0;k<g[j].size();k++) m[g[j][k]]|=2;
				}
			}
			for(j=0;j<num;j++) if(m[j]==3) now++;
			if(now<ans) ans=now;
		}
		printf("Case #%d: %d\n",cs,ans);
 	}
	return 0;
}