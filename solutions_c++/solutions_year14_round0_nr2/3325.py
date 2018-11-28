#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int main(){
	//freopen("B-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cnt = 1; cnt <= T; cnt++){
		double C, F, X, speed = 2, tmp = 0, ans = 1000000;
		scanf("%lf%lf%lf", &C, &F, &X);
		for(int i = 0; i <= (int) X / C; i++){
			ans = min(ans, X / speed + tmp);
			tmp += C / speed;
			speed += F;
		}
		printf("Case #%d: %.07lf\n", cnt, ans);
	}
	return 0;
}
