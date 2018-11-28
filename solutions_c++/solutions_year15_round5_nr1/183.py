#include<stack>
#include<queue>
#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)
#define eprintf(s...) fprintf(stderr, s)

template<class T> inline void amin(T &a, const T &b) { if (b<a) a=b; }
template<class T> inline void amax(T &a, const T &b) { if (a<b) a=b; }

int N, D;
int S[1000011], M[1000011];

void READ(int S[]) {
    LL A, C, R;
    scanf("%d%lld%lld%lld", S, &A, &C, &R);
    REP (i, N-1) S[i+1] = (S[i] * A + C) % R;
}


typedef vector<VI> Adj;
Adj G;
bool use[1000011];
int cnt;

void del(int v) {
    stack<int> X; X.push(v);
    while (X.size()) {
	int v = X.top(); X.pop();
	if (use[v]) {
	    use[v] = false;
	    cnt--;
	    for (int w : G[v]) X.push(w);
	}
    }
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	scanf("%d%d", &N, &D);
	REP (i, N+5) use[i] = false;

	READ(S);
	READ(M);

	G = Adj(N);
	for (int i=1; i<N; i++) {
	    M[i] %= i;
	    G[M[i]].push_back(i);
	}

	M[0] = N; 
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > Q, X;
	use[0] = true;
	cnt = 1;
	for (int w : G[0]) Q.push(make_pair(S[w], w));
	
	int ans = 1;
	
	for (int lo=S[0]-D, hi=S[0]; lo<=S[0]; lo++, hi++) {
	    while (!Q.empty()) {
		pair<int, int> p = Q.top(); Q.pop();
		if (p.first < lo || !use[M[p.second]]) continue;
		if (p.first > hi) {
		    Q.push(p);
		    break;
		}

		use[p.second] = true;
		X.push(p);
		cnt++;
		for (int c : G[p.second]) {
		    Q.push(make_pair(S[c], c));
		}
	    }

//	    eprintf("%d [%d %d]- \n", cnt, lo, hi);
	    while (!X.empty()) {
		pair<int, int> p = X.top(); X.pop();
		if (!use[p.second]) continue;
		if (p.first < lo) {
		    del(p.second);
		} else {
		    X.push(p);
		    break;
		}
	    }

	    amax(ans, cnt);
	}
	printf("Case #%d: ", tc);
	printf("%d\n", ans);
	
    }
    return 0;
}
