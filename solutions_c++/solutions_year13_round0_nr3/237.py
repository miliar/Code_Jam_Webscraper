#include <stdlib.h>
#include <iostream>
#include <stdlib.h>
#include <gmp.h>
using namespace std;

class gmp_int {
public:
	mpz_t n;
// コンストラクタ
	gmp_int() {
		mpz_init(n);
	};
	gmp_int(char *c) {
		mpz_init(n);
		mpz_set_str(n, c, 10);
	};
	gmp_int (const gmp_int &m) {
		mpz_init(n);
		mpz_init_set(n, m.n);
	};
	gmp_int (const int i) {
		mpz_init(n);
		mpz_set_si(n, i);
	};
	gmp_int (const unsigned int i) {
		mpz_init(n);
		mpz_set_ui(n, i);
	};
	gmp_int (const signed long long int i) {
		mpz_init(n);
		char c[30];
		_i64toa_s(i, c, 30, 10);
		mpz_set_str(n, c, 10);
	};
	gmp_int (const unsigned long long int i) {
		mpz_init(n);
		char c[30];
		_ui64toa_s(i, c, 30, 10);
		mpz_set_str(n, c, 10);
	};
	gmp_int (const int i, const int d) {
		mpz_init2(n, d);
		mpz_set_si(n, i);
	};
// デスクトラクタ
	~gmp_int() {
		mpz_clear(n);
	};
// 代入
	gmp_int & operator = (const gmp_int & s) {
		mpz_set(n, s.n);
		return *this;
	};
	gmp_int & operator = (const signed int & s) {
		mpz_set_si(n, s);
		return *this;
	};
	gmp_int & operator = (const unsigned int & s) {
		mpz_set_ui(n, s);
		return *this;
	};
// 加算
	gmp_int & operator += (const gmp_int & s) {
		mpz_add(n, n, s.n);
		return *this;
	};
	gmp_int & operator += (const unsigned int & s) {
		mpz_add_ui(n, n, s);
		return *this;
	};
// 減算
	gmp_int & operator -= (const gmp_int & s) {
		mpz_sub(n, n, s.n);
		return *this;
	};
	gmp_int & operator -= (const unsigned int & s) {
		mpz_sub_ui(n, n, s);
		return *this;
	};
// 乗算
	gmp_int & operator *= (const gmp_int & s) {
		mpz_mul(n, n, s.n);
		return *this;
	};
	gmp_int & operator *= (const signed int & s) {
		mpz_mul_si(n, n, s);
		return *this;
	};
	gmp_int & operator *= (const unsigned int & s) {
		mpz_mul_ui(n, n, s);
		return *this;
	};
// 除算
	gmp_int & operator /= (const gmp_int & s) {
		mpz_fdiv_q(n, n, s.n);
		return *this;
	};
	gmp_int & operator /= (const unsigned int & s) {
		mpz_fdiv_q_ui(n, n, s);
		return *this;
	};
// 剰余
	gmp_int & operator %= (const gmp_int & s) {
		mpz_fdiv_r(n, n, s.n);
		return *this;
	};
	gmp_int & operator %= (const unsigned int & s) {
		mpz_fdiv_r_ui(n, n, s);
		return *this;
	};
// インクリメント・デクリメント
	gmp_int & operator++(int) {
		mpz_add_ui(n, n, 1);
		return *this;
	}
	gmp_int & operator--(int) {
		mpz_sub_ui(n, n, 1);
		return *this;
	}

	unsigned int get_pure_ulong() {
		return mpz_get_ui(n);
	};
	long long int GetS64() {
		static char tmp[100];
		mpz_get_str(tmp, 10, n);
		return _atoi64(tmp);
	};
};

gmp_int operator + (const gmp_int & s1, const gmp_int & s2) {
	gmp_int d("0");
	mpz_add(d.n, s1.n, s2.n);
	return d;
}

gmp_int operator - (const gmp_int & s1, const gmp_int & s2) {
	gmp_int d("0");
	mpz_sub(d.n, s1.n, s2.n);
	return d;
}

gmp_int operator * (const gmp_int & s1, const gmp_int & s2) {
	gmp_int d("0");
	mpz_mul(d.n, s1.n, s2.n);
	return d;
}

gmp_int operator / (const gmp_int & s1, const gmp_int & s2) {
	gmp_int d("0");
	mpz_fdiv_q(d.n, s1.n, s2.n);
	return d;
}

gmp_int operator % (const gmp_int & s1, const gmp_int & s2) {
	gmp_int d("0");
	mpz_fdiv_r(d.n, s1.n, s2.n);
	return d;
}

bool operator <= (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) <= 0;
}

bool operator < (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) < 0;
}

bool operator >= (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) >= 0;
}

bool operator > (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) > 0;
}

bool operator == (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) == 0;
}

bool operator != (const gmp_int & s1, const gmp_int & s2) {
	return mpz_cmp(s1.n, s2.n) != 0;
}

ostream& operator<< (ostream& os, const gmp_int& s) {
	return os << mpz_get_str(NULL, 10, s.n);
}

gmp_int Pow(const gmp_int & b, unsigned int e) {
	gmp_int d;
	mpz_pow_ui(d.n, b.n, e);
	return d;
}

gmp_int PowMod(const gmp_int & b, const gmp_int & e, const gmp_int & m) {
	gmp_int d;
	mpz_powm(d.n, b.n, e.n, m.n);
	return d;
}

gmp_int Sqrt(const gmp_int & b) {
	gmp_int d;
	mpz_sqrt(d.n, b.n);
	return d;
}

