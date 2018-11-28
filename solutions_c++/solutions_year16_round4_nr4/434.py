#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "cstring"
#include "cmath"
#include "algorithm"
#include "set"
#include "map"
#include "queue"
#include "vector"
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repp(i,a,b) for(int i=a; i<a+b; ++i)
#define sz size()
#define X first
#define Y second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int,int> pii;
#define maxn 405

char s[5][5];
int id[5][5];
std::vector<int> v;
int a[5], avis[5];
int b[5], bvis[5];
int n;

bool zuo(int u){
	printf("b %d\n", u);
	if(u==n){
		rep(i,n) printf("%d ", b[i]); printf(" bb\n");
		return 1;
	}
	int cnt = 0;
	rep(i,n){
		if(bvis[i] || s[a[u]][i]=='0') continue;
		cnt++;
		b[u] = i; bvis[i] = 1;
		if(zuo(u+1)==0) return 0;
		bvis[i] = 0;
	}
	if(cnt==0) return 0;
	return 1;
}

bool ren(int u){
	printf("a %d\n", u);
	if(u==n){
		rep(i,n) printf("%d ", a[i]); printf(" aa\n");
		memset(bvis, 0, sizeof bvis);
		if(zuo(0)){
			return 1;
		}
		return 0;
	}
	rep(i,n){
		if(!avis[i]){
			a[u] = i; avis[i] = 1;
			if(ren(u+1)) return 1;
			avis[i] = 0;
		}
	}
	return 0;
}

void run(){
	cin >> n;
	v.clear();
	rep(i,n) scanf("%s", s[i]);
	int u = 0;
	rep(i,n)rep(j,n){
		id[i][j] = u;
		if(s[i][j]=='0') v.pb(u);
		u++;
	}
	rep(i,u) printf("%d ", v[i]);
	int ans = n*n;
	rep(st,1<<u){
		int cnt = 0;
		rep(i, u) if((st>>i)&1){
			int x = v[i]/n, y = v[i]%n;
			s[x][y] = '1';			
			cnt++;
		}
		if(ren(0)) ans = min(ans, cnt);
		rep(i, u){
			int x = v[i]/n, y = v[i]%n;
			s[x][y] = '0';
		}
	}
}
int main(int argc, char const *argv[])
{
	int cas;
	cin >> cas;
	rep(ca,cas){
		printf("Case #%d: ", ca+1);
		run();
	}
	return 0;
}