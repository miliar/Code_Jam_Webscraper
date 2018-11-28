#include <iostream>
#include <cassert>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int grid[5][5];

void output(int msk, int R, int C, int rr=-1, int cc=-1) {
	fu(r,0,R) {
		fu(c,0,C)
			if(r==rr&&c==cc) cout << 'c';
			else cout << ((msk&(1<<(r*C+c)))?'*':'.');
		cout << endl;
	}
}

int dfs(int r, int c, int R, int C) {
	if(r<0 || r>=R || c<0 || c>=C) return 0;
	if(grid[r][c]==-1) return 0;
	if(grid[r][c]>0) { grid[r][c]=-1; return 1; }
	assert(grid[r][c]==0);
	grid[r][c]=-1;
	int ret=1;
	fu(r2,r-1,r+2) fu(c2,c-1,c+2) ret += dfs(r2,c2,R,C);
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ":" << endl;
		int R,C,M;
		cin >> R >> C >> M;
		if(M==R*C-1) {
			fu(r,0,R) {
				fu(c,0,C) {
					cout << (r+c==0 ? 'c' : '*');
				}
				cout << endl;
			}
			continue;
		}
		int bst=0;
		bool done=false;
		fu(msk,0,(1<<(R*C))) {
			int cnt=0;
			fu(j,0,R*C) if(msk&(1<<j)) cnt++;
			if(cnt!=M) continue;
			bzero(grid,sizeof(grid));
			fu(r,0,R) fu(c,0,C) fu(r2,r-1,r+2) fu(c2,c-1,c+2)
				if(r2>=0 && r2<R && c2>=0 && c2<C && (msk&(1<<(r2*C+c2))))
					grid[r][c]++;
			fu(r,0,R) fu(c,0,C) if(msk&(1<<(r*C+c))) grid[r][c]=-1;
			fu(r,0,R) fu(c,0,C) if(grid[r][c]==0) {
				int ret = dfs(r,c,R,C);
				//cout << ret << " vs " << M << endl;
				if(ret==R*C-M) {
					//cout << ret << " " << M << " " << msk << " " <<  cnt << endl;
					output(msk,R,C,r,c);
					done=true;
				}
				bst=max(bst,ret);
				r=R; c=C;
			}
			if(done) break;
		}
		if(!done) { cout << "Impossible" << endl; }
        }
}
