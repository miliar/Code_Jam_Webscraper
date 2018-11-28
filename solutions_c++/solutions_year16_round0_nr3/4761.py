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
		int n,lim;
		cin >> n >> lim;
		cout << "Case #1:\n";
		for(int msk =0; msk < (1<<n) && lim; msk++){
			int b1 = ((msk >> (n-1))&1);
			int b2 = msk & 1;
			if(!b1 || !b2) continue;
			vector<int> res;
			for(int base = 2; base <= 10; base++){
				long long num = toBase10(msk, n, base);
				int div = divisor(num);
				if(div == -1){
					res.clear();
					break;
				}
				res.push_back(div);
			}
			if(res.size()){
				lim--;
				bitset<32> b(msk);
				cout << b.to_string().substr(32-n);
				for(int n : res){cout << " " << n;}
				cout << "\n";
			}
		}
	}

}
