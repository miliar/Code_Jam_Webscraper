
#include <iostream>
#include <vector>
#include <bitset>

#include <thread>
#include <mutex>


using namespace std;

const int BASE_MIN = 2;
const int BASE_MAX = 10;

const int MAX_TRY_DIVISOR = 65533;

long long divisor(__int128 number) {
	if (number % 2 == 0) return 2;
	if (number % 5 == 0) return 5;

	__int128 d = 1;
	while (d * d < number && d < MAX_TRY_DIVISOR) {
		d += 2; // 3
		if (number % d == 0) return d;

		d += 4; // 7
		if (number % d == 0) return d;

		d += 2; // 9
		if (number % d == 0) return d;

		d += 2; // 11
		if (number % d == 0) return d;
	}
	return 0;
}

const int BINARY_PRINT_LEN = 32;

struct jamcoin {
	long long value;
	long long div[BASE_MAX - BASE_MIN + 1];

	__int128 as(int base) {
		__int128 v = value / 2;
		__int128 res = 1;
		__int128 mul = base;
		while (v > 0) {
			res += mul * (v % 2);
			mul *= base;
			v /= 2;
		}
		return res;
	}

	bool check() {
		for (int base = BASE_MIN; base <= BASE_MAX; base++) {
			__int128 d = divisor(as(base));
			//cout << "divisor for " << value << " in " << base << " is " << ((long long) d) << endl;
			if (d == 0) return false;
			div[base - BASE_MIN] = d;
		}
		return true;
	}

	void print() {
		int length = 2;
		while (value >= (1L << length)) length++;
		
		string coin = "";
		while (length > 0) {
			coin += (value & (1L << (--length))) ? '1' : '0';
		}

		cout << coin << " ";
		for (int base = BASE_MIN; base <= BASE_MAX; base++) {
			cout << div[base - BASE_MIN];
			if (base < BASE_MAX) cout << " "; else cout << endl;
		}
	}
};

mutex mut;
int LENGTH;
size_t COUNT;
vector<jamcoin> coins;

bool testdone() {
	mut.lock();
	bool result = (coins.size() == COUNT);
	mut.unlock();
	return result;
}


void submit(jamcoin j) {
	mut.lock();
	if (coins.size() < COUNT) {
		coins.push_back(j);
	}
	mut.unlock();
}

void mine(long long start, int inc) {
	jamcoin j;
	j.value = start;
	while (!testdone()) {
		if (j.check()) {
			submit(j);
			#ifdef _DOTS
			cout << '.' << flush;
			#endif
		}
		j.value += inc;
	}
}


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":" << endl;

		cin >> LENGTH;
		cin >> COUNT;
		long long start = (1L << (LENGTH - 1)) + 1;
		//cout << "start = " << start << endl;
		
		thread t1(mine, start, 8);
		thread t2(mine, start+2, 8);
		thread t3(mine, start+4, 8);
		thread t4(mine, start+6, 8);

		t1.join();
		t2.join();
		t3.join();
		t4.join();

		#ifdef _DOTS
		cout << endl;
		#endif
		for (jamcoin j : coins) j.print();
	}

	return 0;
}

