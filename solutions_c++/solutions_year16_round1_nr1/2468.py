#include <iostream>
#include <string>


int main() {
    int T;
    std::cin >> T;
    std::string s, res;
    res.resize(3000);
    int beg, end, i, n_case = 1;
    while (T--) {
	std::cin >> s;
	// [)
	beg = end = 1500;
	i = 0;
	res[--beg] = s[i++];
	for (; i < s.size(); i++) {
	    if (s[i] < res[beg])
		res[end++] = s[i];
	    else
		res[--beg] = s[i];
	}
	std::cout << "Case #" << n_case++ << ": " << res.substr(beg, end-beg) << std::endl;
    }

    return 0;
}
