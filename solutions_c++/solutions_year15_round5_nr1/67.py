#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
vector<int>g[1100000];
int S[1100000];
int L[1100000];
int R[1100000];
vector<pair<int,int> >ev;
vector<pair<int,int> >ev2;

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int N,D;
		scanf("%d%d",&N,&D);
		int S0,As,Cs,Rs;
		scanf("%d%d%d%d",&S0,&As,&Cs,&Rs);
		int M0,Am,Cm,Rm;
		scanf("%d%d%d%d",&M0,&Am,&Cm,&Rm);
		S[0]=S0;
		for(int i=1;i<N;i++){
			S[i]=((long long)S[i-1]*As+Cs)%Rs;
			M0=((long long)M0*Am+Cm)%Rm;
			int par=M0%i;
			g[par].push_back(i);
		}
		queue<pair<int,pair<int,int> > > Q;
		Q.push(make_pair(0,make_pair(S[0],S[0])));
		while(Q.size()){
			int at=Q.front().first;
			int left=Q.front().second.first;
			int right=Q.front().second.second;
			Q.pop();
			L[at]=left;
			R[at]=right;
			for(int i=0;i<g[at].size();i++){
				Q.push(make_pair(g[at][i],make_pair(min(left,S[g[at][i]]),max(right,S[g[at][i]]))));
			}
		}
		ev.clear();
		ev2.clear();
		for(int i=0;i<N;i++){
			if(R[i]-L[i]>D)continue;
			ev.push_back(make_pair(R[i],L[i]));
			ev2.push_back(make_pair(L[i],R[i]));
	//		printf("%d %d\n",L[i],R[i]);
		}
		std::sort(ev.begin(),ev.end());
		std::sort(ev2.begin(),ev2.end());
		
		int ret=0;
		int rat=0;
		for(int i=0;i<ev.size();i++){
			while(ev2[rat].first+D<ev[i].first){
				rat++;
			}
			ret=max(ret,i-rat+1);
		}
		printf("Case #%d: %d\n",t,ret);
		for(int i=0;i<N;i++)g[i].clear();
	}
}