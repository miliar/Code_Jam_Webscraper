#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#define maxl 1000000000
using namespace std;

int n;

map<int,int> mm,ori;
int two[30];
vector<int> v[30];
int need[30];
int pre[1100000],dui[1100000],head,tail;

void predo(int zt){
	mm=ori;
	int i,j;
	for(i=1;i<=n;++i)if(two[i]&zt){
		for(j=0;j<v[i].size();++j)++mm[v[i][j]];
		--mm[need[i]];
	}
}

void print(int zt){
	if(zt==0)return ;
	print(zt-two[pre[zt]]);
	printf("%d",pre[zt]);
	if(zt==two[n+1]-1)printf("\n");else printf(" ");
}
	

void solve(){
	int m,i,j,x,y;
	scanf("%d%d",&m,&n);
	ori.clear();
	
	for(i=1;i<=m;++i){
		scanf("%d",&x);
		++ori[x];
	}
	
	for(i=1;i<=n;++i){
		v[i].clear();
		scanf("%d%d",&need[i],&x);
		for(j=1;j<=x;++j){
			scanf("%d",&y);
			v[i].push_back(y);
		}
	}
	//cout<<"?"<<endl;
	two[1]=1;
	for(i=2;i<=n+1;++i)two[i]=two[i-1]<<1;
	for(i=0;i<two[n+1];++i)pre[i]=-1;
	pre[0]=0;
	head=0;tail=1;
	dui[tail]=0;
	while(head<tail){
		i=dui[++head];
		predo(i);
		for(j=1;j<=n;++j)if((two[j]&i)==0 && mm[need[j]]>0){
			if(pre[two[j]|i]==-1){
				pre[two[j]|i]=j;
				dui[++tail]=two[j]|i;
			}
		}
	}
	for(i=0;i+1<two[n+1];++i)if(pre[i]!=-1){
	}
	if(pre[two[n+1]-1]==-1)printf("IMPOSSIBLE\n");else print(two[n+1]-1);
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}