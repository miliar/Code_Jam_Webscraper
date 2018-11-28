#include <iostream>

using namespace std;

const int O = 1;
const int I = 2;
const int J = 3;
const int K = 4;

const int mulmap[4][4] = {
	{ O,  I,	J,  K},
	{ I, -O,	K, -J},
	{ J, -K, -O,  I},
	{ K,  J, -I, -O}
};

int mul(int c1, int c2)
{
	int sign = 1;
	if (c1 < 0) {
		c1 *= -1;
		sign *= -1;
	}
	if (c2 < 0) {
		c2 *= -1;
		sign *= -1;
	}
	return sign * mulmap[c1-1][c2-1];
}

int div1(int c1, int c2)
{
	int sign = 1;
	if (c2 < 0) {
		c2 *= -1;
		sign *= -1;
	}
	for (int i = 0; i < 4; i++) {
		if (mulmap[c2-1][i] == c1) {
			return sign * (i + 1);
		} else if (mulmap[c2-1][i] == -c1) {
			return -1 * sign * (i + 1);
		}
	}
	return 0;
}

int mul(int c1, char ch)
{
	int c2;
	switch(ch) {
		case 'i': c2 = I; break;
		case 'j': c2 = J; break;
		case 'k': c2 = K; break;
	}
	return mul(c1, c2);
}

int mul(char ch, int c2)
{
	int c1;
	switch(ch) {
		case 'i': c1 = I; break;
		case 'j': c1 = J; break;
		case 'k': c1 = K; break;
	}
	return mul(c1, c2);
}

string itoc(int i) {
	return (string[9]){"-k", "-j", "-i", "-1", "", "1", "i", "j", "k"}[i+4];
}

int main()
{
	int T;
	cin >> T;
	for (int j = 1; j <= T; ++j) {
		int L, X;
		string letters;
		cin >> L >> X >> letters;
		int maxL = (4 < X ? 4 : X) * L;
		int totL = X * L;
		int bprod[L];
		int fprod[L];
		int c = O;
		for (int i = L - 1; i >= 0; --i) {
			bprod[i] = c = mul(letters[i], c);
		}
		c = O;
		for (int i = 0; i < L; ++i) {
			fprod[i] = c = mul(c, letters[i]);
		}
		if (fprod[L - 1] != bprod[0]) {
			cerr << "Commutative error: " << fprod[L] << "!=" << bprod[0] << endl;
			return(1);
		}

		int lproduct = bprod[0]; // product of full segment of letters
		int lpow[4];
		lpow[0] = O;
		for (int i = 1; i < 4; ++i) {
			lpow[i] = mul(lpow[i-1], lproduct);
		}
		bool found = false;
		int ipow = O;
		for (int li = 0; !found && li < totL-2 && li < maxL; ++li) {
			//cout << itoc(fprod[li%L]) << ' ' << itoc(lpow[(li)/L]) << ' ' << itoc(mul(fprod[li%L], lpow[(li)/L])) << endl;
			if (mul(lpow[(li)/L], fprod[li%L]) == I) {
				//cout << li << endl;
				for (int lj = li + 1; !found && lj < totL-1 && lj-li+1 < maxL; ++lj) {
					//cout << ':' << lj << endl;
					int jprod = O;
					int ldiff = lj/L - li/L;
					//cout << "ldiff = " << ldiff << ", li = " << li << ", lj = " << lj << endl;
					if (ldiff == 0) {
						jprod = div1(fprod[lj%L], fprod[li%L]);
						//cout << itoc(fprod[li%L]) << '/' << itoc(fprod[lj%L]) << " = " << itoc(jprod) << endl;
					} else if (ldiff == 1) {
						jprod = mul(bprod[(li+1)%L], fprod[lj%L]);
					} else {
						jprod = mul(bprod[(li+1)%L], lpow[ldiff-1]);
						jprod = mul(jprod, fprod[lj%L]);
					}
					//cout << jprod << ' ' << itoc(jprod) << endl;
					if (jprod == J) {
						//cout << "jprod = J at " << li << endl;
						int kprod = mul(bprod[(lj+1)%L], lpow[(X - 1 - (lj+1)/L)%4]);
						if (kprod == K) {
								found = true;
						}
					}
				}
			}
		}
		cout << "Case #" << j << ": " << (found ? "YES" : "NO") << endl;
	}
	return 0;
}
