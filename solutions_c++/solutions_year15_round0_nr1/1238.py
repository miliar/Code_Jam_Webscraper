#include <fstream>
#include <string>

// Standing Ovation

int main() {
	std::ifstream file("input.in");
	std::ofstream out("output.txt");
	int t;
	file >> t;
	int count = 1;

	while (t-- > 0) {
		int answer = 0;
		int standers = 0;
		int smax;
		std::string str;
		file >> smax;
		file >> str;

		for (int i = 0; i <= smax; i++) {
			standers += (int)str.at(i) - 48;
			while (standers <= i) {
				answer++;
				standers++;
			}
		}
		out << "Case #" << count++ << ": " << answer << std::endl;
	}
	return 0;
}