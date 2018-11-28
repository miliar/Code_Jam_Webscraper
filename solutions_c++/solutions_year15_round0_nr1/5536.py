#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
int shy[1005], N;
int main() {
	//freopen("a.in", "r", stdin); 
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	//freopen("A-small-attempt3.in", "r", stdin); freopen("A-small-attempt3.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
    string str;
    cin>>N>>str;
    for (int i = 0; i < N; i ++) {
      shy[i] = str[i] - '0';
    }
    int tot = shy[0], ret = 0;
    for (int i = 1; i <= N; i ++) {
      if (tot < i) {
        ret += i - tot;
        tot = i;
      }
      tot += shy[i];
    }
		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}
