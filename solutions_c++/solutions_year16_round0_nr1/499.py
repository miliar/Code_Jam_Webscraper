#include<bits/stdc++.h>
using namespace std;

void fillout(int num, vector<int> &stamp) {
	while(num != 0) {
		stamp[num%10] ++ ;
		num /= 10;
	}
}


int solve(int N) {
	vector<int> data(10, 0);
	for(int j=1;; j++) {
		fillout(j*N, data);
		
		bool ok = true;
		for(int i=0; i<data.size(); i++)
			if(data[i] == 0) ok = false;
		if(ok) return j * N;
	}
	return 0;
}


int main() {
	int T;
	cin >>T;
	for(int i=0; i<T; i++) {
		int N;
		cin >> N;
		if( N > 0 ) {
			int ans = solve(N);
			cout << "Case #" << i+1 << ": " << ans << endl;
		}
		else cout << "Case #" << i+1 << ": INSOMNIA" << endl;
	}
	return 0;
}

