// Problem C. Fair and Square

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

static bool isFair(size_t x)
{
	ostringstream ss;
	ss << x;
	string s(ss.str());
	return equal(s.begin(), s.end(), s.rbegin());
}

static size_t makeFair(size_t w, int even)
{
	stringstream ss;
	ss << w;
	string s(ss.str());
	string t(s.rbegin() + (even > 0 ? 0 : 1), s.rend());
	s.append(t);
	ss.str(s);
	size_t x;
	ss >> x;
	assert(ss);
	return x;
}

static size_t doDigits(unsigned n,
	size_t xa, size_t xb, size_t ya, size_t yb)
{
	size_t count = 0;
	size_t wa = pow(10.0, double(n));
	size_t wb = pow(10.0, double(n+1));
	for (int i = 0; i < 2; ++i) {
		for (size_t w = wa; w < wb; ++w) {
			size_t x = makeFair(w, i);
			size_t y = x * x;
			if (x > xb || y > yb)
				return count;
			//xxx assert(xa <= x && x <= xb);
			assert(isFair(x));
			if (ya <= y && y <= yb && isFair(y)) {
				//xxx cout << "xxx x y " << x << '\t' << y << '\n';
				count++;
			}
		}
	}
	return count;
}

static const size_t testcase()
{
	assert(cin);
	size_t ya, yb;
	cin >> ya >> yb;
	assert(cin);
	size_t count = 0;
	size_t xa = ceil(sqrt(ya));
	size_t xb = floor(sqrt(yb));
	size_t na = floor(log10(xa) / 2);
	size_t nb = ceil(log10(xb) / 2);
	//xxx cout << "xxx na " << na << ' ' << nb << '\n';
	for (size_t n = na; n <= nb; ++n)
		count += doDigits(n, xa, xb, ya, yb);
	return count;
}

int main()
{
	unsigned n;
	cin >> n;
	assert(cin);
	for (unsigned i = 0; i < n; ++i)
		cout << "Case #" << i+1 << ": " << testcase() << '\n';
	return 0;
}
