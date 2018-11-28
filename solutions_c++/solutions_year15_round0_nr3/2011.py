#include <iostream>
using namespace std;

struct quaternion {
	quaternion() : r(1), i(0), j(0), k(0) {}
	quaternion(int r) : r(r), i(0), j(0), k(0) {}
	quaternion(int r, int i, int j, int k) : r(r), i(i), j(j), k(k) {}
	quaternion(char c) : quaternion(c == '1', c == 'i', c == 'j', c == 'k') {}
	int r, i, j, k;
};

quaternion operator*(const quaternion& q1, const quaternion& q2) {
	return quaternion(q1.r * q2.r - q1.i * q2.i - q1.j * q2.j - q1.k * q2.k,
	                  q1.r * q2.i + q1.i * q2.r + q1.j * q2.k - q1.k * q2.j,
	                  q1.r * q2.j - q1.i * q2.k + q1.j * q2.r + q1.k * q2.i,
	                  q1.r * q2.k + q1.i * q2.j - q1.j * q2.i + q1.k * q2.r);
}


bool operator==(const quaternion& q1, const quaternion& q2) {
	return (q1.r == q2.r && q1.i == q2.i && q1.j == q2.j && q1.k == q2.k);
}

ostream & operator<< (ostream &os, const quaternion &q) {
	return (os << q.r << " " << q.i << "i " << q.j << "j " << q.k << endl);
}

 
struct s_punkt {
	s_punkt() : x(0), y(0) {}
	s_punkt(int x, int y) : x(x), y(y) {}
	int x, y;
	string wlasciciel;
};


quaternion wynp[10005];
quaternion wynk[10005];


int main() {
	ios_base::sync_with_stdio();
	int t, l, x;
	bool odp;
	string s;
	cin >> t;
	for(int tn = 1; tn <= t; tn ++) {
		cin >> l >> x >> s;
		odp = false; 
		for(int i = 0; i < l * x; i ++) {
			wynp[i + 1] = wynp[i] * s[i % l];
		}
		for(int i = 1; i <= l * x && !odp; i ++) {
			if(wynp[i] == 'i') {
				for(int j = i + 1; j < l * x && !odp; j ++) {
					if(wynp[i] * 'j' == wynp[j] && wynp[j] * 'k' == wynp[l * x]) {
						odp = true;
					}
				} 
			}
		}
		cout << "Case #" << tn << ": " << (odp ? "YES" : "NO") << endl;
	}
}
