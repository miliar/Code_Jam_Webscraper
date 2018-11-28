#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <string>

using namespace std;

// --------------------- Template ---------------------------------------------

#define FOR(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define FORN(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T, class IT>
inline void PRINT(IT i1, IT i2) {
    cout << '['; copy(i1, i2, ostream_iterator<T>(cout, ", ")); cout << "]\n";
}

#if defined(M_H_HOME) && (0)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

struct quat {
	int sign;
	char v;
	quat(int s, char val) : sign(s), v(val) { }
	quat() : sign(1), v('1') { } 
};

quat mul(const quat& a, const quat& b) {
	char v = '\0';
	int sign_ = 1;
	switch (a.v) {
		case '1' : v = b.v;
				   break;
		case 'i' : switch (b.v) {
		              case '1' : v = 'i'; break;
					  case 'i' : v = '1'; sign_ = -1; break;
					  case 'j' : v = 'k'; break;
					  case 'k' : v = 'j'; sign_ = -1; break;
					  default  : throw 2;
				   }
				   break;
		case 'j' : switch (b.v) {
		              case '1' : v = 'j'; break;
					  case 'i' : v = 'k'; sign_ = -1; break;
					  case 'j' : v = '1'; sign_ = -1; break;
					  case 'k' : v = 'i'; break;
					  default  : throw 2;
				   }
				   break;
		case 'k' : switch (b.v) {
		              case '1' : v = 'k'; break;
					  case 'i' : v = 'j'; break;
					  case 'j' : v = 'i'; sign_ = -1; break;
					  case 'k' : v = '1'; sign_ = -1; break;
					  default  : throw 2;
				   }
				   break;
		default  : throw 1;  
	}
	return quat(a.sign * b.sign * sign_, v);
}

// lrev(x) mul x == 1
quat lrev(const quat& x) {
	return x.v == '1' ? x : quat(-x.sign, x.v);
}

bool operator==(const quat& a, const quat& b) {
	return a.sign == b.sign && a.v == b.v;
}


int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("c.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    int T;
	cin >> T;
	FORN(casen, T) {
		bool result = false;
        int L, X;
		cin >> L >> X;
		string str, res;
		cin >> str;
		FORN(i, X) {
			res = res + str;
		}
		vector<quat> fwd(res.size());
		quat tmp(1, '1');
		FORN(i, fwd.size()) {
			fwd[i] = mul(tmp, quat(1, res.at(i)));
			tmp = fwd[i];
		}
		tmp = quat(1, '1');
		for (int k = res.size() - 1; k >= 2; --k) {
			tmp = mul(quat(1, res.at(k)), tmp);
			if (tmp == quat(1, 'k')) {
				// look for i and j
				for (int i = 0; i <= k - 2; ++i) { // i is the last symbol
					if (fwd[i] == quat(1, 'i') && (mul(lrev(fwd[i]), fwd[k-1]) == quat(1, 'j'))) {
						result = true;
						goto bail;
						break;
					}
				}
			}
		}
		bail: ;
		cout << "Case #" << casen+1 << ": " << (result ? "YES" : "NO" ) << endl; 
	}

    return 0;
}
