#include <bits/stdc++.h>
using  namespace std;

long long get (int mask, int base, int len){
	long long ret = 0;
	for (int i=len-1; i>=0; i--)
		ret = ret*base + ((mask >> i) & 1);
	return ret;
}

long long div (long long x){
	for (long long i=2; i*i<=x; i++) if (x%i == 0)
		return i;
	return -1LL;
}

void main2(){
	int n,c; cin >> n >> c;
	for (int mask=(1<<(n-1)); (mask < (1<<n)) && c; mask++) if (mask & 1){
		vector<long long> d;
		for (int b=2; b<=10; b++){
			long long num = get(mask, b, n);
			long long dd = div(num);
			if (dd != -1)
				d.push_back(dd);
			else
				break;
		}
		if ((int)d.size() == 9){
			for (int i=n-1; i>=0; i--)
				cout << ((mask>>i)&1);
			cout << " ";
			for (int i=0; i<(int)d.size(); i++)
				cout << d[i] << ' ';
			cout << endl;
			c--;
		}
	}
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ":" << endl;
		main2();
	}
	return 0;
}
