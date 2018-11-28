#include <bits/stdc++.h>
using namespace std;
#define rep(c) for (int t = 0; t < c; t++)
#define sqr(x) ((x) * (x))
const double Pi = 3.141592653589793238462643383279;
struct point {
	double x, y;
	point() {
		x = y = 0;
	}
	point(double X, double Y) {
		x = X, y = Y;
	}
	void init() {
		scanf("%lf", &x);
		scanf("%lf", &y);
	}
	void show() {
		cout << "(" << x << ";" << y << ")" << endl;
	}
	void to_polar() {
		point r;
		r.x = sqrt(x * x + y * y);
		r.y = atan2(y, x);
		x = r.x;
		y = r.y;
	}
	void to_decart() {
		point r;
		r.x = x * cos(y);
		r.y = x * sin(y);
		x = r.x;
		y = r.y;
	}
	void rotate(double a) {
		point r;
		r.x = (int)(round((x * cos(a) - y * sin(a)) * 10000)) / 10000.;
		r.y = (int)(round((y * cos(a) + x * sin(a)) * 10000)) / 10000.;
		x = r.x;
		y = r.y;
	}
	void rotate(double a, point o) {
		point r;
		r.x = (int)(round((o.x + (x - o.x) * cos(a) - (y - o.y) * sin(a)) * 10000)) / 10000.;
		r.y = (int)(round((o.y + (x - o.x) * sin(a) + (y - o.y) * cos(a)) * 10000)) / 10000.;
		x = r.x;
		y = r.y;
	}
};
point make_point(double X, double Y) {
	point r(X, Y);
	return r;
}
double dist(long long x1, long long y1, long long x2, long long y2) {
	return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}
double dist(point A, point B) {
	return sqrt(pow(B.x - A.x, 2) + pow(B.y - A.y, 2));
}
double vec(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
	return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
}
double scalar(int x1, int y1, int x2, int y2) {
	return x1 * x2 + y1 * y2;
}
long long sum_of_digits(long long n) {
	long long res = 0;
	while (n > 0) {
		res += n % 10;
		n /= 10;
	}
	return res;
}
bool point_in_figure(long long n, long long X1, long long Y1, vector <long long> const & x, vector <long long> const & y) {
	// луч
	long long X2 = X1 + 1000001, Y2 = Y1 + 1;
	long long intersection_count = 0;
	for (long long i = 0; i < n; i++) {
		long long j = (!i ? n - 1 : i - 1);
		double t0 = vec(x[i], y[i], X1, Y1, X2, Y2);
		double t1 = vec(x[j], y[j], X1, Y1, X2, Y2);
		double t2 = vec(X1, Y1, x[i], y[i], x[j], y[j]);
		double t3 = vec(X2, Y2, x[i], y[i], x[j], y[j]);
		if (
				((t0 >= 0 && t1 < 0) || (t0 < 0 && t1 >= 0)) &&
				((t2 >= 0 && t3 < 0) || (t2 < 0 && t3 >= 0))
				)
			intersection_count++;
	}
	return intersection_count % 2 != 0;
}
double area(long long n, vector <point> const & a) {
	double res = 0;
	for (long long i = 1; i < n; i++)
		res += (a[i].x - a[i - 1].x) * (a[i].y + a[i - 1].y);
	res += (a[0].x - a[n - 1].x) * (a[0].y + a[n - 1].y);
	return fabs(res) / 2;
}
double angle(int x1, int y1, int x2, int y2, int x3, int y3) {
	const int ax = x2 - x1;
	const int ay = y2 - y1;
	const int bx = x2 - x3;
	const int by = y2 - y3;
	return acos(
			scalar(ax, ay, bx, by) /
			(sqrt(ax * ax + ay * ay)) * sqrt(bx * bx + by * by)
	);
}
double angle(point a) {
	return atan2(a.y, a.x);
}
long long input() {
	long long n; scanf("%lld", &n); return n;
}
string _input() {
	string s; cin >> s; return s;
}
vector <long long> prefix_function (string s, long long max_prefsuf_len = INT_MAX) {
	long long n = s.size();
	vector <long long> p((int)n);
	for (long long i = 1; i < n; i++) {
		long long j = p[i - 1];
		while (j > 0 && s[i] != s[j])
			j = p[j - 1];
		if (s[i] == s[j]) j++;
		if (j >= max_prefsuf_len) j = max_prefsuf_len;
		p[i] = j;
	}
	return p;
}
bool isprime(long long n) {
	if (!n || n == 1) return 0;
	for (long long i = 2; i * i <= n; i++)
		if (n % i == 0) return 0;
	return 1;
}
string Sum(string a, string b) {
	int l = b.length() - a.length();
	int l1 = a.length() - b.length();
	if (a.length() > b.length())
		for (int i = 0; i < l1; i++)
			b = "0" + b;
	if (b.length() > a.length())
		for (int i = 0; i < l; i++)
			a = "0" + a;
	int buf = 0;
	string res = "";
	for (int i = a.length() - 1; i >= 0; i--){
		char tmp = (((a[i] - '0') + (b[i] - '0') + buf) % 10) + '0';
		res = tmp + res;
		buf = ((a[i] - '0') + (b[i] - '0') + buf) / 10;
	}
	if (buf == 1)
		res = '1' + res;
	return res;
}
string Mul(string a, string b){
	int buf = 0;
	int l = b.length() - a.length();
	int l1 = a.length() - b.length();
	if (a.length() > b.length())
		for (int i = 0; i < l1; i++)
			b = "0" + b;
	if (b.length() > a.length())
		for (int i = 0; i < l; i++)
			a = "0" + a;
	string s_buf("");
	string sum("0");
	int z = 0;
	for (int i = a.length() - 1; i >= 0; i--){
		for (int j = b.length() - 1; j >= 0; j--){
			s_buf += (((a[i] - '0')*(b[j] - '0') + buf) % 10 + '0');
			buf = ((a[i] - '0')*(b[j] - '0') + buf) / 10;
		}
		if (buf != 0)
			s_buf += buf + '0';
		reverse(s_buf.begin(), s_buf.end());
		for (int f = 0; f < z; f++)
			s_buf += '0';
		z++;
		sum = Sum(sum, s_buf);
		s_buf = "";
		buf = 0;
	}
	return sum;
}

int divs_count(int n) {
	set <int> s;
	for (int i = 1; i * i <= n; i++) {
		if (n % i == 0) {
			s.insert(i);
			s.insert(n / i);
		}
	}
	return (int)(s.size());
}

int gcd(int a, int b) {
	while (a != b) {
		if (a > b) {
			a -= b;
		}
		else {
			b -= a;
		}
	}
	return a;
}

bool good(int a[], int n) {
	for (int i = 1; i < n; i++)
		if (gcd(a[i], a[i - 1]) != 1)
			return 0;
	return 1;
}

int main() {
	freopen("Output.txt", "w", stdout);
	int T = input();
	rep(T) {
		int n = input();
		if (!n) {
			printf("Case #%i: INSOMNIA\n", t + 1);
			continue;
		}
		set <int> s;
		int i = 1, ans = 0;
		while (s.size() != 10) {
			int N = n * i;
			ans = N;
			while (N) {
				s.insert(N % 10);
				N /= 10;
			}
			i++;
		}
		printf("Case #%i: %i\n", t + 1, ans);
	}
}