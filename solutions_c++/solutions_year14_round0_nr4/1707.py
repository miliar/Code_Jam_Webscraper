#include<iostream>
#include<algorithm>

using namespace std;

const int N= 1004;
double nao[N], ken[N];

bool cmp(const double u, const double v){
	return u < v;
}

int solve(int n, double adv[], double disadv[]){
	int cnt= 0;
	int i, j;
	for(i= 1, j= 1; i <= n && j <= n; i++, j++){
		while(disadv[i] >= adv[j] && j <= n)
			j++;
		if(j <= n && disadv[i] < adv[j])
			cnt++;
		else 
			break;
	}
	return cnt;
}

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas= 1; cas <= t; cas++){
		int n;
		scanf("%d", &n);
		for(int i= 1; i <= n; i++)
			scanf("%lf", nao+i);
		for(int i= 1; i <= n; i++)
			scanf("%lf", ken+i);
		sort(nao+1, nao+1+n, cmp);
		sort(ken+1, ken+1+n, cmp);
		int dec= solve(n, nao, ken);
		int war= n-solve(n, ken, nao);
		printf("Case #%d: %d %d\n", cas, dec, war);
	}
	return 0;
}