#include<stdio.h>
#include<algorithm>
using namespace std;
int n, r;
long long w[10100], C[10100], tw[10100], tc[10100], Ans[101];
void Do(){
	long long d = w[2] - w[1];
	if (w[n] == 0){
		d = -d;
	}
	Ans[r++] = d;
	int i, cnt = 0;
	if (d < 0){
		int pv1 = 1, pv2 = 1;
		for (i = 2; i <= n; i++){
			while (w[pv1] < w[i] + d)pv1++;
			if (w[pv1] > w[i] + d)continue;
			while (pv2 <= cnt && tw[pv2] < w[i] + d)pv2++;
			tw[cnt + 1] = w[i], tc[cnt + 1] = C[pv1];
			if (pv2 <= cnt && tw[pv2] == w[i] + d){
				tc[cnt + 1] -= tc[pv2];
			}
			cnt++;
		}
		n = 0;
		for (i = 1; i <= cnt; i++){
			if (tc[i]){
				n++;
				w[n] = tw[i];
				C[n] = tc[i];
			}
		}
	}
	else{
		int pv1 = n, pv2 = 1;
		for (i = n - 1; i >= 1; i--){
			while (w[pv1] > w[i] + d)pv1--;
			if (w[pv1] < w[i] + d)continue;
			while (pv2 <= cnt && tw[pv2] > w[i] + d)pv2++;
			tw[cnt + 1] = w[i], tc[cnt + 1] = C[pv1];
			if (pv2 <= cnt && tw[pv2] == w[i] + d)tc[cnt + 1] -= tc[pv2];
			cnt++;
		}
		n = 0;
		for (i = cnt; i >= 1; i--){
			if (tc[i]){
				n++;
				w[n] = tw[i];
				C[n] = tc[i];
			}
		}
	}
}
int main(){
	int TC, TT, i;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d", &n);
		for (i = 1; i <= n; i++){
			scanf("%lld", &w[i]);
		}
		for (i = 1; i <= n; i++){
			scanf("%lld", &C[i]);
		}
		r = 0;
		while (n != 1){
			Do();
		}
		while (C[1] != 1){
			C[1] /= 2;
			Ans[r++] = 0;
		}
		sort(Ans, Ans + r);
		for (i = 0; i < r; i++)printf("%lld ", Ans[i]);
		printf("\n");
	}
}