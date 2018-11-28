#include <algorithm>
#include <iostream>
#include <cstring>
#define L 1000001

char N[L];

using namespace std;

bool is_cons(char c) {
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

bool is_sub_cons(int start, int n) {
	for (int i = start; i < start + n; ++ i) {
		if (!is_cons(N[i])) {
			return false;
		}
	}
	return true;
}

int find_cons(int start, int end, int n) {
	for (int i = start; i < end - n + 1; ++ i) {
		if (is_sub_cons(i, n)) {
			return i;
		}
	}
	return -1;
}

int main() {
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++ i) {
		int ans = 0, n;
		cin >> N >> n; 
		int l = strlen(N);

		for (int j = 0; j < l - n + 1; ++ j) {
			int k = find_cons(j, l, n);
		//	cout << k << endl;
			if (k == -1) {
				break;
			}

			ans += l - (k+n) + 1;
		}

		cout << "Case #" << i << ": " << ans << endl; 
	}	
	
}
