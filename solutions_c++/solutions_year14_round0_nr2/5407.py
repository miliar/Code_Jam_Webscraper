#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cout << __LINE__ << ' ' << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

//ハマったらチェックリスト見ろ!!

int main(){
	int T;
	cin >> T;
	rep(tc, T){
		cout << "Case #" << tc+1<<": ";
		double cost, f, goal;
		double nowf = 2.0, now = 0;
		cin >> cost >> f >> goal;
		double nowAns = goal/nowf;
		while(1){
			double next = cost/nowf;
			double nextA = next + now + goal/(nowf+f);
			if(nextA >= nowAns)break;
			nowAns = nextA;
			now += next;
			nowf += f;
		}
		printf("%.9f\n", nowAns);
	}
	
  return 0;
}
