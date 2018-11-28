#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 10005

int N,X;
int x[MAXN];
bool v[MAXN];
int main(){
	int cs;
	cin >> cs;
	REP(csn,1,cs+1){
		printf("Case #%d: ", csn);
		cin >> N >> X;
		REP(i,0,N){
			scanf("%d", x+i);
		}
		sort(x,x+N, greater<int>());
		FILL(v,0);
		int ans = 0;
		REP(j,0,N){
			if(v[j]) continue;
			int x1 = x[j];
			v[j] = 1;
			ans ++;
			int x2 = X-x1;
			REP(i,j+1,N){
				if(!v[i] && x[i]<=x2){
					v[i] = 1;
					break;
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}