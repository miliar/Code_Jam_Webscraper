#include <bits/stdc++.h>
using namespace std;

int t;
int n;
set <char> seen;

void solve(){
	int k = n;
	while(seen.size() < 10){
		string num;
		ostringstream convert;
		convert << n;
		num = convert.str();
		for(int i = 0; i < num.size(); i++){
			seen.insert(num[i]);
		}
		n += k;
	}
	cout << n-k << endl;
	
}



int main(void){
	ios :: sync_with_stdio(false);
	cin >> t;
	int cnt = 1;
	while(t--){
		seen.clear();
		cin >> n;
		cout << "Case #" << cnt << ": ";
		if(n)solve();
		else cout << "INSOMNIA" << endl;
		cnt++;	
	}
	return 0;
}
