#include <iostream>
#include <fstream>

using namespace std;

class Q {
	public:
		//1 = >0
		//-1 = <0
		int v;
		int sign;
		Q(char c) {
			sign = 1;
			if(c == '1') v = 0;
			if(c == 'i') v = 1;
			if(c == 'j') v = 2;
			if(c == 'k') v = 3;
		};
		Q(int v) : v(v), sign(1) {};
		Q operator*(Q b) {
			int s = b.sign * sign;
			int val = 0;
			switch(v | b.v << 4) {
				case 0x00: val = 0; break;
				case 0x10: val = 1; break;
				case 0x20: val = 2; break;
				case 0x30: val = 3; break;

				case 0x01: val = 1; break;
				case 0x11: val = 0; s *= -1; break;
				case 0x21: val = 3; break;
				case 0x31: val = 2; s *= -1; break;

				case 0x02: val = 2; break;
				case 0x12: val = 3; s *= -1; break;
				case 0x22: val = 0; s *= -1; break;
				case 0x32: val = 1; break;

				case 0x03: val = 3; break;
				case 0x13: val = 2; break;
				case 0x23: val = 1; s *= -1; break;
				case 0x33: val = 0; s *= -1; break;
			}

			Q r(val);
			r.sign = s;
			return r;
		}

		bool operator==(Q b) {
			return b.v == v && b.sign == sign;
		}

		bool operator!=(Q b) {
			return !( b == *this);
		}
};

ostream& operator<<(ostream& os, const Q& q) {
	if(q.sign == -1)
		os << "-";
	switch(q.v) {
		case 0: os << "1"; break;
		case 1: os << "i"; break;
		case 2: os << "j"; break;
		case 3: os << "k"; break;
	}
	return os;
}

using namespace std;
int main() {
	Q O('1');
	Q I('i');
	Q J('j');
	Q K('k');

	auto ijk = I*J*K;

	int nTests = 0;
	cin >> nTests;
	for(int i=0; i<nTests; ++i) {
		Q total(0);

		bool res = false;
		int L, X;
		cin >> L >> X;

		char str[1024*16];
		cin >> str;

		int iPosition = 0;
		int kPosition = 0;

		//First compute the total multiplication of the string, to ensure it's equal to ijk = -1
		total = O;
		for(int z=0; z<X; z++) {
			for(int j=0; j<L; ++j) {
				Q v(str[j]);
				total = total * v;
				//cout << " = " << total << endl;
			}
		}
		if(total != ijk) {
#ifdef DEBUG
			cout << "Failed at wrong product" << endl;
#endif
			goto end;
		}

		//Now the total product is equal to ijk. Let's find i starting from left
		total = O;
		for(int z=0; z<X; z++) {
			for(int j=0; j<L; ++j) {
				Q v(str[j]);
				//cout << total << "*" << v << " = " << total*v << "(i)" << endl;
				total = total * v;
				iPosition++;

				if(total == I)
					break;

			}
			if(total == I)
				break;
		}

		if(total != I) {
#ifdef DEBUG
			cout << "Failed at couldn't find i " << L << "," << X << endl;
#endif
			goto end;
		}

		//Now the total product is equal to ijk and we have i. Let's find k starting from right
		total = O;
		for(int z=0; z<X; z++) {
			for(int j=0; j<L; ++j) {
				Q v(str[L-j-1]);
				total = v * total;
				kPosition++;

				if(total == K)
					break;
			}
			if(total == K)
				break;
		}

		if(total != K) {
#ifdef DEBUG
			cout << "Failed at couldn't find k" << endl;
#endif
			goto end;
		}

#ifdef DEBUG
			cout << "k = " << kPosition << ", i = " << iPosition << ", X = " << X << ", L = " << L << endl;
#endif
		//We found both i and k, ensure we didn't have to collide to do that
		if( (kPosition+iPosition) > (X*L)) {
			goto end;
		}
		res = true;
end:
		cout << "Case #" << (i+1) << ": " << (res ? "YES" : "NO") << endl;
	}
}
