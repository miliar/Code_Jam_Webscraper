#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <stack>
#include <queue>

using namespace std;

int a[1000000];
long long sum[1000001];

double solveSmall(int N){
	double res = 0.0;
	for(int i=0;i<N;i++){
		for(int j=i;j<N;j++){
			res = max(res, (sum[N]-max(sum[i], max(sum[j+1]-sum[i], sum[N]-sum[j+1])))/(double)sum[N]);
		}
	}
	return res;
}

double solveLarge(int N){
	long long get = sum[N];
	for(int i=0;i<N;i++){
		long long chooseA = sum[i];
		if(sum[i+1]-sum[i] > sum[N]-sum[i+1]){
			get = min(get, max(chooseA, sum[i+1]-sum[i]));
		} else {
			int L = i, R = N;
			while(R-L > 1){
				int mid = (L+R)/2;
				if(sum[mid+1]-sum[i] <= sum[N]-sum[mid+1]){
					L = mid;
				} else {
					R = mid;
				}
			}
			get = min(get, max(chooseA, max(sum[L+1]-sum[i], sum[N]-sum[L+1])));
			if(L+2 <= N){
				get = min(get, max(chooseA, max(sum[L+2]-sum[i], sum[N]-sum[L+2])));
			}
		}
	}
	return (sum[N]-get)/(double)sum[N];
}

int main(){
	int T; cin >> T;
	for(int test=1;test<=T;test++){
		int N, p, q, r, s; cin >> N >> p >> q >> r >> s;
		sum[0] = 0;
		for(int i=0;i<N;i++){
			a[i] = (i*(long long)p + q)%r + s;
			sum[i+1] = sum[i] + a[i];
		}
		printf("Case #%d: %.10lf\n", test, solveLarge(N));
	}
}
