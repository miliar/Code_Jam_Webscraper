#include <iostream>
#include <string>
#include <list>

std::string do_work(const std::string &n) {
	std::list<char> res;
	for (const auto &it : n)
		if (res.size() && *res.begin() > it)
			res.push_back(it);
		else
			res.push_front(it);
	return std::string(res.begin(), res.end());
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::string n;
		std::cin >> n;
		std::cout << "Case #" << i << ": " << do_work(n) << std::endl;
	}
	return 0;
}
