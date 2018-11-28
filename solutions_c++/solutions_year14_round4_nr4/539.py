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
#define MOD 1000000007

using namespace std;

int T,M,N;
string S[10];

int cnt;
int FULL;
int dp1[1<<8][5];
int dp2[1<<8][5];

struct node
{
	node* next[256];

	node(){
		REP(i,256){
			next[i] = 0;
		}
	}
};

void insert(node* &t, string s, int id){
	if (id == s.length()) return;

	if (t->next[s[id]] == 0){
		t->next[s[id]] = new node();
		cnt++;
	}

	insert(t->next[s[id]], s, id+1);
}

void destroy(node* &t){
	REP(i,256){
		if (t->next[i] != 0){
			destroy(t->next[i]);
		}
	}

	delete t;
}

int cost(int mas){
	node* root = new node();
	cnt = 1;

	REP(i,M){
		if (mas & (1<<i)){
			insert(root, S[i], 0);
		}
	}

	destroy(root);

	return cnt;
}

int rek1(int mas, int d){
	if (mas == 0){
		return 0;
	}else if (dp1[mas][d] != -1){
		return dp1[mas][d];
	}else if (d == 1){
		dp1[mas][d] = cost(mas);
		return dp1[mas][d];
	}else{
		dp1[mas][d] = 0;

		REP(i,M){
			if (mas & (1<<i)){
				// coba semua subset
				int tau = mas ^ (1<<i);
				int t = tau;
				while (1){
					int tgt = t|(1<<i);
					dp1[mas][d] = max(dp1[mas][d], cost(tgt) + rek1(mas ^ tgt, d-1));

					if (t == 0) break;
					t = (t-1) & tau;
				}
				break;
			}
		}


		return dp1[mas][d];
	}
}

int rek2(int mas, int d){
	if (mas == 0){
		return 1;
	}else if (dp2[mas][d] != -1){
		return dp2[mas][d];
	}else if (d == 1){
		if (cost(mas) == rek1(mas,d)){
			return 1;
		}else{
			return 0;
		}
	}else{
		dp2[mas][d] = 0;

		REP(i,M){
			if (mas & (1<<i)){
				// coba semua subset
				int tau = mas ^ (1<<i);
				int t = tau;			
				while (1){
					int tgt = t|(1<<i);
					
					if (rek1(mas,d) == cost(tgt) + rek1(mas ^ tgt, d-1)){
						dp2[mas][d] += rek2(mas^tgt, d-1);
						dp2[mas][d] %= MOD;
					}

					if (t == 0) break;
					t = (t-1) & tau;
				}
				break;
			}
		}

		return dp2[mas][d];
	}
}

int main(){	
	scanf("%d", &T);
	REP(jt,T){
		scanf("%d%d", &M, &N);
		REP(i,M){
			char sc[100];
			scanf("%s", sc);
			S[i] = sc;
		}

		RESET(dp1,-1);
		RESET(dp2,-1);			

		FULL = (1 << M) - 1;
		int maks = rek1(FULL, N);
		int tot = rek2(FULL, N);

		LL way = tot;
		FOR(i,2,N){
			way = (i * way) % MOD;
		}

		printf("Case #%d: %d %lld\n", 1+jt, maks, way);
	}	
}
