#include <cstdio>
#include <vector>
#include <utility>
#include <queue>
#include <functional>

using namespace std;

const int inf=1000000000;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ii,ii> block;

int dist(block a,block b);
int dist(ii a,ii b);

int main() {
	int cases;
	scanf("%d",&cases);
	for(int round=1; round<=cases; round++) {
		int n;
		int w,h;
		scanf("%d%d%d",&w,&h,&n);
		vector<block> data;
		data.resize(n);
		for(int i=0; i<n; i++) {
			block &a=data[i];
			scanf("%d%d%d%d",
				  &a.first.first,&a.second.first,
				  &a.first.second,&a.second.second);
		}
		vvi adjMat(n+2,vi(n+2));
		adjMat[n][n+1]=adjMat[n+1][n]=w;
		for(int i=0; i<n; i++) {
			adjMat[i][n]=adjMat[n][i]=data[i].first.first;
			adjMat[i][n+1]=adjMat[n+1][i]=w-data[i].first.second-1;
		}
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				adjMat[i][j]=dist(data[i],data[j]);
		priority_queue<ii,vector<ii>,greater<ii> > pq;
		pq.push(ii(0,n));
		vi dist(n+2,inf);
		while(!pq.empty()) {
			int x=pq.top().second;
			int len=pq.top().first;
			pq.pop();
			if(dist[x]!=inf)
				continue;
			dist[x]=len;
			for(int i=0; i<n+2; i++)
				pq.push(ii(len+adjMat[x][i],i));
		}
		printf("Case #%d: %d\n",round,dist[n+1]);
	}
	return 0;
}

int dist(block a,block b) {
	return max(dist(a.first,b.first),dist(a.second,b.second));
}

int dist(ii a,ii b) {
	if(a.first>b.second)
		return a.first-b.second-1;
	else if(a.second<b.first)
		return b.first-a.second-1;
	else
		return 0;
}

