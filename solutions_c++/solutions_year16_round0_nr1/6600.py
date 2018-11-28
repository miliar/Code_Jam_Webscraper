
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

#pragma region
typedef unsigned int uint;
typedef unsigned char byte;
typedef unsigned short ushort;
typedef long long  ll;
typedef unsigned long long  ull;
#pragma endregion

#define loop(_i, _n) for( _i = 0; _i < _n; _i++)
#define loopi(_i, _n, _s) for( _i = _s; _i < _n; _i++)

int main(int argc, char* argv[]) {
	freopen("C:\\Users\\Beauty\\Downloads\\A-large.in", "r", stdin);
	freopen("out0.txt", "w", stdout);

	int num_case, t;
	cin >> num_case; num_case++;

	unsigned long long i, res, v, l;
	int n, o, k, nums[10] = { 0 };

	loopi(t, num_case, 1)
	{
		cin >> n;
		if (!n) { cout << "Case #" << t << ": INSOMNIA\n"; continue; }

		memset(nums, 0, sizeof(nums));
		l = i = n;

		while (i) {
			v = i;
			while (v) {
				k = v % 10;
				if (!nums[k]) { nums[k] = 1; l = i; }
				v /= 10;
			}

			loop(o, 10) if (!nums[o]) break;
			if (o == 10) break; 
			i += n;
		}

		cout << "Case #" << t << ": ";
		cout << l << endl;
	}

	return 1;
}