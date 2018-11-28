#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int n, m;
char a[200][200];
int d[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
int gao(){
	//cout<<n<<' '<<m<<endl;
	int ret = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j){
				//cout<<i<<' '<<j<<' '<<a[i][j]<<endl;
			if (a[i][j] != '.'){
				int b[4] = {0, 0, 0, 0};
				for (int k = 0; k < 4; ++k){
					int x = i + d[k][0];
					int y = j + d[k][1];
					while ((x < n)&&(x >= 0)&&(y < m)&&(y >= 0)){
						//cout<<x<<' '<<y<<endl;
						if (a[x][y] != '.'){
							b[k] = 1;
							break;
						}
						x += d[k][0];
						y += d[k][1];
					}
				}
				
				//cout<<b[0]<<' '<<b[1]<<' '<<b[2]<<' '<<b[3]<<endl;
				if ((b[0] == 1)&&(a[i][j] == '^')) continue;
				if ((b[1] == 1)&&(a[i][j] == 'v')) continue;
				if ((b[2] == 1)&&(a[i][j] == '<')) continue;
				if ((b[3] == 1)&&(a[i][j] == '>')) continue;
				if (b[0] + b[1] + b[2] + b[3] > 0) ++ret;
				else return -1;
			}
		}
	return ret;
}
int main(){
	int t = 0, tt;
	for (scanf("%d ", &tt); t < tt; ++t){
		scanf("%d %d ", &n, &m);
		for (int i = 0; i < n; ++i){
			scanf("%s", a[i]);
			//cout<<a[i]<<endl;
		}
		int ans = gao();
		if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else printf("Case #%d: %d\n", t + 1, ans);
	}
}