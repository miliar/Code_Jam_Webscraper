#include<bits/stdc++.h>

using namespace std;

int t, k, c, s;

int main(){
	
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	ofstream cout ("output.txt");
	
	cin >> t;
	int cases = 1;
	while(t--){
		cin >> k >> c >> s;
		cout << "Case #" << cases++ << ": ";
		long long soma = k*(c-1), num = 1;
		for(int i = 1; i <= k; i++) cout << num << " ", num += soma;
		cout << '\n';
	}
	
}