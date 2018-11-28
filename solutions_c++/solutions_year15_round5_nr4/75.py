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

ll e[10005], f[10005];
map<int, int> M;
vector<int> ans;

void removeE(int val){
	//printf("val = %d\n", val);
	ans.push_back(val);
	if(val == 0){
		for(auto it=M.begin(); it != M.end(); ++it)
			it->second /= 2;
		return;
	}
	if(val > 0){
		map<int, int> m=M;
		for(auto it=M.begin(); it != M.end(); ++it){
			m[it->first+val]=m[it->first+val]-m[it->first];
		}
		M.clear();
		for(auto it=m.begin(); it != m.end(); ++it)
			if(it->second){
				M[it->first]=it->second;
				//printf("M[%d]=%d\n", it->first, it->second);
			}
		return;
	}
	map<int, int> m=M;
	for(auto it=M.rbegin(); it != M.rend(); ++it){
		m[it->first+val]=m[it->first+val]-m[it->first];
	}
	M.clear();
	for(auto it=m.rbegin(); it != m.rend(); ++it)
		if(it->second){
			M[it->first]=it->second;
			//printf("M[%d]=%d\n", it->first, it->second);
		}
}

void solve(){
	ans.clear();
	int P;
	scanf("%d", &P);
	rep(i,0,P){
		scanf("%lld", e+i);
	}
	rep(i,0,P){
		scanf("%lld", f+i);
		M[e[i]]=f[i];
	}
	while(true){
		auto it=M.begin();
		auto it2=M.begin();
		++it2;
		if(it->second > 1)
			removeE(0);
		else if(it2 == M.end()){
			break;
		}
		else if(it->first < 0){
			removeE(it->first-it2->first);
		}
		else{
			it=M.end();
			--it;
			it2=it;
			--it2;
			if(it->second > 1)
				removeE(0);
			else{
				removeE(it->first-it2->first);
			}
		}
	}
	sort(ans.begin(), ans.end());
	for(int i=0; i < ans.size(); ++i)
		printf("%d ", ans[i]);
	printf("\n");
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
