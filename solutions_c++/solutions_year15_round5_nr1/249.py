
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;
long long S[1010];
long long M[1010];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	int N,D;
	long long As, Cs,Rs;
	long long Am, Cm,Rm;

	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> N >> D;
		cin >> S[0] >> As >> Cs >> Rs;
		cin >> M[0] >> Am >> Cm >> Rm;
		vector<vector<int> > G;
		G.resize(N+1);
		for(int i=1;i<N;i++){
			S[i] = (S[i-1]*As + Cs) % Rs;
			M[i] = (M[i-1]*Am + Cm) % Rm;
		}
		for(long long i=1;i<N;i++) G[M[i]%i].push_back(i);

		long long mm;

		int ans = 1;

		for(int i=0;i<=1000;i++){
			mm= i;
			queue<int > que;
			int k=1;
			if(mm <= S[0] && S[0] <= mm + D) que.push(0);
			while(!que.empty()){
				int x= que.front();
				que.pop();

				for(int j=0;j<G[x].size();j++){
					if(S[G[x][j]] < mm || S[G[x][j]] > mm + D ){
						continue;
					}
					que.push(G[x][j]);
					k++;
				}
			}
			ans = max(ans,k);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}