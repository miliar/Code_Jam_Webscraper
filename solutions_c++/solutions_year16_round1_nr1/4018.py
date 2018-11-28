#include <iostream>

using namespace std;

int main(){
	int t;cin >>t;
	for (int k = 1; k <= t;++k){
	string x;
	cin >> x;
	string ans = "";
	ans += x[0];
	for (int i = 1; i < x.size(); ++i){
		if(x[i] >= ans[0]){
			ans = x[i] + ans;
		}else{
			ans += x[i];
		}
	}
	cout <<"Case #"<<k << ": "<< ans << endl;
}
	return 0;
}
