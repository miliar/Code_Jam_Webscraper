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

int R, C;
int field[10][10];
int dx[4]={1,0,-1,0}, dy[4]={0,1,0,-1};
int tot;

struct Drum{
	int f[10][10];

	bool operator<(Drum other){
		rep(i,0,R)
			rep(j,0,C){
				if(f[i][j] != other.f[i][j])
					return f[i][j] < other.f[i][j];
			}
		return 0;
	}
};

Drum rotate(Drum d){
	Drum ret;
	rep(i,0,R)
		rep(j,0,C){
			ret.f[i][j]=d.f[i][(j+1)%C];
		}
	return ret;
}

bool check(int r, int c){
	c%=C;
	if(c < 0)c += C;
	if(field[r][c] == -1)
		return 1;
	int num=0;
	rep(i,0,4){
		int x=r+dx[i];
		int y=c+dy[i];
		y %= C;
		if(y < 0)
			y += C;
		if(x < 0 || x >= R)
			continue;
		if(field[x][y] == -1)
			return 1;
		if(field[x][y] == field[r][c])++num;
	}
	return num == field[r][c];
}

void rec(int r, int c){
	if(c == C){
		rec(r+1,0);
		return;
	}
	if(r == R){
		bool ok=1;
		rep(j,0,R)
			rep(k,0,C)
				if(!check(j,k))
					ok=0;
		Drum d;
		rep(j,0,R)
			rep(k,0,C)
			d.f[j][k]=field[j][k];
		Drum cur=d;
		rep(j,0,C){
			cur=rotate(cur);
			if(cur < d)
				ok=0;
		}
		if(ok)
			++tot;
		/*printf("%d\n", int(ok));
		rep(i,0,R){
			rep(j,0,C)
				printf("%d ", field[i][j]);
			printf("\n");
		}
		printf("\n");*/
		return;
	}
	for(int i=1; i <= 4; ++i){
		field[r][c]=i;
		bool ok=1;
		rep(j,0,R)
			rep(k,0,C)
				if(!check(j,k))
					ok=0;
		if(!ok)
			continue;
		rec(r,c+1);
	}
	field[r][c]=-1;
}

void solve(){
	tot=0;
	scanf("%d%d", &R, &C);
	rep(i,0,R)
		rep(j,0,C)
			field[i][j]=-1;
	rec(0,0);
	printf("%d\n", tot);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
