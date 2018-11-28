#include<cstdio>
#include<vector>
#include<map>
using namespace std;
#define sz(X) (int)X.size()

map< pair< map<int,int>, vector<int> >, vector<int> > PD;

int type[210];
vector<int> inside[210];
vector<int> solve(map<int,int> keys, vector<int> baus, int n) {
	vector<int> ret;	
	if(sz(baus)==0)
		return ret;
	if(PD.find(make_pair(keys,baus))!=PD.end())
		return PD[make_pair(keys,baus)];
	for(int i=0;i<sz(baus);i++){
    if(keys[type[baus[i]]]){
			map<int,int> keys2 = keys;
			keys2[type[baus[i]]]--;
			vector<int> baus2 = baus;
			baus2.erase(baus2.begin()+i);
			for(int j=0; j<sz(inside[baus[i]]);j++)
				keys2[inside[baus[i]][j]]++;
			vector<int> resp = solve(keys2,baus2,n-1);
			if(sz(resp)==n-1){
				ret.push_back(baus[i]);
				ret.insert(ret.end(),resp.begin(),resp.end());
				PD[make_pair(keys,baus)]=ret;
				return ret;
			}
		}
	}
	PD[make_pair(keys,baus)]=ret;
	return ret;
}


int main(){
	int T;
	scanf("%d",&T);
	for(int caso=1;caso<=T;caso++){
		PD.clear();
		int n,k;
		scanf("%d %d",&k,&n);
		map<int,int> keys;
		vector<int> baus;
		for(int i=1;i<=n;i++){
			baus.push_back(i);
			inside[i].clear();
		}
		for(int i=0;i<k;i++){
			int x;
			scanf("%d",&x);
			keys[x]++;
		}
		for(int i=1;i<=n;i++){
			int ki;
			scanf("%d %d", &type[i],&ki);
			while(ki--){
				int x;
				scanf("%d",&x);
				inside[i].push_back(x);
			}
		}
		vector<int> ret = solve(keys,baus,n);
		if(sz(ret)==0)
			printf("Case #%d: IMPOSSIBLE\n",caso);
		else{
			printf("Case #%d:",caso);
			for(int i=0;i<sz(ret);i++)
				printf(" %d",ret[i]);
			printf("\n");
		}
	}
	return 0;
}
