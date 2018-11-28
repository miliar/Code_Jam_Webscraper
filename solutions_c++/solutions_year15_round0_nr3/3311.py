#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int find(int a, int b) {
	int s1, s2;
	s1 = 1;
	s2 = 1;
	if(a < 0) {
		s1 = -1;
		a = -1 * a;
	}
	if(b < 0) {
		s2 = -1;
		b = -1 * b;
	}
	if(a == 1) return s1 * s2 * b;
	if(b == 1) return s1 * s2 * a;
	if(a == 'i') {
		if(b == 'i') {
			return s1 * s2 *  (-1);
		}
		if(b == 'j') {
			return s1 * s2 *  'k';
		}
		if(b == 'k') {
			return s1 * s2 *  (-1) * 'j';
		}
	}
	if(a == 'j') {
		if(b == 'i') {
			return s1 * s2 *  (-1) * 'k';
		}
		if(b == 'j') {
			return s1 * s2 *  (-1);
		}
		if(b == 'k') {
			return s1 * s2 *  'i';
		}
	}
	if(a == 'k') {
		if(b == 'i') {
			return s1 * s2 *  'j';
		}
		if(b == 'j') {
			return s1 * s2 *  (-1) * 'i';
		}
		if(b == 'k') {
			return s1 * s2 *  (-1);
		}
	}
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int l, n;
		cin >> l >> n;
		string str;
		cin >> str;
		int start = 1;
		int s1 = -1;
		int s2 = -1;
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < str.length() ; j++) {
				start = find(start, str[j]);
				if(start == 'i') {
					if(s1 == -1) {
						s1 = i*l + j;
					}
				}
			}
		}
		start = 1;
		for(int i = n - 1 ; i >= 0 ; i--) {
			for(int j = str.length() - 1 ; j >= 0 ; j--) {
				start = find(str[j], start);
				if(start == 'k') {
					if(s2 == -1) {
						s2 = i*l + j;
					}
				}
			}
		}
		if(start == -1) {
			if(s1 != -1 && s2 != - 1 && s2 - s1 > 1) {
				cout << "Case #" << tc << ": " << "YES" << endl;
			} else {
				cout << "Case #" << tc << ": " << "NO" << endl;
			}
		} else {
			cout << "Case #" << tc << ": " << "NO" << endl;
		}
	}
	return 0;
}
