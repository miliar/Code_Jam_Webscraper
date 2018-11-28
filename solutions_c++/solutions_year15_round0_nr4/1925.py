#include <bits/stdc++.h>
#include <stdint.h>
using namespace std;

typedef uint8_t byte;
typedef int16_t i16;
typedef uint16_t ui16;
typedef int32_t i32;
typedef uint32_t ui32;
typedef int64_t i64;
typedef uint64_t ui64;

#define MOD 1000000007
#define ADD_MOD(a, b) (((a) + (b)) % MOD)
#define MUL_MOD(a, b) i32((i64(a) * i64(b)) % MOD)
#define SUB_MOD(a, b) ((a) >= (b) ? (a) - (b) : (a) + MOD - (b))

int main() {
	ios_base::sync_with_stdio(false);

	size_t testCount;
	cin >> testCount;

	for (size_t testIndex = 0; testIndex < testCount; ++testIndex) {
		size_t n, w, h;
		cin >> n >> w >> h;

		size_t maxSize = n >= 3 ? 2 : 1;

		bool first = false;
		if (maxSize > w || maxSize > h) {
			first = true;
		} else if (n > w && n > h) {
			first = true;
		} else if ((w * h) % n != 0) {
			first = true;
		} else if (n == 4 && max(w, h) == 4 && min(w, h) == 2) {
			first = true;
		}

		cout << "Case #" << testIndex + 1 << ": " << (first ? "RICHARD" : "GABRIEL") << endl;
	}

	return 0;
}
