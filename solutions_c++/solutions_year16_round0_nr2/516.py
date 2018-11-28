#include <iostream>
#include <string>

int main() {
    int T, n_case = 1, res;
    std::string s;
    std::cin >> T;
    while (T--) {
	res = 0;
	std::cin >> s;
	std::cout << "Case #" << n_case << ": ";
	n_case++;
	bool flip = false;
	for (auto c = s.rbegin(); c != s.rend(); c++) {
	    if ((!flip && *c == '-') || (flip && *c == '+')) {
		flip = !flip;
		res++;
	    }
	}
	std::cout << res << std::endl;
    }

    return 0;
}
