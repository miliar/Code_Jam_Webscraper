#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	
	int t;
	cin >> t;
	
	for(int x = 0; x < t; x++){
		int n;
		cin >> n;
		cout << "Case #" << x + 1 << ": ";

		bool used[10];
		for(int i = 0; i < 10; i++){
			used[i] = false;
		}
		int left = 10;
		for(int i = n, tryn = 0; tryn < 1000000; i += n, tryn++){
			int cop = i;
			while(cop > 0){
				left -= (!used[cop % 10]);
				used[cop % 10] = true;
				cop /= 10;
			}

			if(left == 0){
				cout << i << '\n';
				break;
			}
		}

		if(left != 0){
			cout << "INSOMNIA" << '\n';
		}
	}
	return 0;
}
