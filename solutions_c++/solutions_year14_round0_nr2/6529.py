#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;


int main() {
	int T;
	freopen("x.txt", "r", stdin);
	freopen("w.txt", "w", stdout); 
	scanf("%d", &T);
	
	for (int cas = 1; cas <= T; cas++) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double ans = X / 2;
		double sum = C / 2;
		int j = 1;
		for (int i = 1; i <= X * 10; i++) {
			if (sum + X / (i * F + 2) < ans) {
				ans = sum + X / (i * F + 2);
				j = i;
			}
			sum += C / (2 + i * F);
		}
		if (j == X * 10) puts("?????");
		printf("Case #%d: %.10lf\n", cas, ans);
	}
}
