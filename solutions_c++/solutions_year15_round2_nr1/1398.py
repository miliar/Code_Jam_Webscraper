#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

int visited[10000000];

int reverse(int n)
{
	int ret = 0;
	while(n>0){
		ret = 10*ret+(n%10);
		n/=10;
	}
	return ret;
}

int bfs(int N)
{
	if(N==1)
		return 1;
	queue<pair<int,int>> Q;
	Q.push({1,1});
	visited[1]=1;
	while(!Q.empty()) {
		auto u = Q.front();
		Q.pop();
		int v = reverse(u.first);
		int w = u.first+1;
		if(v==N||w==N)
			return u.second+1;
		if((!visited[w])&&(w<10000000)){
			Q.push({w,u.second+1});
			visited[w]=1;
		}
		if(!visited[v]){
			Q.push({v,u.second+1});
			visited[v]=1;
		}
	}
}

int main()
{
	int N,t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		cin>>N;
		memset(visited,0,sizeof(visited));
		int ans = bfs(N);
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}