#include <cmath>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <deque>
#include <queue>
#include <functional>
#include <map>
#include <bitset>
#include <stack>
#include <set>
#include <string>
using namespace std;
#define fr(a,b,c) for(int a=b;a<c;a++)
#define addEdge(a,b) to[z] = b; ant[z] = adj[a]; adj[a] = z++
#define addEdgeC(a,b,c) from[z] = a; to[z] = b; ant[z] = adj[a]; adj[a] = z; cost[z] = c; edges[z] = z; z++;
#define rp(a,b) fr(a,0,b)
#define MP make_pair
#define F first
#define S second
#define PI acos(-1)
const int infinity = 0x3f3f3f3f;
const long long longInfinity = 0x3f3f3f3f3f3f3f3fLL;
typedef pair<int,int> pii;
typedef pair<pii,int> trii;
typedef long long ll;
typedef priority_queue<pii, vector<pii>, greater<pii> > HeapPii;

int T,N;
char A[2000];

int aller(){
	int upUntilNow = A[0] - '0';
	int extra = 0;
	fr(i,1,N+1){
		if(i - upUntilNow > 0){
			extra += (i - upUntilNow);
			upUntilNow += (i - upUntilNow);
		}
		upUntilNow += (A[i] - '0');
	}
	return extra;
}

int main(){
	scanf("%d",&T);
	rp(t,T){
		scanf("%d",&N);
		scanf("%s",A);
		printf("Case #%d: %d\n",t+1,aller());
	}
}

























