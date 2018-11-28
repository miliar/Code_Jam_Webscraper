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

vector<int> words[25];
int M[1000005];
map<string, int> toInd;

void solve(){
	int N;
	scanf("%d", &N);
	string s;
	getline(cin, s);
	int wordN=0;
	toInd.clear();
	rep(i,0,N){
		words[i].clear();
		getline(cin, s);
		string t;
		for(int j=0; j <= s.size(); ++j){
			if(j == s.size() || s[j] == ' '){
				if(toInd.find(t) == toInd.end()){
					toInd[t]=wordN++;
				}
				words[i].push_back(toInd[t]);
				t.clear();
				continue;
			}
			t.push_back(s[j]);
		}
	}
	int ans=999999999;
	for(int i=0; i < (1<<N); ++i){
		if((i&1) || !(i&2))
			continue;
		for(int j=0; j < wordN; ++j)
			M[j]=0;
		for(int j=0; j < N; ++j)
			for(int k=0; k < words[j].size(); ++k){
				if(i&(1<<j))
					M[words[j][k]] |= 1;
				else 
					M[words[j][k]] |= 2;
			}
		int val=0;
		for(int j=0; j < wordN; ++j)
			if(M[j] == 3)
				++val;
		ans=min(ans, val);
	}
	printf("%d\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
