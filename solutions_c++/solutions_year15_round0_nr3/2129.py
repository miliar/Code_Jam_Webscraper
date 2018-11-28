#include <iostream>

using namespace std;

#define ONE 1
#define I 2
#define J 3
#define K 4


int mat[4][4] = {
	{ONE, I, J, K},
	{I, -ONE, K, -J},
	{J, -K, -ONE, I},
	{K, J, -I, -ONE}
};

int mult(int a, int b) {
	int sign = 1;
	if (a < 0) {
		sign ^= 1;
		a = -a;
	}
	if (b < 0) {
		sign ^= 1;
		b = -b;
	}

	return (-1 + 2*sign)*mat[a-1][b-1];
}

int to_int(char c) {
	switch(c) {
		case '1':
			return ONE;
		case 'i':
			return I;
		case 'j':
			return J;
		case 'k':
			return K;
		default:
			return 0;
	}
}

int prod(string s, int start, int end) {
	int ris = to_int(s[start]);
	for (int i = start+1; i < end; i++) {
		int add = to_int(s[i]);
		ris = mult(ris, add);
	}
	return ris;
}



int main() {
	int T;

	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		string str;
		int L, X;
		bool found = false;
		cin >> L >> X;
		cin >> str;

		string s = "";
		while (X--) s+=str;

		if (prod(s, 0, s.size()) == -ONE) {
			int li = s.size();
			for (int i = 0; i < s.size(); i++) {
				if (prod(s, 0, i) == I) {
					li = i;
					break;
				}
			}
			int ri = 0;
			for (int i = s.size()-1; i > 0; i--) {
				if (prod(s, i, s.size()) == K) {
					ri = i;
					break;
				}
			}

			if (li < ri) found = true;
		}


		if (found)
			cout << "Case #" << tc << ": YES" << endl;
		else
			cout << "Case #" << tc << ": NO" << endl;
	}
	return 0;
}