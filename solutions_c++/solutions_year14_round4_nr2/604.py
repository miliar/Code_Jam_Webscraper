#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <set>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FOR(a,b,c) for (int a = b; a <= c; a++)
#define RESET(a,b) memset(a,b,sizeof a)

#define PB push_back
#define PII pair<int,int>
#define MP make_pair
#define F first
#define S second

#define EPS 1e-8
#define INF 1023123123
#define LL long long
#define __ puts("")

#define MAXN 1005

using namespace std;

int T,N;
int S[MAXN];
int ar[MAXN];
int dp[MAXN][MAXN];
map<int,int> di;

int cost(int a, int b){
	return abs(a - b);
}

int rek(int ki, int ka){
//	printf("%d %d\n", ki, ka);
	int id = ki + (N-1 - ka);

	if (ki >= ka){
		return 0;
	}else{
		int ret = 0;

		int pos = -1;
		FOR(i,ki,ka){
			if (ar[id] == S[i]){
				pos = i;
				break;
			}
		}

		if (abs(pos - ki) < abs(pos - ka)){
			// bubble left
			while (pos != ki){
				swap(S[pos], S[pos-1]);
				ret++;
				pos--;
			}

			return ret + rek(ki+1, ka);
		}else{
			// bubble right
			while (pos != ka){
				swap(S[pos], S[pos+1]);
				ret++;
				pos++;
			}
			return ret + rek(ki, ka-1);
		}
	}
}

int main(){	
	scanf("%d", &T);
	REP(jt,T){
		di.clear();

		scanf("%d", &N);
		REP(i,N){
			scanf("%d", &ar[i]);
			S[i] = ar[i];
		}

		sort(ar, ar + N);

		printf("Case #%d: %d\n", jt+1, rek(0,N-1));
	}	
}
