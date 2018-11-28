//AV
//quasar

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, r, c;
char mat[104][104];
bool v[104][104];

int solve(int i, int j);
int find(int r1, int c1, int dr, int dc){
	while (1){
		r1 += dr, c1 += dc;
		if (r1 < 0 || r1 == r || c1 < 0 || c1 == c) break;
		if (mat[r1][c1] != '.'){
			if (v[r1][c1]) return 0;
			else return solve(r1, c1);
		}
	}
	return -1;
}
int solve(int i, int j){
	v[i][j] = true;
	int dr=0, dc=0;
	switch (mat[i][j]){
	case '^':dr = -1; break;
	case '<':dc = -1; break;
	case 'v':dr = 1; break;
	case '>':dc = 1; break;
	}
	int tmp = find(i, j, dr, dc);
	if (tmp != -1) return tmp;
	dc = 0;
	for (dr = -1; dr <= 1;dr+=2)
	{
		tmp = find(i, j, dr, dc);
		if (tmp != -1)
			return tmp+1;
	}
	dr = 0;
	for (dc = -1; dc <= 1; dc += 2)
	{
		tmp = find(i, j, dr, dc);
		if (tmp != -1)
			return tmp + 1;
	}
	return -1;
}
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int cs = 1;

	cin >> t;
	while (t--){
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			cin >> mat[i];
		memset(v, 0, sizeof(v));
		int ans = 0;
		for (int i = 0; i < r;i++)
		for (int j = 0; j < c;j++)
		if (mat[i][j] != '.'&&!v[i][j])
		{
			int tmp = solve(i, j);
			if (tmp == -1)
			{
				ans = -1;
				break;
			}
			ans += tmp;
		}
		if (ans == -1)
			cout << "Case #"<<cs++<<": IMPOSSIBLE\n";
		else cout << "Case #" << cs++ << ": "<<ans<<"\n";
	}
}
