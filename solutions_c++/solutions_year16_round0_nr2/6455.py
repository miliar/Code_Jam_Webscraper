#include <iostream>

using namespace std;

int main(){
	string x;
	int t; cin>> t;
	for (int k = 1; k <=t; ++k){
		cin >> x;
		int ans = 0;
		char sw = x[0];
		for ( int i = 0; i < x.size(); ++i){
			if(x[i] != sw){
				ans++;
				sw = x[i];
		}
	}
	if(sw == '-') ans++;
	cout <<"Case #"<< k << ": "<<  ans << endl;
	}
}
