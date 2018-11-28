#include <iostream>
#include <vector>

#define FOR(it, seq) for(auto it : seq)
#define FORI(it, beg, end) for(auto it = beg; it != end; ++it)

#define DBG(x) cout << x
#define DBGV(v) {cout << "["; FOR(i_, v) {DBG(i_); cout << ", ";} cout << "]" << endl; }

using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef vector<lint> VL;

typedef unsigned int jamcoin_t;

int T;

void print(jamcoin_t j) {
	int idx = 0;
	while ((j >> idx)) {
		++idx;
	}
	FORI(i, 0, idx) {
		cout << (j >> (idx - i - 1) & 0x1);
	}
}

lint get_value(jamcoin_t j, int base) {
	lint value = 0;
	lint order = 1;
	while (j > 0) {
		value += order * (j&1);
		order *= base;
		j >>= 1;
	}

	return value;
}

lint get_divisor(lint value) {
	for (lint d = 2; d*d <= value; ++d) {
		if (value % d == 0) {
			//cout << "D: " << value << ", " << d << endl;
			return d;
		}
	}
	return 0;
}

bool is_jamcoin(jamcoin_t j, lint divisors[]) {
	FORI(base, 2, 11) {
		lint d = get_divisor(get_value(j, base));
		if (d == 0) {
			return false;
		}
		divisors[base] = d;
	}
	return true;
}

void generate(int J, int N) {
	lint divisors[11];
	jamcoin_t boundary = (0x1 << (N-1)) | 0x1;
	FORI(i, 0, 1<<(N-2)) {
		if (J == 0) {
			break;
		}
		jamcoin_t j = boundary | (i << 1);
		//print(j);
		//cout << endl;

		if (is_jamcoin(j, divisors)) {
			print(j);
			J -= 1;
			cout << " ";
			FORI(base, 2, 11) {
				cout << divisors[base];
				if (base < 10) {
					cout << " ";
				}
			}
			cout << endl;
		}
	}
}


int main(int argc, char *argv[])
{
	int J, N;
	cin >> T;

	FORI(t, 0, T) {
		cout << "Case #" << (t+1) << ": " << endl;
		cin >> N >> J;

		generate(J, N);

		//cout << endl;
	}


	return 0;
}
