
#include <cassert>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
        int R,C;
        cin >> R >> C;
        vector<string> grid(R);
        vector<vector<int> > countH(R, vector<int>(C));
        vector<vector<int> > countV(R, vector<int>(C));
        fu(r,0,R) cin >> grid[r];
        fu(r,0,R) fu(c,0,C) countH[r][c] = (c?countH[r][c-1]:0) + (grid[r][c]!='.');
        fu(r,0,R) fu(c,0,C) countV[r][c] = (r?countV[r-1][c]:0) + (grid[r][c]!='.');

        int change = 0;
        bool possible = true;
        fu(r,0,R) fu(c,0,C) if(grid[r][c]!='.') {
            map<char,int> counts;
            counts['<'] = countH[r][c]-1;
            counts['^'] = countV[r][c]-1;
            counts['>'] = countH[r][C-1]-countH[r][c];
            counts['v'] = countV[R-1][c]-countV[r][c];
            if(counts[grid[r][c]]) continue;
            if(counts['<']+counts['>']+counts['^']+counts['v']) change++;
            else possible=false;
        }

        if(possible) cout << change << endl;
        else cout << "IMPOSSIBLE" << endl;
	}
}
