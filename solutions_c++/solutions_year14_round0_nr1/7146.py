#include <fstream>
#include <vector>
#include <iostream>


int main(int argc, char* argv[])
{
	std::ifstream fin(argv[1]);
	std::vector<int> x;

	int T;
	fin >> T;
	for (int t=0; t<T; t++) {
		int answer1;
		fin >> answer1;
		answer1--;
		typedef int Cards[4][4];
		Cards cards1;
		for (int row=0; row<4; row++) {
			for (int col=0; col<4; col++) {
				fin >> cards1[row][col];
			}
		}

		int answer2;
		fin >> answer2;
		answer2--;
		typedef int Cards[4][4];
		Cards cards2;
		for (int row=0; row<4; row++) {
			for (int col=0; col<4; col++) {
				fin >> cards2[row][col];
			}
		}

		std::vector<int> answer;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (cards1[answer1][i] == cards2[answer2][j]) {
					answer.push_back(cards1[answer1][i]);
				}
			}
		}

		switch (answer.size()) {
		case 0:
			std::cout << "Case #" << t+1 << ": " << "Volunteer cheated!" << "\n";
			break;
		case 1:
			std::cout << "Case #" << t+1 << ": " << answer[0] << "\n";
			break;
		default:
			std::cout << "Case #" << t+1 << ": " << "Bad magician!" << "\n";
			break;
		}
	}

	return 0;
}
