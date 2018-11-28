#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int T,Case,N,M,i,j,k,mx,mn,ans,map[111][111],f[111][111];
bool OK(int x,int y){
	int i,tmp=0;
	for(i=1;i<=N;++i)
		if(map[i][y]>=k){ ++tmp; break; }
	for(i=1;i<=M;++i)
		if(map[x][i]>=k){ ++tmp; break; }
	return (tmp==2?0:1);
}
int main(){
	ofstream cout ("B-large.out");
	ifstream cin ("B-large.in");
	cin >> T;
	for(Case=1;Case<=T;++Case){
		cin >> N >> M;
		memset(map,0,sizeof(map));
		mx=0; mn=101; ans=1;
		for(i=1;i<=N;++i)
		for(j=1;j<=M;++j){
			cin >> map[i][j];
			if(map[i][j]>mx) mx=map[i][j];
			if(map[i][j]<mn) mn=map[i][j];
		}
		for(k=mx;k>mn;--k){
			for(i=1;i<=N;++i)
			if(ans)
				for(j=1;j<=M;++j){
					if(map[i][j]<k&&!OK(i,j)){
						ans=0;
						break;
					}
				}
		}
		cout << "Case #" << Case << ": " << (ans?"YES":"NO") << endl;
	}
	return 0;
}
