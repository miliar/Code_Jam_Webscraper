#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1000000
#define MOD 1000000007  
#define f first
#define s second
#define EPS 1e-9
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
//#define DFS_WHITE -1
//#define DFS_BLACK 0

ii arr[255][255];
int n, x, L;
string str;

void solve() {
	set<ii> Set;
	ii p;
	p.f = 1;
	p.s = 1;
	Set.insert(p);
	loop(j,0,x){
		loop(i,0,L){
			int sign = p.s;
			p = arr[p.f][str[i]];
			p.s *= sign;
		}
		if(Set.find(p) != Set.end()){
			n = j+1;	// x
			return;
		}
		Set.insert(p);
	}
	n = x;
}


int main(){
	Rd;
	Wr;

	int T, c;
	sc(T);
	loop(t,0,T){
		printf("Case #%d: ", t+1);
		int x, r, c;
		sc(x); sc(r); sc(c);
		
		//printf("%d %d %d    ",  x, r, c);
		if( (r*c) % x != 0 ){
			printf("RICHARD\n");
		}
		else{
			bool ok = true;
			loop(h,1,x+1){
				int w = x-h+1;
				if( !(h <= r && w <= c) && !(h <= c && w <= r) ) {
					printf("RICHARD\n");
					ok = false;
					break;
				}
				if( x == 4 && ( r == 2 && c == 4 || r == 4 && c == 2 ) ){
					printf("RICHARD\n");
					ok = false;
					break;
				}
			}
			if(ok)
				printf("GABRIEL\n");
		}
	}
	return 0;
}