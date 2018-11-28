// TwT514 {{{
#include <bits/stdc++.h>
#define SZ(x) ((int)(x).size())
#define FOR(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define REP(i,n) for (int i=0; i<(n); i++)
#define REP1(i,a,b) for (int i=(int)(a); i<=(int)(b); i++)
#define ALL(x) (x).begin(),(x).end()
#define MS0(x,n) memset(x,0,(n)*sizeof(*x))
#define MS1(x,n) memset(x,-1,(n)*sizeof(*x))
#define MP make_pair
#define PB push_back
#define RI(a) scanf("%d",&(a))
#define RII(a,b) scanf("%d%d",&(a),&(b))
#define RIII(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
// }}}
#define N 55
int r,c,m, rem, sp;
char mp[N][N];

void input(){
	RIII(r,c,m);
	rem = r*c-m;
}

void print(){
	if(sp){
		REP(j,c){
			REP(i,r) printf("%c", mp[i][j]);
			puts("");
		}
	}	
	else{
		REP(i,r) {
			REP(j,c) printf("%c", mp[i][j]);
			puts("");
		}
	}
}
char impos[] = "Impossible";

void solve1(){
	for(int i=0; i<c; i++) mp[0][i] = '*';
	for(int i=0; i<rem;i++) mp[0][i] = '.';
	mp[0][0] = 'c';
	print();
}

void solve2(){
	if(rem==1){
		for(int i=0; i<c; i++) mp[0][i] = mp[1][i] = '*';
		mp[0][0] = 'c';
		return print();
	}
	if(rem%2 || rem==2){
		puts(impos);
		return;
	}
	for(int i=0; i<c; i++) mp[0][i] = mp[1][i] = '*';
	for(int i=0; i<rem/2; i++) mp[0][i] = mp[1][i] = '.';
	mp[0][0] = 'c';
	print();
}


void solve(){
	static int zi=0;
	printf("Case #%d:\n", ++zi);
	if(r>c){
		swap(r,c); sp = 1;
	}
	else sp = 0;
	if(r==1) solve1();
	else if(r==2) solve2();
	else{
		REP(i,r) REP(j,c) mp[i][j] = '*';
		if(rem==1){
			mp[0][0] = 'c';
			return print();
		}
		else if(rem==2 || rem==3 || rem==5 || rem==7){
			puts(impos);
		}
		else if(rem==4){
			REP(i,2) REP(j,2) mp[i][j] = '.';
			mp[0][0] = 'c';
			return print();
		}
		else if(rem==6){
			REP(i,2) REP(j,3) mp[i][j] = '.';
			mp[0][0] = 'c';
			return print();
		}
		else if(rem <= 3*r){
			int k = rem/3;
			REP(i,k) REP(j,3) mp[i][j] = '.';
			if(rem%3==1){
				mp[k][0] = mp[k][1] = '.';
				mp[k-1][2] = '*';
			}
			else if(rem%3==2){
				mp[k][0] = mp[k][1] = '.';
			}
			mp[0][0] = 'c';
			return print();
		}
		else{
			int k = rem/r, qq = rem%r;
			REP(i,r) REP(j,k) mp[i][j] = '.';
			REP(j,qq) mp[j][k] = '.';
			if(qq==1){
				mp[1][k] = '.';
				mp[r-1][k-1] = '*';
			}
			mp[0][0] = 'c';
			return print();
		}
	}
}

int main() {
	int zn;
	RI(zn);
	while(zn--){
		input();
		solve();
	}
    return 0;
}

