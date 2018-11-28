#include<stdio.h>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
int res,res2,n,maxDep;
vector<int> v[1111];
int ace[1111],a[1111];
int ancestor(int x){return x-ace[x]?ace[x]=ancestor(ace[x]):x;}
void dfs(int x,int fat,int d){
	maxDep=max(maxDep,d);
	for(vector<int>::iterator it=v[x].begin(); it!=v[x].end(); it++){
		int y=*it;
		if(y==fat)continue;
		dfs(y,x,d+1);
	}
}
int main(){
	int _,T;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		scanf("%d",&n);
		for(int i=1; i<=n; i++){
			v[i].clear();
			ace[i]=i;
		}
		for(int i=1; i<=n; i++){
			scanf("%d",&a[i]);
			v[a[i]].push_back(i);
			ace[ancestor(i)]=ancestor(a[i]);
		}
		res=0;res2=0;
		for(int i=1; i<=n; i++){
			if(ancestor(i) != i) continue;
			set<int> s;
			int x;
			for(x=i; !s.count(x); x=a[x])
				s.insert(x);
			vector<int> cycle;
			cycle.push_back(x);
			int w = a[x];
			while(w!=x){
				cycle.push_back(w);
				w = a[w];
			}
			if(cycle.size()>2){
				res=max(res,(int)cycle.size());
				continue;
			}
			w=a[x];
			int now=2;
			maxDep=-1;
			dfs(x,w,0);
			now+=maxDep;
			maxDep=-1;
			dfs(w,x,0);
			now+=maxDep;
			res2+=now;
		}
		printf("Case #%d: %d\n",T,max(res2,res));
	}
	return 0;
}