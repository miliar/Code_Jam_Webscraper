#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
ll conv(ll n, int b){
	ll res = 0;
	ll pd = 1;
	while(n){
		res += pd * (n % 2);
		n /= 2;
		pd *= b;
	}
	return res;
}


int n, j;
string s;
int kh = 1000;
ll find_div(ll m){
	for(int d = 2; d < kh; d++){
		if(m % d == 0){
			return d;
		}
	}
	return m;

}
void solve(){
	int it = 0;
	for(ll i = (1LL << n) + 1; it < j && i < (1LL << (n + 1)); i += 2){
		bool fl = 1;
		for(int b = 2; b <= 10; b++){
			fl &= (find_div(conv(i, b)) < conv(i, b));
		}
		if(fl){
			
			cout << conv(i, 10) << " ";
			for(int b = 2; b <= 10; b++)
				cout << find_div(conv(i, b)) << " ";
			cout << endl;
			it++;
		}
			
	}
	cerr << it << endl;
}
int main(){
	cin >> n >> j;
	n--;
	cout << "Case #1:\n";
	solve();
	return 0;
}
