#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

template<typename T>
struct Quaternion {
	T real;
	T i;
	T j;
	T k;
	Quaternion(const T real = 0, const T i = 0, const T j = 0, const T k = 0)
		: real(real), i(i), j(j), k(k) {
	}

	Quaternion(const char c) : Quaternion() {
		switch (c) {
			case 'i':
				i = T(1);
				break;
			case 'j':
				j = T(1);
				break;
			case 'k':
				k = T(1);
				break;
			default:
				assert(false);
		}
	}

	Quaternion operator*(const Quaternion<T> &rhs) const {
/*		(a+bi+cj+dk) * (e+fi+gj+hk)
		ae + afi + agj + ahk
		ebi - bf + bgk - bhj
		cej - cfk - cg + chi
		dek + dfj - dgi - dh
*/
		Quaternion result;
		result.real = real*rhs.real - i*rhs.i - j*rhs.j - k*rhs.k;
		result.i = real*rhs.i + i*rhs.real + j*rhs.k - k*rhs.j;
		result.j = real*rhs.j - i*rhs.k + j*rhs.real + k*rhs.i;
		result.k = real*rhs.k + i*rhs.j - j*rhs.i + k*rhs.real;

		return result;
	}

	bool operator==(const Quaternion<T> &rhs) const {
		return real == rhs.real &&
			i == rhs.i &&
			j == rhs.j &&
			k == rhs.k;
	}
};
template<typename T>
ostream & operator<<(ostream &os, const Quaternion<T> q) {
	os << "(";
	if (q.real) os << ((q.real > 0) ? "1" : "-1");
	if (q.i) os << ((q.i > 0) ? "i" : "-i");
	if (q.j) os << ((q.j > 0) ? "j" : "-j");
	if (q.k) os << ((q.k > 0) ? "k" : "-k");
	os << ")";
}

typedef Quaternion<int> Quat;
typedef vector<Quat> MyVec;

bool CanSolve(const MyVec &input) {
	const Quat I(0, 1, 0, 0);
	const Quat K(0, 0, 0, 1);

	MyVec lefts(input.size());

	lefts[0] = input[0];
	for (int i = 1; i < input.size(); ++i) {
		lefts[i] = lefts[i-1] * input[i];
	}

	MyVec rights(input.size());
	rights[input.size() - 1] = input[input.size() - 1];
	for (int i = input.size() - 2; i >= 0; --i) {
		rights[i] = input[i] * rights[i+1];
	}

	for (auto q : input) {
		cerr << q << ", ";
	}
	cerr << endl;

	for (auto q : lefts) {
		cerr << q << ", ";
	}
	cerr << endl;

	for (auto q : rights) {
		cerr << q << ", ";
	}
	cerr << endl;

	bool has_i = false;
	bool has_k = false;
	for (int i = 0; i < input.size() - 1; ++i) {
		if (!has_i) {
			cerr << "comparing " <<  lefts[i] << " and " << rights[i+1] << endl;
			if (lefts[i] == I && rights[i+1] == I) {
				has_i = true;
				cerr << "has i" << endl;
			}
		} else {
			cerr << "comparing " <<  lefts[i] << " and " << rights[i+1] << endl;
			if (lefts[i] == K && rights[i+1] == K) {
				has_k = true;
				cerr << "has k" << endl;
				break;
			}
		}
	}

	return has_k;
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;

	for(int t = 0; t < T; ++t) {
		long long L, X;
		cin >> L >> X;
		string s;
		cin >> s;
		assert(s.size() == L);
		string rep_s;
		for (int x = 0; x < X; ++x) {
			rep_s += s;
		}

		MyVec quaternions(rep_s.begin(), rep_s.end());
		if (CanSolve(quaternions)) {
			cout << "Case #" << (t+1) << ": YES" << endl;
		} else {
			cout << "Case #" << (t+1) << ": NO" << endl;
		}
	}

	return 0;
}

