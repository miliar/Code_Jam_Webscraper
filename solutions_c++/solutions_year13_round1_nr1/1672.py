#include <iostream>
#include <string>
#include <stdint.h>

using std::cin;
using std::cout;
using std::string;

int main()
{
    int n;

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin >> n;

    for(size_t i = 0; i < n; ++i) {
		uint64_t r;
		int64_t t;
		uint64_t k = -1;

		cin >> r >> t;
		++r;
		while(t >= 0) {
			++k;
			t -= (2 * r - 1);
			r += 2;
		}
				
		cout << "Case #" << i+1 << ": ";
		cout << k << std::endl;
	}

    return 0;
}
