#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[20];
int b[20];
int c[20];

bool cmp(int a, int b){
	return a > b;
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			scanf("%d", &a[i]);
		}
		int ans = 100000000;
		for(int i = 0; i < (1<<n); i++){
			int k = 0;
			if(i){
				for(int j = 0; j < n; j++){
					if(i & (1<<j))
						b[k++] = a[j];
				}
				sort(b, b + k);
			}
			int sta = (1<<n) - i - 1;
			if(sta){
				int s = k;
				for(int j = 0; j < n; j++){
					if(sta & (1<<j)) b[s++] = a[j];
				}
				sort(b + k, b + s, cmp);
			}
			if(i && sta && b[k - 1] < b[k]) continue;
			int num = 0;
			for(int j = 0; j < n; j++) c[j] = a[j];
			for(int j = 0; j < n; j++){
				int k;
				for(k = j; k < n; k++){
					if(b[j] == c[k]) break;
				}
				for(int p = k; p > j; p--){
					swap(c[p], c[p - 1]);
					num++;
				}
			}
			ans = min(ans, num);
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
}
