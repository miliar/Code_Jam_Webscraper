#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
const string dir = "^>v<";

int n,m;
char a[1000][1000];

void main2(){
	cin >> n >> m;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			cin >> a[i][j];
	int ans = 0;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++) if (a[i][j] != '.'){
			int d = dir.find(a[i][j]);
			int free = -1;
			do{
				int ii=i+dr[d], jj=j+dc[d];
				bool flag = true;
				while (ii>=0 && ii<n && jj>=0 && jj<m){
					if (a[ii][jj] != '.'){
						flag = false;
						break;
					}
					ii+= dr[d]; jj+= dc[d];
				}
				if (flag == false){
					free = d;
					break;
				}
				d = (d+1) % 4;
			}while (dir[d] != a[i][j]);
			if (free == -1){
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			ans+= (dir[free] != a[i][j]);
		}
	cout << ans << endl;
}

int main(){
	int tt; cin >> tt;
	for (int o=1; o<=tt; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
