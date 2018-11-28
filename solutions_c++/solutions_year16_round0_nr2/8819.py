#include <fstream>
#include <string.h>

using namespace std;

unsigned long long solve(char s[]) {
	int r = 0;
	int len = strlen(s);
	if (len == 0)
		return 0;
	char c = s[0];
	int i = 1;
	do {
		while (i < len && s[i] == c) {
			i++;
		}
		if (i == len) {
			if (s[len - 1] == '+')
				return r;
			else
				return r+1;
		}
		r++;
		c = s[i];
		i++;
	}
	while(true);
	return r;
}

int main(int argc, char *argv[]) {
	// read file
	std::ifstream infile(argv[1]);
	std::ofstream outfile("output.txt");
	unsigned int no_tests;
	infile >> no_tests;
	for (int i = 0; i < no_tests; i++) {
		char s[100] = {0};
		infile >> s;
		int result = solve(s);
		outfile << "Case #" << i+1 << ": " << result << "\n";
	}
	infile.close();
	outfile.close();
	return 0;
}