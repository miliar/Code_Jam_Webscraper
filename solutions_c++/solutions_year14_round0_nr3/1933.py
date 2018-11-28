/* 
 * in the name of god 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */ 

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std; 

typedef long long LL; 
typedef pair<int,int> pii; 
typedef complex<double> point; 

bool mark[100][100];
char mat [100][100];
int n,m,tot;

void dfs (int x, int y){
	if (x<0 || y<0 || x>=n || y>=m || mark[x][y] || mat[x][y]=='*') return;
	mark[x][y] = true;
	for (int dx = -1; dx<=1; dx++)
		for (int dy = -1; dy <= 1; dy++){
			int xx = x + dx, yy = y + dy;
			if (xx<0 || yy<0 || xx>=n || yy>=m) continue;
			if (mat[xx][yy] == '*')
				return;
		}
	for (int dx = -1; dx<=1; dx++)
		for (int dy = -1; dy <= 1; dy++)
			dfs(x+dx, y+dy);
}

int main(){
	int T; cin >> T;
	for (int rep=1; rep<=T; rep++){
		cout << "Case #" << rep << ":\n";
		cin >> n >> m >> tot;
		if (tot == n*m-1){
			for (int i=0; i<n; i++){
				for (int j=0; j<m; j++){
					if (i==0 && j==0)
						cout << 'c';
					else
						cout << '*';
				}
				cout << endl;
			}
			continue;
		}
		bool OK = false;
		for (int mask = 0; mask < (1<<n*m); mask++) if (__builtin_popcount(mask) == tot){
			for (int r = 0; r < n; r++)	
				for (int c = 0; c < m; c++)
					if (mask & (1<<(r*m+c)))
						mat[r][c] = '*';
					else
						mat[r][c] = '.';
			memset(mark, false, sizeof mark);
			for (int r = 0; r < n; r++)
				for (int c = 0; c < m; c++) if (mat[r][c] == '.'){
					bool emp = true;
					for (int dr = -1; dr<=1; dr++)
						for (int dc = -1; dc<=1; dc++){
							int rr = r + dr, cc = c + dc;
							if (rr<0 || rr>=n || cc<0 || cc>=m) continue;
							if (mat[rr][cc] == '*') emp = false;
						}
					if (emp){
						mat[r][c] = 'c';
						dfs(r,c);
						r = c = max(n,m);
					}
				}
			bool bad = false;
			for (int i=0; i<n; i++)
				for (int j=0; j<m; j++) if (!mark[i][j] && mat[i][j]=='.')
					bad = true;				
			if (!bad){
				for (int i=0; i<n; i++){
					for (int j=0; j<m; j++)
						cout << mat[i][j];
					cout << endl;
				}
				OK = true;
				break;
			}
		}
		if (!OK)
			cout << "Impossible" << endl;
	}
	return 0;
}
