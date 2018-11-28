#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

std::string s;

bool relax (std::vector<int>& v) {
    int i = v.size()-1;
    while (i >= 0 && v[i] + 2 + 2 * (v.size()-1-i) >= s.size()-1) {
	s[v[i]] = '0';
	i--;
    }
    if (i < 0) return false;
    s[v[i]] = '0';
    v[i] += 2;
    s[v[i++]] = '1';
    while (i < v.size()) {
	v[i] = v[i-1]+2;
	s[v[i++]] = '1';
    }
    return true;
}

int main() {
    int T, N, J;
    std::cin >> T >> N >> J;
    std::vector<int> even, odd;
    s.resize(N);
    std::cout << "Case #1:\n";
    while (J > 0) {
	std::fill (s.begin(), s.end(), '0');
	s.back() = '1';
	s.front() = '1';
	for (auto i : even)
	    s[i] = '1';
	for (auto i : odd)
	    s[i] = '1';
	do {
	    std::cout << s;
	    for (int i = 3; i < 12; i++)
		std::cout << ' ' << i;
	    std::cout << std::endl;
	    J--;
	} while (relax (odd) && J > 0);
	if (!relax (even)) {
	    even.push_back(0);
	    odd.push_back(0);
	    for (int i = 2, j = 0; j < even.size(); j++, i+=2) {
		even[j] = i;
		odd[j] = i-1;
	    }
	}
	for (int i = 2, j = 0; j < even.size(); j++, i+=2) {
	    odd[j] = i-1;
	}
    }

    return 0;
}
