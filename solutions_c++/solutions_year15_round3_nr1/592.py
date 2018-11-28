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

const int MAX = 100000;
int is[MAX], nis[MAX];

int main(){
	ios_base::sync_with_stdio(false);
	int T, R, C, W;
	cin >> T;
	FOR(cnt,0,T){
		cin >> R >> C >> W;
		FOR(i,0,W){
			is[i] = -MAX;
			nis[i] = 0;
		}
		nis[W] = 1;
		is[W] = W;
		FOR(l,W+1,C+1){
			is[l] = 1+max(W-1,is[l-1]);
			nis[l] = 1+nis[l-1];
			FOR(i,1,l){
				is[l] = min(is[l], max(W+1,1+max(nis[i]+is[l-i-1], is[i]+nis[l-i-1])));
				nis[l] = min(nis[l], 1+nis[i]+nis[l-i-1]);
			}
		}
		cout << "Case #" << cnt+1 << ": " << (R-1)*nis[C] + is[C] << endl;
	}

	return 0;
}
