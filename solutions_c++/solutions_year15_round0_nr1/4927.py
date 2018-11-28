#include <fstream>
#include <string>

long T;

long solve(std::string &s) {
	long count = 0;
	long result = 0;
	for (int i = 0; i < (int)s.length(); ++i) {
		if (count < i){
			result += i - count;
			count = i;
		}
		count += s[i] - '0';
	}
	return result;
}

int main() {
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	in >> T;

	std::string buf;

	for (int i = 0; i < T; ++i){
		in >> buf >>  buf;
		out << "Case #" << i + 1 << ": " << solve(buf) << '\n';
	}

	in.close();
	out.close();
}