#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

bool rec(vector<string> &g, int n, int d, int s){
	if(d==n) return true;
	bool ex = false;
	for(int i = 0; i < n; i++){
		if(1&(s>>i)) continue;
		if(g[d][i]=='1'){
			ex = true;
			if(!rec(g, n, d+1, s|(1<<i))) return false;
		}
	}
	return ex;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n;
		cin>>n;
		int nn = n*n;
		vector<string> g(n);
		for(int i = 0; i < n; i++) cin>>g[i];
		int res = n*n;
		for(int i = 0; i < 1<<nn; i++){
			vector<string> g2(g);
			bool cont = false;
			for(int j = 0; j < nn; j++){
				if(!(1&(i>>j))) continue;
				if(g[j/n][j%n]=='1'){
					cont = true;
					break;
				}
				g2[j/n][j%n] = '1';
			}
			if(cont) continue;
			int r = __builtin_popcount(i);
			if(r>=res) continue;
			bool ok = true;
			sort(g2.begin(), g2.end());
			do{
				ok &= rec(g2, n, 0, 0);
			}while(next_permutation(g2.begin(), g2.end()));
			if(ok){
				res = r;
				//cerr<<r<<endl;
				//for(int k = 0; k < n; k++) cerr<<g2[k]<<endl;
			}
		}
		printf("Case #%d: %d\n", Case, res);
	}
	return 0;
}

