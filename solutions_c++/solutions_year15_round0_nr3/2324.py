#include <vector>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class QTN{
	// real i j k
	int a, b, c, d;
public:
	QTN() {}
	QTN(int a, int b, int c, int d) : a(a), b(b), c(c), d(d) {}
	QTN operator*(int x) const { return QTN(a*x,b*x,c*x,d*x); }
	QTN operator*(QTN x) const {
		int a1 = a, a2 = x.a, 
			b1 = b, b2 = x.b, 
			c1 = c, c2 = x.c, 
			d1 = d, d2 = x.d;
		return QTN( a1*a2-b1*b2-c1*c2-d1*d2,
					a1*b2+b1*a2+c1*d2-d1*c2,
					a1*c2-b1*d2+c1*a2+d1*b2,
					a1*d2+b1*c2-c1*b2+d1*a2
				  );
	}
	QTN & operator*=(QTN x) { *this = *this * x; return *this; }
	bool operator==(QTN x) { return a == x.a && b == x.b && c == x.c && d == x.d; }
	bool operator!=(QTN x) { return !((*this) == x); }
} ONE(1, 0, 0, 0), I(0, 1, 0, 0), J(0, 0, 1, 0), K(0, 0, 0, 1),
	_ONE(-1, 0, 0, 0), _I(0, -1, 0, 0), _J(0, 0, -1, 0), _K(0, 0, 0, -1);

QTN toQTN(char c) {
	switch (c){
		case 'i': return I;
		case 'j': return J;
		case 'k': return K;
		default: break;
	}
}

bool solve(int L, long long X, const string & str)
{
	long long posI(-1), posK(-1);
	QTN prod = ONE, revprod = ONE;

	QTN tmp = ONE;
	for (int i = 0; i != L; ++i) {
		tmp *= toQTN(str[i%L]);
	}
	
	if (tmp == ONE) return false;
	else if (tmp == _ONE) {
		if (X % 2 != 1) return false;
	}
	else if (X % 4 != 2) return false;
	
	for (int i = 0; i != 4 * L; ++i) {
		prod *= toQTN(str[i%L]);
		if (prod == I)
		{
			posI = i + 1;
			break;
		}
	}

	for (int i = 0; i != 4 * L; ++i) {
		revprod = toQTN(str[L - 1 - (i%L)]) * revprod;
		if (revprod == K) {
			posK = X*L - i;
			break;
		}
	}

	//cout << posI << endl;
	//cout << posK << endl;

	return  posI > 0 && posK > 0 && posI < posK && posI <= X*L;
}

void test() {
	QTN one(1,0,0,0), i(0,1,0,0),j(0, 0, 1, 0), k(0,0,0,1);
	cout << ((j * i) == (k * -1)) << endl;
	cout << ((j * j) == (one * -1)) << endl;
	cout << ((j * k) == i) << endl;
}

inline string YESNO(bool flag){ return flag ? string("YES") : string("NO"); }

void run() {
	//ifstream fin("C-test-in.txt");
	//ifstream fin("C-small-in.txt");
	ifstream fin("C-large-in.txt");
	//ofstream fout("C-test-out.txt");
	//ofstream fout("C-small-out.txt");
	ofstream fout("C-large-out.txt");

	unsigned LINE;
	fin >> LINE;

	int L; long long X; string str;
	//cout << LINE;
	for (unsigned line = 0; line != LINE; ++line)
	{
		fin >> L >> X;
		fin >> str;
		//cout << mx;
		fout << "Case #" << line + 1 << ": " << YESNO(solve(L, X, str)) << endl;
	}
	fout.close();
}

int main(){
	run();
	return 0;

}