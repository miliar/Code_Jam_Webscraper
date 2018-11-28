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
		size_t n;
		cin >> n;

		size_t standing = 0;
		size_t invited = 0;

		for (size_t i = 0; i <= n; ++i) {
			char ch;
			cin >> ch;

			size_t p = (size_t)(ch - '0');
			if (i > standing) {
				invited += i - standing;
				standing += i - standing;
			}

			standing += p;
		}

		cout << "Case #" << testIndex + 1 << ": " << invited << endl;
	}

	return 0;
}
