#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
int ca,ti,r,n,m,k,x[100],i,j,y[100],ans[100];
bool ok;
map<int,int> g;
double best,mul;
void dfs(int r,int cur){
	if(r>n)
		g[cur]++;
	else{
		dfs(r+1,cur);
		dfs(r+1,cur*y[r]);
	}
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>r>>n>>m>>k;
		cout<<"Case #"<<ti<<":"<<endl;
		while(r--){
			fr(i,1,k)
				cin>>x[i];
			best=0;
			fr(j,1,1000){
				g.clear();
				fr(i,1,n)
					y[i]=rand()%(m-1)+2;
				dfs(1,1);
				mul=1;
				fr(i,1,k)
					mul*=g[x[i]];
				if(mul>best){
					best=mul;
					fr(i,1,n)
						ans[i]=y[i];
				}
			}
			fr(i,1,n)
				cout<<ans[i];
			cout<<endl;
		}
	}
}
