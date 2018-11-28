#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
int T;
int n,m;
char str[105][105];
int have[105][30];
int p;
int root;
vector<int> v[105];
int a[105];
int ans,times;
int work(){
	for (int i=0;i<m;i++) v[i].clear();
	for (int i=0;i<n;i++) v[a[i]].push_back(i);
	int ret=0;
	for (int i=0;i<m;i++){
	p=0;
	root=0;
	memset(have,0,sizeof(have));
		for (int j=0;j<v[i].size();j++){
			int tmp=root;
			int l=strlen(str[v[i][j]]);
			for (int k=0;k<l;k++){
				//cout<<tmp<<' '<<(int)(str[v[i][j]][k]-'A')<<' '<<have[tmp][str[v[i][j]][k]-'A']<<endl;
				if(have[tmp][str[v[i][j]][k]-'A']) tmp=have[tmp][str[v[i][j]][k]-'A'];
				else {
					p++;
					have[tmp][str[v[i][j]][k]-'A']=p;
					tmp=p;
				}
				//cout<<i<<' '<<j<<' '<<v[i][j]<<' '<<str[v[i][j]][k]<<' '<<p<<endl;
			}
		}
		if(p==0)p--;
		ret+=p+1;
	}
	//for (int i=0;i<n;i++) cout<<a[i]<<' ';cout<<endl;
	//cout<<ret<<endl;
	return ret;
}
void dfs(int st){
	if(st==n){
		int tmp=work();
		if(tmp>ans) {ans=tmp;times=1;}
		else if(tmp==ans) times++;
		return ;
	}
	for (int i=0;i<m;i++){
		a[st]=i;
		dfs(st+1);
	}
}
int main(){
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++){
			scanf(" %s",str[i]);
		}
		ans=0;
		times=0;
		dfs(0);
		printf("Case #%d: %d %d\n",ca++,ans,times);
	}
	return 0;
}
