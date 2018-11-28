// Problem A. Bullseye

#include <cassert>
#include <iostream>

using namespace std;

static unsigned testcase()
{
	uint64_t r, t;
	cin >> r >> t;
	assert(cin);
	uint64_t n = 0;
	while (t > 0) {
		uint64_t x = 2 * r + 1;
		if (t < x)
			break;
		t -= x;
		r += 2;
		n++;
	}
	return n;
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
