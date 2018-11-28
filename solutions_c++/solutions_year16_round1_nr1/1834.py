#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solve(){
	string s,r;
	cin >> s;
	r.push_back(s[0]);
	for (int i = 1; i < s.size(); i++){
		if (r[0] <= s[i]) r.insert(r.begin(),s[i]);
		else r.push_back(s[i]);
	}
	cout << r << endl;
}

int main(){
	
	//t: Test case
	int t;
	cin >> t;
	
	for (int i = 1; i<= t; i++){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

