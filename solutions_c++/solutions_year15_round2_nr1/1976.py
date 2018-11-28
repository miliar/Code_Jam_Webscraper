#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <climits>
#include <utility>
#include <map>
#include <sstream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <string>
#include <bitset>

#define fore(i,n) for(int i=0;i<n;i++)
#define fori(i,n) for(int i=0;i<=n;i++)
#define all(v) v.begin(),v.end()

#define T 10000005
#define M 1000005

using namespace std;

int reverse(int i) {
	int e=1;
	int res = 0;
	int tmp= i;
	while(i) {
		e*=10;
		i/=10;
	}
	e/=10;
	while(tmp) {
		res += (tmp%10) * e;
		e/=10;
		tmp/=10;	
	}
	return res;

}

long long dist[T];
bool visit[T];
vector<vector<int> > graph;
void BFS(int s) {
	
	memset(dist,T,sizeof(dist));
	memset(visit,false,sizeof(visit));
	
	int u,v,cantidadVecinos;
	queue<int> Q;
	visit[s] = 1;
	dist[s] = 0;
	Q.push(s);
	while(!Q.empty())
	{
		u = Q.front();
		Q.pop();
		cantidadVecinos = graph[u].size();
		for(int i=0;i<cantidadVecinos;i++)
		{
			v = graph[u][i];
			if(visit[v] == 0)
			{
				visit[v] = 1;
				dist[v] = dist[u] + 1;
				Q.push(v);
			}
		}
	}


}
int main()
{
	
	graph.resize(M);
	fore(i,M) {
		graph[i].push_back(i+1);
		int tmp = reverse(i);
		if(tmp!=i && tmp<M)
			graph[i].push_back(tmp);
	}
	BFS(1);
	int test,caso=0,n;
	scanf("%d",&test);
	while(test--) {
		cin >> n;
		
		printf("Case #%d: %lld\n",++caso,dist[n]+1);
	
	}
}	


