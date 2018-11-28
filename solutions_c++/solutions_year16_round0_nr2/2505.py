#include <iostream>
#include <vector>

using namespace std;

typedef vector <int> VI;
typedef long long ll;

int main(){
	ll T;
	cin >> T;
	for (ll i = 0; i < T; ++i){
		string s;
		cin >> s;
		int l = s.size();
		VI plus = VI(l), minus = VI(l);
		cout << "Case #" << i+1 << ": ";
		if (s[0] == '+'){
			plus[0] = 0;
			minus[0] = 1;
		}
		else {
			plus[0] = 1;
			minus[0] = 0;
		}
		for (int j = 1; j < l; ++j){
			if (s[j] == '+'){
				plus[j] = plus[j-1];
				minus[j] = plus[j] + 1;
			}
			else{
				minus[j] = minus[j-1];
				plus[j] = minus[j] + 1;
			}
		}
		cout << plus[l-1] << endl;
	}
}

