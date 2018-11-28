#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

#define indexOf(a,v) (find((a).begin(),(a).end(),v)-(a).begin())

struct Chest{
	int type;
	vector<int> inside;
}chest[20];
int K,N;
vector<int> key[1<<20];
vector<int> perm[1<<20];


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	rep(i,t){
		cin>>K>>N;
		rep(j,1<<N){
			perm[j].clear();
			perm[j].push_back(INF);
			key[j].clear();
			key[j].push_back(INF);
		}
		perm[0].clear();
		key[0].clear();

		rep(j,K){
			int a;
			cin>>a;
			key[0].push_back(a);
		}
		rep(j,N){
			int ti,ki;
			cin>>ti>>ki;
			chest[j].type=ti;
			rep(_,ki){
				int a;
				cin>>a;
				chest[j].inside.push_back(a);
			}
		}
		rep(j,(1<<N)-1){
			if(key[j].size()==1&&key[j][0]==INF)continue;
			rep(k,N){
				if(j>>k&1)continue;
				int index=indexOf(key[j],chest[k].type);
				if(index==key[j].size())continue;
				int next=j|1<<k;
				if(key[next].size()==1&&key[next][0]==INF){
					key[next]=key[j];
					key[next].erase(key[next].begin()+index);
					key[next].insert(key[next].end(),chest[k].inside.begin(),chest[k].inside.end());
				}
				vector<int> tmp=perm[j];
				tmp.push_back(k);
				if(tmp<perm[next])perm[next]=tmp;
			}
		}
		vector<int> &ans=perm[(1<<N)-1];
		cout<<"Case #"<<i+1<<":";
		if(ans[0]!=INF)
			rep(j,ans.size())cout<<' '<<ans[j]+1;
		else cout<<" IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}