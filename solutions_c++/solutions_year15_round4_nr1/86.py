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

char field[105][105];
int change[105][105];
int dx[4]={1,0,-1,0}, dy[4]={0,1,0,-1};

void solve(){
	int R, C;
	scanf("%d%d", &R, &C);
	rep(i,0,R){
		scanf("%s", field[i]);
		rep(j,0,C)
			change[i][j]=0;
	}
	int ans=0;
	rep(k,0,4){
		for(int i=0; true; ++i){
			if(k%2 && i >= R)
				break;
			if(k%2 == 0 && i >= C)
				break;
			int x=0, y=0;
			if(k == 0)
				y=i;
			else if(k == 1)
				x=i;
			else if(k == 2){
				y=i;
				x=R-1;
			}
			else{
				x=i;
				y=C-1;
			}
			while(x >= 0 && y >= 0 && x < R && y < C){
				if(field[x][y] != '.'){
					char c=field[x][y];
					++change[x][y];
					if(k == 0 && c == '^'){
						++ans;
					}
					if(k == 1 && c == '<'){
						++ans;
					}
					if(k == 2 && c == 'v'){
						++ans;
					}
					if(k == 3 && c == '>'){
						++ans;
					}
					if(change[x][y] == 4){
						puts("IMPOSSIBLE");
						return;
					}
					break;
				}
				x += dx[k];
				y += dy[k];
			}
		}
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
