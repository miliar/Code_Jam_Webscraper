#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solve(){
	long long k,c,s;
	long long p= 1;
	cin >> k >> c >> s;
	for (int i = 0; i<c-1;i++){
		p = p * k;
	}
	
	long long x = 1;
	
	for (int i = 1; i<=s; i++){
		cout << x << " ";
		x = x + p;
	}
	cout << endl;
	
}

int main(){
	
	int t;
	cin >> t;
	
	for (int i = 1; i<= t; i++){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
