#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>

#define wrapper(i) std::cout << "Case #" << i << ": "

std::string build_temp(std::string str) {
	std::string t = "";
	if (str.length() == 0)
		return t;
	t += str[0];
	for (int i=1; i<str.length(); ++i)
		if (str[i] != str[i-1])
			t += str[i];
	return t;
}

int find_closest(int arr[], int size) {
	int sum = 0;
	for (int i=0; i<size; ++i)
		sum += arr[i];
	float mean = (float)sum / size;
	return round(mean);
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	std::cin >> cases;
	for (int test_case=1; test_case<=cases; test_case++) {
		int N, err=0;
		std::string str[100];
		std::cin >> N;
		for (int i=0; i<N; ++i)
			std::cin >> str[i];
		std::string temp = "";
		for (int i=0; i<N; ++i) {
			std::string t = build_temp(str[i]);
			if (temp.length() == 0)
				temp = t;
			else if (temp.compare(t)) {
				++err;
				break;
			}
		}
		int moves = 0;
		wrapper(test_case);
		if (err) {
			std::cout << "Fegla Won" << std::endl;
		}
		else {
			for (int i=0; i<temp.length(); ++i) {
				int count[100] = {};
				for (int j=0; j<N; ++j) {
					int len = str[j].find_first_not_of(temp[i]);
					if (len == -1)
						len = str[j].length();
					count[j] = len;
					str[j].erase(0, count[j]);
				}
				int m = find_closest(count, N);
				for (int j=0; j<N; ++j)
					moves += abs(count[j]-m);
			}
			std::cout << moves << std::endl;
		}

	}

	return 0;
}

