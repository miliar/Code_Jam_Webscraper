#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
void solve(){
	int n;
	cin >> n;
	vector<int> arr(n);
	for(int i = 0; i < n; ++i)
		cin >> arr[i];
	while(true){
		vector<char> act;
		int hi = 0;
		for(int i = 0; i < n; ++i){
			if(arr[i] > hi){
				hi = arr[i];
				act.resize(0);
			}
			if(arr[i] == hi)
				act.push_back(i);
		}
		if(hi==0)
			break;
		if(act.size()%2==0){
			cout << ' ' << (char)(act[0]+'A') << (char)(act[1]+'A');
			--arr[act[0]];
			--arr[act[1]];
		}
		else{
			cout << ' ' << (char)(act[0]+'A');
			--arr[act[0]];
		}
	}
}
int main(){
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; ++tc){
		cout << "Case #" << tc << ":";
		solve();
		cout << '\n';
	}
}

