#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
int n, k;
double p[201], res;
bool check[201];
double D[20][201];
void back(int t,int cnt){
	if (t == n){
		if (cnt == k){
			memset(D, 0, sizeof(D));
			int c = 0;
			D[0][0] = 1;
			for (int i = 0; i < n; i++){
				if (check[i]){
					for (int j = 0; j <= k / 2; j++){
						D[c + 1][j] += D[c][j] * (1-p[i]);
						D[c + 1][j + 1] += D[c][j] * p[i];
					}
					c++;
				}
			}
			if (res < D[c][k / 2]){
				res = D[c][k / 2];
			}
		}
		return;
	}

	back(t + 1, cnt);
	if (cnt + 1 <= k){
		check[t] = 1;
		back(t + 1, cnt + 1);
		check[t] = 0;
	}
}
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		res = 0;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%lf", &p[i]);
		back(0,0);
		printf("Case #%d: %.8lf\n", test, res);
	}
	return 0;
}
