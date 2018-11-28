#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;
int T;

int N;
vector<int> V[100000];
int P;

void solve(int num) {
	int sol = 1<<23;
	map<string,int> M;
	REP(p,10000) V[p].clear();
	P = 0;
	scanf("%d", &N);
	REP(n,N) {
		char S[100000];
		scanf(" %[^\n] ", S);
		//printf("-%s-\n", S);
		int i = 0;
		while (S[i] != '\0') {
		string s;
		while (S[i] != ' ' && S[i] != '\0') {
			s.push_back(S[i]); i++;
		}
		if (S[i] == '\0') S[i+1] = '\0';
		if (M.find(s) == M.end()) {
			//printf("%s\n", s.c_str());
			M[s] = P;
			P++;
		}
		V[M[s]].push_back(n-2);
		i++;
		}
	}
	for (int c = 0; c < (1<<(N-2)); c++) {
		int val = 0;
		REP(p,P) {
		bool eng = false, french = false;
		//printf("\n %d:", p);
		for (auto x:V[p]) {
			//printf(" %d ", x);
			if (x == - 2) eng = true;
			else if (x == - 1) french = true;
			else { 
				if (c & (1<<x)) {
					eng = true;}
				else french = true;
			}
		}
		if (french && eng) val++;
		}
		sol = min(sol,val);
	}
	printf("Case #%d: %d\n", num, sol);
	return;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		solve(t+1);
	}
	return 0;
}
