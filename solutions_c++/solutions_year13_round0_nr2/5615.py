#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

#define N 110

int hei[N][N];
int a[N], b[N];
int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	int h, w;
	cin >> t;
	for (int cas=1; cas<=t; cas++){
		cin >> h >> w;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (int i=0; i<h; ++i){
			for (int j=0; j<w; ++j){
				cin >> hei[i][j];
				a[i] = max(a[i], hei[i][j]);
				b[j] = max(b[j], hei[i][j]);
			}
		}
		bool ans = true;
		for (int i=0; i<h; ++i){
			for (int j=0; j<w; ++j){
				if (hei[i][j] != min(a[i], b[j])) ans = false;
			}
		}
		printf("Case #%d: ", cas);
		if (ans) puts("YES");
		else puts("NO");
	}
	return 0;
}
