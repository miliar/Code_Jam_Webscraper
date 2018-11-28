#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

ll S[1000005];
ll M[1000005];
vector<pair<int, int> > v;
bool on[1000005];
bool use[10000005];
vector<int> children[1000005];
int ans;
queue<int> q;

void down(int pos){
	if(!on[pos])
		return;
	if(!use[pos])++ans;
	use[pos]=1;
	rep(i,0,children[pos].size()){
		int to=children[pos][i];
		q.push(to);
	}
}

void downBad(int pos){
	if(!use[pos])
		return;
	--ans;
	use[pos]=0;
	rep(i,0,children[pos].size()){
		int to=children[pos][i];
		q.push(to);
	}
}

bool up(int pos){
	if(!pos)
		return on[pos];
	return use[M[pos]];
}

void turn(int pos, bool state){
	on[pos]=state;
	if(state == 0 && !use[pos])
		return;
	if(!state){
		if(use[pos])--ans;
		use[pos]=0;
	}
	if(!up(pos))
		return;
	if(state){
		++ans;
		use[pos]=1;
	}
	rep(i,0,children[pos].size()){
		int to=children[pos][i];
		q.push(to);
	}
	while(!q.empty()){
		int to=q.front();
		q.pop();
		if(state)down(to);
		else downBad(to);

	}
}

void solve(){
	int N, D;
	int As, Cs, Rs;
	int Am, Cm, Rm;
	ans=0;
	scanf("%d%d", &N, &D);
	scanf("%d%d%d%d", S, &As, &Cs, &Rs);
	scanf("%d%d%d%d", M, &Am, &Cm, &Rm);
	v.clear();
	rep(i,0,N){
		on[i]=0;
		use[i]=0;
		children[i].clear();
		S[i+1]=(S[i]*As+Cs)%Rs;
		M[i+1]=(M[i]*Am+Cm)%Rm;
		if(i)M[i]%=i;
		v.push_back(make_pair(S[i], i));//i?(M[i]%i):(-1)));
		if(i)
			children[M[i]%i].push_back(i);
	}
	sort(v.begin(), v.end());
	int p1=0, p2=0;
	int best=0;
	while(p2 < N){
		while(p2 < N && v[p2].first-v[p1].first <= D){
			turn(v[p2].second, 1);
			++p2;
		}
		if(v[p1].first <= S[0] && (p2 == N || S[0] < v[p2].first))
			best=max(ans, best);
		turn(v[p1].second, 0);
		++p1;
	}
	printf("%d\n", best);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		cerr << t << endl;
		printf("Case #%d: ", t);
		solve();
	}
}
