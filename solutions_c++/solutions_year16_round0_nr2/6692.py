
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
	freopen("C:\\Users\\Beauty\\Downloads\\B-large.in", "r", stdin);
	freopen("out0.txt", "w", stdout);

	int num_case, t;
	cin >> num_case; num_case++;

	int n, i, j, len, res;
	char s[1000], c;
	
	loopi(t, num_case, 1)
	{
		cin >> s;
		len = strlen(s);
		res = 0;
		i = 1;
		c = s[0];

		if (len == 1) {
			if (c == '-')
				res++;
		}
		else {
			while (1) {
				while (i < len && s[i] == c) i++;
				if (i < len) {
					c = s[i];
					j = 0;
					res++;
					while (j < i) s[j++] = c;
				}
				else {
					if (s[0] == '-') res++;
					break;
				}
			}
		}

		cout << "Case #" << t << ": ";
		cout << res << endl;
	}

	return 1;
}