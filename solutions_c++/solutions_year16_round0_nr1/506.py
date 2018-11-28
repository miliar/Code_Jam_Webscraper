#include <iostream>
#include <vector>
#include <algorithm>


int main() {
    std::vector<bool> vb (10);
    int T, i;
    int n_case = 1;
    std::cin >> T;
    while (T--) {
	std::cin >> i;
	std::cout << "Case #" << n_case << ": ";
	n_case++;
	if (i == 0) {
	    std::cout << "INSOMNIA\n";
	    continue;
	}
	int t = 1, n = 0, mul, j;
	std::fill (vb.begin(), vb.end(), false);
	for (; n < 10; t++) {
	    mul = i * t;
	    while (mul) {
		j = mul % 10;
		mul /= 10;
		if (!vb[j]) {
		    vb[j] = true;
		    n++;
		}
	    }
	}
	std::cout << (t-1) * i << std::endl;
    }

    return 0;
}
