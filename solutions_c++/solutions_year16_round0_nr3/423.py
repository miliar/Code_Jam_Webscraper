#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

vector<int> prime;
void init() {
	int tmp[10] = {2,3,5,7,11,13,17,19,23,29};
	for(int i=0; i<10; i++) prime.push_back(tmp[i]);
}

string bin(LL N) {
	string res;
	while(N!=0) {
		if(N%2==0) res = "0" + res;
		else res = "1" + res;
		N /= 2;
	}
	return res;
}

bool check(LL base, LL mod, LL origin) {
	LL res = 0;
	LL bai = 1;
	while(origin != 0) {
		if(origin % 2) {
			res += bai;
			
		}
		origin /= 2;
		bai *= base;
		bai %= mod;
		res %= mod;
	}
	if(res!=0) return false;
	return true; 
}


void solve(int N, int J) {
	LL cur = 1;
	for(int i=0; i<N-1; i++) cur *= 2;
	cur ++;
	int cnt = 0;
	while(true) {
		bool ok = true;
		vector<int> res;
		for(int i=2; i<=10; i++) {
			int num = 0;
			for(int j=0; j<prime.size(); j++) {
				if(check(i, prime[j], cur)) 
					num = prime[j];
			}
			if(num == 0) ok = false;
			res.push_back(num);
		}
		if(ok) {
			cnt++;
			
			cout << bin(cur) ;
			for(auto elem: res) cout << " " << elem ;
			cout << endl;
			
			if(cnt == J) break;
		}
		cur += 2;
	}
	
}


int main() {
	init();
	int T;
	cin >> T;
	for(int i=0; i<T; i++) {
		int N,J;
		cin >> N >> J;
		cout << "Case #" << i+1 << ":" << endl;
		solve(N,J);
	}
	
	
	return 0;
}

