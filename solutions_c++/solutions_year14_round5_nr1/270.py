#include <bits/stdc++.h>
using namespace std;
const int limit = 1000000 + 5;
long long a[limit];
int n;

bool check(long long value){
	int cnt = 1;
	long long sum = 0;
	for(int i = 0; i < n; ++i){
		if (a[i] > value) return false;
		if (sum + a[i] > value){
			++cnt;
			sum = a[i];				
		}
		else sum += a[i];	
	}
	return cnt <= 3;
}

void MAIN(){
	int p,q,r,s;
	scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
	long long sum = 0;
	for(int i = 0; i < n; ++i){
		a[i] = i;
		a[i] = a[i] * p + q;
		a[i] %= r;
		a[i] = a[i] + s;
		sum = sum + a[i];
	}
	
	long long dau = 0, cuoi = sum;
	while (dau <= cuoi){
		long long k = (dau + cuoi) >> 1;
		if (check(k)) cuoi = k-1; else dau = k+1;	
	}
	
	printf("%.10f\n", double(sum - dau) / sum);
}

int main(){
	freopen("file.inp","r",stdin);
	freopen("file.out","w",stdout);
	int ntest; scanf("%d",&ntest);
	for(int test = 1; test <= ntest; ++test){
		printf("Case #%d: ", test);
		MAIN();	
	}
}