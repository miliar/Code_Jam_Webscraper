#include <bits/stdc++.h>
using namespace std;

int main(){
	int t; cin >> t;
	for(int i=0; i<t; i++){
		int k, c, s; cin >> k >> c >> s;
		cout << "Case #" << (i+1) << ":";
		for(int j=0; j<k; j++) 
			cout << " " << (j+1);
		cout << '\n';
	}
	return 0;
}