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

#define MAXN 10005

using namespace std;

int T,N,X;
int S[MAXN];

int main(){	
	scanf("%d", &T);
	REP(jt,T){
		scanf("%d%d", &N, &X);
		REP(i,N){
			scanf("%d", &S[i]);
		}

		sort(S, S + N);

		int tot = 0;
		int p1 = 0;
		int p2 = N-1;
		while (p1 <= p2){
			if (S[p1] + S[p2] <= X){
				p1++;
				p2--;
			}else{
				p2--;
			}
			tot++;
		}

		printf("Case #%d: %d\n", jt+1, tot);
	}	
}
