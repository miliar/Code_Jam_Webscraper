#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool check(std::string s) {
	std::vector<bool> letters;
	letters.resize(200);
	letters[s[0]] = true;
	for(int i = 1; i < s.size(); i++) {
		if(letters[s[i]] && s[i-1] != s[i])
			return false;
		letters[s[i]] = true;
	}
	return true;
}

int main() {
	int t;
	std::cin >> t;
	for(int h = 1; h <= t; h++) {
		int n;
		std::cin >> n;
		std::string temp;
		std::vector<std::string> cars;
		for(int i = 0; i < n; i++) {
			std::cin >> temp;
			cars.push_back(temp);
		}
		std::sort(cars.begin(), cars.end());
		int result = 0;
		std::vector<int> numbers;
		for(int i = 0; i < cars.size(); i++)
			numbers.push_back(i);
		do {
			std::string tocheck;
			for(int i = 0; i < numbers.size(); i++)
				tocheck += cars[numbers[i]];
			result += check(tocheck);
			if(result == 1000000007)
				result = 0;
		} while(std::next_permutation(numbers.begin(), numbers.end()));
		printf("Case #%d: %d\n", h, result);
	}
	return 0;
}
