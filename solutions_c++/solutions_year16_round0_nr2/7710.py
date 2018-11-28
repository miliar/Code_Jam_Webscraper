
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> read_input() {

	std::vector<std::string> input_buffer;
	while (!std::cin.eof()) {
		std::string s;
		std::cin >> s;
		if (!s.empty()) {
			input_buffer.push_back(std::move(s));
		}
	}

	return input_buffer;
}

template <class T>
void output_answer(int no, T ans) {
	std::cout << "Case #" << no << ": " << ans << std::endl;
}

int check(const std::string& input) {
	int count = 0;
	std::string s = input + '+';
	char current = s.front();
	for (char c : s) {
		if (current != c) {
			++count;
		}
		current = c;
	}
	return count;
}

int main(void) {
	std::ios::sync_with_stdio(false);

	std::string s;
	std::cin >> s;
	int T = std::stoi(s);
	const auto input_buffer = std::move(read_input());

	int c = 0;
	for (const auto& input : input_buffer) {
		++c;
		int ans = check(input);
		output_answer(c, ans);
	}

	return 0;

}
