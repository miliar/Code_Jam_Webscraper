#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
#define INF 500
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int r,c,w;
int v[30];
int pd[11][11][100000];

int conv(){ 
	int ret = 0;
	int mult =1;
	for(int i=0;i<c;i++){
		ret += (v[i]+1)*mult;
		mult*=3;
	}
	return ret;
}

int solve(int q, int q1) {
	int nmin = INF;
	int check = conv();
	if(pd[q][q1][check]!=-1)return pd[q][q1][check];
	if(q1==w) {
		int cnt=0, esp=0;
		for(int i=0;i<c;i++) {
			if(v[i]==0) {
				cnt = 0;
			} else{
				cnt++;
				if(cnt >= w) {
					esp++;
				}
			}
		}
		int ret = (esp == 1) ? 0 : INF;
		return pd[q][q1][check] = ret;
	}
	for(int i=0;i<c;i++) {
		if(v[i]== -1) {
			int nmax = -1;
			v[i] = 0;
			int x = solve(q+1, q1);
			if (x != INF) 
				nmax = x;
			v[i] = 1;
			int y = solve(q+1, q1+1);
			if (y != INF && y  > nmax) 
				nmax = y;
			v[i]=-1;
			if (nmax != -1 && nmin > nmax + 1 ) {
				nmin = nmax + 1;
			}
		}
	}
	return pd[q][q1][check] = nmin;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		scanf("%d %d %d",&r,&c,&w);
		/*
		memset(v,-1,sizeof(v));
		memset(pd,-1,sizeof(pd));
		printf("Case #%d: %d\n",caso, solve(0,0));
		*/
		printf("Case #%d: %d\n",caso, (c+w-1)/w + w-1);
	}
	return 0;
}
