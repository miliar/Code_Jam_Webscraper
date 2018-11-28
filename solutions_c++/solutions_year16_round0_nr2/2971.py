#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define int long long

int flatten(string& str){
	int res = 0;
	char pre = str[0];
	for(int i=1;i<str.size();i++){
		if(str[i] == pre) continue;
		pre = str[i];
		res++;
	}
	return res;
}

void solve(){
	string str;
	cin>> str;
	const char happy = '+';
	const char none = '-';

	int ans = flatten(str);
	if(str.back() == none) ans++;

	cout<< ans<< endl;
	return;
}

signed main(){
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1 << ": ";
		solve();
	}
	return 0;
}
