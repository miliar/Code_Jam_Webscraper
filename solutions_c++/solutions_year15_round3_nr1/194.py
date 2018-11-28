#include <bits/stdc++.h>
using namespace std;

const int inf = 1000000000;

int dp[100];

void main2(){
	int r,c,w; cin >> r >> c >> w;
	cout << (r-1) * (c/w) + (c-1)/w + w << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
