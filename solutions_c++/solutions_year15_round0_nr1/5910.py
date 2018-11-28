#include<iostream>

using namespace std;

int z, n, w, k, len;
string s;

int main() {
	cin >> z;
	for (int y = 1; y <= z; y++) {
		cin >> n >> s;
		w = 0;
		k = 0;
		len = s.size();
		for (int i = 0; i < s.size(); i++) {
			if (k < i) {
				w += i - k; 
			}
			k = max(k + s[i] - '0', i + s[i] - '0');
		}
		cout << "Case #" << y << ": " << w << endl;
	}
}
