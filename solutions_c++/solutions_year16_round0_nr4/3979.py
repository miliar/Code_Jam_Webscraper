#include <iostream>

using namespace std;

int main(){
	int t, k, c, s;
	cin >> t;
	for (int i=0; i<t; i++) {
		cin >> k >> c >> s;
		cout << "Case #" << i+1 << ": ";
		for (int j = 1; j < k; j++) cout << j << ' ';
		cout << k << endl;
	}
}
