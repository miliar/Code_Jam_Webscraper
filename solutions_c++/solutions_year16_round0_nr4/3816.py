#include <bits/stdc++.h>
using namespace std;

long long pwr(long long num, int exp){
	if(exp ==0) return 1;
	long long res = pwr(num, exp/2);
	res *= res;
	if(exp&1) res *= num;
	return res;
}
long long toBase10(int msk, int len, int fromBase){

	long long res = 0;
	for(int i = 0; i < len; i++){
		int b = ((msk >> i) & 1);

		res += pwr(fromBase, i) * b;
	}
	return res;
}
int divisor(long long num){
	int d = 1;
	for(long long i = 2; i * i <= num; i += d, d = 2){
		if(num % i == 0) return i;
	}
	return -1;
}
int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; ++t)
	{
		int k,c,s;
		cin >> k >> c >> s;
		printf("Case #%d:", t);
		for (int i = 1; i <= s; ++i)
		{
			printf(" %d",i);
		}
		printf("\n");
	}

}
