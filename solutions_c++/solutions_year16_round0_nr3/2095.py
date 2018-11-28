#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
#include <cassert>

class weird_num {
private:
	std::vector<int> x;
public:
	weird_num(int size) : x(size) {
		assert(size > 4);
		fill(x.begin(), x.end(), 0);
		x[0] = x[x.size() - 1] = 1;
	}
	bool divisable_by(int radix, int by) const {
		int result = 0;
		for (int i = 0; i < x.size(); ++i) {
			result = (result*radix + x[i]) % by;
		}
		return (result % by) == 0;
	}
	weird_num operator++() {
		int carry = 1;
		for (int i = x.size() - 2; (i >= 0) && carry ; --i) {
			int s = x[i] + carry;
			x[i] = s & 1;
			carry = s >> 1;
		}
		assert(x[0] == 1);
		return *this;
	}
	void to_stream(std::ostream& os) const {
		std::copy(x.begin(), x.end(), std::ostream_iterator<int>(os));
	}
};

using namespace std;

ostream& operator<<(ostream& os, const weird_num& wn) {
	wn.to_stream(os);
	return os;
}

int find_divisor(const weird_num& n, int radix) {
	const int candidates[7] = { 3, 5, 7, 11, 13, 17, 19 };
	for (int i = 0; i < 7; ++i) {
		if (n.divisable_by(radix, candidates[i]))
			return candidates[i];
	}
	return 0;
}

int main()
{
	int divisors[11] = { 0 };
	int casen, N, J;
	cin >> casen >> N >> J;
	assert(casen == 1);

	weird_num t(32);
	if (N != 32) {
		t = weird_num(N);
	}

	cout << "Case #1:\n";

	int found = 0;
	while (found < J) {
		bool good = true;
		for (int radix = 2; (radix <= 10) && good; ++radix) {
			divisors[radix] = find_divisor(t, radix);
			good = good && divisors[radix];
		}
		if (good) {
			cout << t;
			for (int radix = 2; radix <= 10; ++radix) {
				cout << " " << divisors[radix];
			}
			cout << '\n';
			++found;
		}
		++t;
	}

    return 0;
}

