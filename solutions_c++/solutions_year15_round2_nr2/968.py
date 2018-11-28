#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(auto i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout11.h"

int solve(int R, int C, int N){
	int M = 1<<(R*C);
	int score = R*C*4;
	for (int p=0; p<M; ++p) {
		if (__builtin_popcount(p) != N) continue;
		int s = 0;
		//printf("pattern %d\n", p);
		rep(r,R) {
			rep(c,C) {
				int i=r*C+c;
				if (!(p & (1<<i))) continue;
				//printf("(%d/%d %d/%d)..\n", r,R, c,C);
				if (r < R-1){
					int j=i+C;
					//printf("v %d %d\n", i,j);
					if (p & (1<<j)) ++s;
				}
				if (c < C-1){
					int j=i+1;
					//printf("> %d %d\n", i,j);
					if (p & (1<<j)) ++s;
				}
			}
		}
		//printf("s=%d\n", s);
		score = min(score, s);
	}
	return score;
}

int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
  	int R,C,N; cin >> R>>C>>N;
  	// 1 <= N <= R*C <= 16,10000
    ;;
 answer:
    cout << "Case #" << _t << ": " << solve(R,C,N) << endl;
  }
}