gmp_int GCD(gmp_int x, gmp_int y){
	return x != 0 ? GCD(y % x, x) : y;
}

void Itoa(char * str, int base, const gmp_int & s) {
	mpz_get_str(str, base, s.n);
}

class gmp_float {
public:
	mpf_t n;
	static void SetPrecision(int prec) {
		mpf_set_default_prec(prec);
	}
	static int GetPrecision() {
		return mpf_get_default_prec();
	}
// コンストラクタ
	gmp_float() {
		mpf_init(n);
	};
	gmp_float(char *c) {
		mpf_init_set_str(n, c, 10);
	};
	gmp_float (const gmp_float &m) {
		mpf_init_set(n, m.n);
	};
	gmp_float (const int i) {
		mpf_init_set_si(n, i);
	};
	gmp_float (const unsigned int i) {
		mpf_init_set_ui(n, i);
	};
	gmp_float (const long long int i) {
		static char tmp[100];
		_i64toa_s(i, tmp, 100, 10);
		mpf_init_set_str(n, tmp, 10);
	};
	gmp_float (const double d) {
		mpf_init_set_d(n, d);
	};
// デスクトラクタ
	~gmp_float() {
		mpf_clear(n);
	};
// 代入
	gmp_float & operator = (const gmp_float & s) {
		mpf_set(n, s.n);
		return *this;
	};
	gmp_float & operator = (const signed int & s) {
		mpf_set_si(n, s);
		return *this;
	};
	gmp_float & operator = (const unsigned int & s) {
		mpf_set_ui(n, s);
		return *this;
	};
// キャスト
	operator int() {
		return mpf_get_si(n);
	};
// 加算
	gmp_float & operator += (const gmp_float & s) {
		mpf_add(n, n, s.n);
		return *this;
	};
	gmp_float & operator += (const unsigned int & s) {
		mpf_add_ui(n, n, s);
		return *this;
	};
// 減算
	gmp_float & operator -= (const gmp_float & s) {
		mpf_sub(n, n, s.n);
		return *this;
	};
	gmp_float & operator -= (const unsigned int & s) {
		mpf_sub_ui(n, n, s);
		return *this;
	};
// 乗算
	gmp_float & operator *= (const gmp_float & s) {
		mpf_mul(n, n, s.n);
		return *this;
	};
	gmp_float & operator *= (const int & s) {
		mpf_mul_ui(n, n, (unsigned int)s);
		return *this;
	};
	gmp_float & operator *= (const unsigned int & s) {
		mpf_mul_ui(n, n, s);
		return *this;
	};
	gmp_float & operator *= (const double & s) {
		gmp_float d(s);
		mpf_mul(n, n, d.n);
		return *this;
	};
// 除算
	gmp_float & operator /= (const gmp_float & s) {
		mpf_div(n, n, s.n);
		return *this;
	};
	gmp_float & operator /= (const unsigned int & s) {
		mpf_div_ui(n, n, s);
		return *this;
	};
	gmp_float & operator /= (const double & s) {
		gmp_float d(s);
		mpf_div(n, n, d.n);
		return *this;
	};
// 剰余
// 値の変換
	double GetDouble() {
		return mpf_get_d(n);
	};
};

gmp_float operator + (const gmp_float & s1, const gmp_float & s2) {
	gmp_float d("0");
	mpf_add(d.n, s1.n, s2.n);
	return d;
}

gmp_float operator - (const gmp_float & s1, const gmp_float & s2) {
	gmp_float d("0");
	mpf_sub(d.n, s1.n, s2.n);
	return d;
}

gmp_float operator * (const gmp_float & s1, const gmp_float & s2) {
	gmp_float d("0");
	mpf_mul(d.n, s1.n, s2.n);
	return d;
}

gmp_float operator * (const gmp_float & s1, const int & s2) {
	gmp_float d("0");
	mpf_mul_ui(d.n, s1.n, s2);
	return d;
}

gmp_float operator / (const gmp_float & s1, const gmp_float & s2) {
	gmp_float d("0");
	mpf_div(d.n, s1.n, s2.n);
	return d;
}

gmp_float operator / (const gmp_float & s1, const int & s2) {
	gmp_float d("0");
	mpf_div_ui(d.n, s1.n, s2);
	return d;
}

bool operator <= (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) <= 0;
}

bool operator < (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) < 0;
}

bool operator >= (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) >= 0;
}

bool operator > (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) > 0;
}

bool operator == (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) == 0;
}

bool operator != (const gmp_float & s1, const gmp_float & s2) {
	return mpf_cmp(s1.n, s2.n) != 0;
}

ostream& operator<< (ostream& os, const gmp_float& s) {
	return os << mpf_out_str(NULL, 10, 20, s.n);
}

gmp_float Pow(const gmp_float & b, unsigned int & i) {
	gmp_float d("0");
	mpf_pow_ui(d.n, b.n, i);
	return d;
}

gmp_float Sqrt(const gmp_float & b) {
	gmp_float d("0");
	mpf_sqrt(d.n, b.n);
	return d;
}

gmp_float Sqrt(const unsigned int & i) {
	gmp_float d("0");
	mpf_sqrt_ui(d.n, i);
	return d;
}

gmp_float Floor(const gmp_float & b) {
	gmp_float d("0");
	mpf_floor(d.n, b.n);
	return d;
}

char * GetStr(const gmp_float &b, int &e, char * c) {
	long int tmp;
	char * buf = mpf_get_str(c, &tmp, 10, 400000, b.n);
	e = tmp;
	return buf;
}

