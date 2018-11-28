#include <fstream>
#include <string>

void solve() {
	std::ifstream inputFile("test.in");
	std::ofstream outFile("test.out");
	if (inputFile.is_open()) {
		int T;;
		inputFile >> T;
		std::string line;
		std::getline(inputFile, line);
		
		for (int i = 0; i < T; i++) {
			
			std::getline(inputFile, line);

			int sum = 0;
			int addition = 0;
			for (int j = 2; j < line.length(); j++) {
				if (j-2>sum) {
					addition += j-2 - sum;
					sum += j-2 - sum;
				}
				sum += line[j] - '0';
			}

			outFile << "Case #" << i+1 << ": " << addition << "\n";
		}
	}
}

int main()
{
	solve();
	return 0;
}

