#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

const int MAX = 50;

bool poss[MAX];
int C, D, V;
VI coins;

int main(){
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	FOR(cnt,0,T){
		fill(poss, poss+MAX, false);
		poss[0] = 1;
		cin >> C >> D >> V;
		coins.resize(D);
		FOR(i,0,D)
			cin >> coins[i];
		FOR(i,0,D) ROF(x,coins[i],V+1) if(poss[x-coins[i]])
			poss[x] = true;
		int ans = 0;
		do{
			int c = 1;
			while(c <= V && poss[c])
				c++;
			if(c > V)
				break;
			ans++;
			ROF(x,c,V+1) if(poss[x-c])
				poss[x] = 1;
		}while(1);
		cout << "Case #" << cnt+1 << ": " << ans << endl;
	}

	return 0;
}
