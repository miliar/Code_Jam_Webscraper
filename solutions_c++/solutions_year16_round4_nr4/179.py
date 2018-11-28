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

char f[30][30];
int N;
bool used[30];
bool personUsed[30];

bool checkOk(){
	bool ok=1;
	rep(i,0,N){
		if(personUsed[i])
			continue;
		personUsed[i]=true;
		bool any=0;
	rep(j,0,N){
		if(f[i][j] == '0')
			continue;
		if(used[j])
			continue;
		any=1;
		used[j]=1;
		bool res=checkOk();
		used[j]=0;
		if(!res){
			ok=0;
			break;
		}
	}
		personUsed[i]=false;
		if(!any)
			return 0;
	}
	return ok;
}

int bruteforce(int x, int y){
	if(x == N)
		return checkOk()?0:1000000;
	if(y == N)
		return bruteforce(x+1,0);
	int best=1000000;
	if(f[x][y] == '0'){
		f[x][y]='1';
		best=min(best, bruteforce(x, y+1)+1);
		f[x][y]='0';
	}
	best=min(best, bruteforce(x, y+1));
	return best;
}

void solve(){
	scanf("%d", &N);
	rep(i,0,N)
		scanf("%s", f[i]);
	int ans=bruteforce(0,0);
	printf("%d\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
