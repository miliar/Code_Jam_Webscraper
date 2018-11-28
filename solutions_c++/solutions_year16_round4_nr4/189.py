#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

string stuff[25];
int nr;
int nc;
int n;
int vis[50];
void dfs(int i){
	if(vis[i]) return;
	vis[i] = 1;
	if(i < n){
		nr++;
		for(int j = 0; j < n; j++){
			if(stuff[i][j] == '1') dfs(j+n);
		}
	} else {
		nc++;
		for(int j = 0; j < n; j++){
			if(stuff[j][i-n] == '1') dfs(j);
		}
	}
}
int rows[50];
int cols[50];
int cc = 0;
main() {
	FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
	FILE *fout = freopen("D-small-attempt0.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> stuff[i];
			vis[i] = vis[i+n] = 0;
		}
		int n1 = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				n1 += (stuff[i][j] == '1');
			}
		}
		int ans = 0;
		int newn = n;
		cc = 0;
		for(int i = 0; i < 2*n; i++){
			nr = nc = 0;
			if(!vis[i]){
				dfs(i);
				if(nr == nc){
					ans += nr*nr;
					newn -= nr;
				} else {
					rows[cc] = nr;
					cols[cc++] = nc;
				}
			}
		}
		if(cc <= 3){
			ans += newn*newn;
			cout << ans-n1 << endl;
		} else {
			cout << "DO YOURSELF\n";
			cout << ans-n1<< endl;
			for(int i = 0; i < cc; i++){
				cout << rows[i] << " " << cols[i] << endl;
			}
		}
	}
	exit(0);
}
// I DID some cases manually