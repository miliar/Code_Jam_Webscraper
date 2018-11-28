#include <iostream>
#include <string.h>

using namespace std;

int m_map[4][4] = {
	0,1,2,3,
	1,0,3,2,
	2,3,0,1,
	3,2,1,0
};

int n_map[4][4] = {
	0,0,0,0,
	0,1,0,1,
	0,1,1,0,
	0,0,1,1
};

int main() {
	int T;
	cin >> T;

	for (int i = 0 ; i < T ; ++i) {
		int L;
		unsigned long long X;
		string str;

		cin >> L >> X >> str;

		string cur = str;
		str = "";
		while (X) {
			if (X % 2) {
				str += cur;
			}
			cur += cur;
			X >>= 1;
		}

		bool ans = false;
		int arr[str.length()];
		int arr2[str.length()];

		int res = 0;
		int s = 0;
		for (int j = 0 ; j < str.length() ; ++j) {
			int tm = res;
			arr[j] = res = m_map[res][str[j]-'h'];
			arr2[j] = s = (n_map[tm][str[j]-'h'] + s) % 2;
		}

		for (int j = 0 ; j < str.length()-1 ; ++j) {
			for (int k = j+1 ; k < str.length()-1 ; ++k) {
				
				// arr[j] = i;
				bool aa = ( arr[j] == 1 && arr2[j] == 0);
				// arr[j] * j = arr[k];
				bool bb = ( m_map[arr[j]][2] == arr[k] && 
					(n_map[arr[j]][2] + arr2[j]) % 2 == arr2[k]);
				// arr[k] * k = arr[str.length()];
				bool cc = ( m_map[arr[k]][3] == arr[str.length()-1] &&
					(n_map[arr[k]][3] + arr2[k]) % 2 == arr2[str.length()-1]);

				ans = aa && bb && cc;
				if (ans) break;
			}
			if (ans) break;
		}

		cout << "Case #" << i+1 << ": " << (ans?"YES":"NO") << endl; 
	}
}