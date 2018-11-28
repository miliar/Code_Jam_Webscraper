//In the name of God
#include <bits/stdc++.h>
using namespace std;
ofstream fout("GCJA.out");
#define cout fout
const int Maxn = 105;
char p[Maxn][Maxn];
int n,m;
int check(int i,int j){
	int res = 100 * 100 + 1;
	if(res) for(int r = i - 1; r >= 0; --r) if(p[r][j] != '.') res = 1 - (p[i][j] == '^');
	if(res) for(int r = i + 1; r < n; ++r) if(p[r][j] != '.') res = 1 - (p[i][j] == 'v');
	if(res) for(int r = j - 1; r >= 0;--r) if(p[i][r] != '.') res = 1 - (p[i][j] == '<');
	if(res) for(int r = j + 1; r < m; ++r ) if(p[i][r] != '.') res = 1 - (p[i][j] == '>');
	return res;
}
int main(){
	int tc;
	cin >> tc;
	int ts = 1;
	while(tc--){
		cout << "Case #" << ts++ << ": ";
		cin >> n >> m;
		for(int i = 0; i < n;i++){
			cin >> p[i];
		}
		int res = 0;
		for(int i = 0; i < n;i++)
			for(int j = 0; j < m;j++)
				if(p[i][j] != '.')
					res += check(i,j);
		if(res >= 100 * 100 + 1){
			cout <<"IMPOSSIBLE\n";
			continue;
		}
		cout << res << '\n';
	}
	return 0;
}
