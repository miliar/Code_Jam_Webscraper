//
//#tag
//#sol

#include <bits/stdc++.h>


// #include <unordered_map>

#define ll long long
#define ull unsigned long long
#define PII pair<int,int>
#define PDD pair<double,double>
#define FT first
#define SD second
#define REP(i,j,k) for(int (i)=(j);(i)<(k);++(i))
#define PB push_back
#define PI acos(-1)
#define DB(x) cerr << #x << " = " << x << endl;
#define _ << ", " << 
#define MP make_pair
#define EPS 1e-9
#define INF 0x3f3f3f3f
#define IOFAST() ios_base::sync_with_stdio(0);cin.tie(0)
#define FILL(x,v) memset(x,v,sizeof(x))
// #define umap unordered_map

using namespace std;

template <class _T> inline string tostr(const _T& a){ ostringstream os(""); os<<a;return os.str(); }

const int maxn = 200;

int dx[] = {0,1,0,-1};
int dy[] = {-1,0,1,0};

char in[maxn][maxn];
int mark[maxn][maxn];
int fix[maxn][maxn];

int main(){
	
	int K; cin >> K;
	REP(cn,1,K+1){
		int n, m;
		cin >> n >> m;
		REP(i,0,n){
			scanf("%s", in[i]);
			REP(j,0,m){
				if( in[i][j] == '^' ) in[i][j] = 0;
				if( in[i][j] == '>' ) in[i][j] = 1;
				if( in[i][j] == 'v' ) in[i][j] = 2;
				if( in[i][j] == '<' ) in[i][j] = 3;
			}
		}
		FILL(fix,0);
		int resp = 0;
		int imp = 0;		
		REP(i,0,n){
			REP(j,0,m){
				FILL(mark,0);
				int y = i, x = j;				
				int dir = in[i][j];
				mark[y][x] = 1;
				if( dir > 3 ) continue;
				int ly = y, lx = x;
				while(true){
					if( in[y][x] <= 3){ 
						dir = in[y][x];
						ly = y, lx = x;
					}
					
					int ny = y + dy[dir];
					int nx = x + dx[dir];
					if( ny < 0 || ny >= n || nx < 0 || nx >= m ) {
						
						y = ly, x = lx;
						// DB( y _ x );
						if(fix[y][x] == 0){
							int cont = 0;
							REP(ii,0,n){
								if( ii == y ) continue;
								if( in[ii][x] <= 3 ) cont++;
							}
							REP(jj,0,m){
								if( jj == x ) continue;
								if( in[y][jj] <= 3 ) cont++;
							}
							if( cont == 0 ){
								imp = 1; goto end;
							}
						}
						fix[y][x] = 1; 
						break;						
					}
					y = ny, x = nx;					
					if( mark[y][x] == 1) break;
					mark[y][x] = 1;
				}
			}
		}
		
		REP(i,0,n) REP(j,0,m){
			if(fix[i][j] > 0) resp++;
		}
		end:
		if( imp) printf("Case #%d: IMPOSSIBLE\n", cn);
		else printf("Case #%d: %d\n", cn, resp);
	}
	
	
	
	return 0;
}
