#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

#define TRACE(fmt,x) {fprintf(stderr,fmt,x);fprintf(stderr,"\n");}
#define CASE(a,b) fprintf(stderr, "%d / %d = %.2f | %.2f\n", a, b, (double)clock()/CLOCKS_PER_SEC, ((double)clock()/a*b)/CLOCKS_PER_SEC);

class Quat {
public:
	short int w, i, j, k;

	Quat(int _w, int _i, int _j, int _k) {
		w = _w; i = _i; j = _j; k = _k;
	}
	Quat(char s) {
		w = i = j = k = 0;
		if (s == 'i') i = 1;
		if (s == 'j') j = 1;
		if (s == 'k') k = 1;
	}

	Quat operator * (const Quat& r) const {
		if (this->w == 1)  return Quat( r.w,  r.i,  r.j,  r.k);;
		if (this->w == -1) return Quat(-r.w, -r.i, -r.j, -r.k);
		if (this->i == 1)  return Quat(-r.i,  r.w, -r.k,  r.j);
		if (this->i == -1) return Quat( r.i, -r.w,  r.k, -r.j);
		if (this->j == 1)  return Quat(-r.j,  r.k,  r.w, -r.i);
		if (this->j == -1) return Quat( r.j, -r.k, -r.w,  r.i);
		if (this->k == 1)  return Quat(-r.k, -r.j,  r.i,  r.w);
		if (this->k == -1) return Quat( r.k,  r.j, -r.i, -r.w);
		return Quat(0,0,0,0);	// never
	}

	Quat operator + (const Quat& r) const {
		return Quat(this->w + r.w, this->i + r.i, this->j + r.j, this->k + r.k);
	}

	bool is_i() {
		return (w == 0 && i == 1 && j == 0 && k == 0);
	}
	bool is_j() {
		return (w == 0 && i == 0 && j == 1 && k == 0);
	}
	bool is_k() {
		return (w == 0 && i == 0 && j == 0 && k == 1);
	}

	bool is_ijk() {
		return (w == 0 && i == 1 && j == 1 && k == 1);
	}

	friend ostream& operator<<(ostream& os, const Quat& q)
	{
		os << "(";
		if (q.w > 0) os << 1;
		else if (q.w < 0) os << -1;

		if (q.i > 0) os << "i";
		else if (q.i < 0) os << "-i";

		if (q.j > 0) os << "j";
		else if (q.j < 0) os << "-j";

		if (q.k > 0) os << "k";
		else if (q.k < 0) os << "-k";

		os << ')';
		return os;
	}

};

/*

6
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i
4 3
kiij

*/

string solve(string s, int L, int X) {
	int F = L*X;

	Quat q1(1, 0, 0, 0), q2(1, 0, 0, 0), q3(1, 0, 0, 0);

	int i=0;
	while (!q1.is_i() && i < F) {
		q1 = q1 * Quat(s.at(i%L));
		i++;
	}

	while (q1.is_i() && !q2.is_j() && i < F) {
		q2 = q2 * Quat(s.at(i%L));
		i++;
	}

	while (q2.is_j() && i < F) {
		q3 = q3 * Quat(s.at(i%L));
		i++;
	}

	if (q3.is_k()) return "YES";

	return "NO";
}

int main() {
	int T;
	cin >> T;

	for (int t=1; t<=T; t++) {
		int L, X;
		cin >> L >> X;

		string q;
		cin >> q;

		cout << "Case #" << t << ": " << solve(q, L, X) << endl;

		//CASE(t,T)
	}

	return 0;
}
