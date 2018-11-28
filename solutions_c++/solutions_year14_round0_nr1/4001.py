#include <iostream>
#include <vector>

void inputMatrix(std::vector<std::vector<int> > &vec) {
	for (int i = 0; i < 4; i++) {
		for (int j= 0; j < 4; j++) {
			std::cin >> vec[i][j];
		}
	}
}

void printAns(const int row1, const std::vector<std::vector<int> > &vec1, const int row2,  const std::vector<std::vector<int> > &vec2) {
	int numOfCommonElements = 0;
	int commonNum;
	for(int i = 0; i < 4; i++) {
		int num = vec1[row1][i];
		for (int j = 0; j < 4; j++) {
			if (num == vec2[row2][j]) {
				numOfCommonElements ++;
				commonNum = num;
			}
		}
	}
	if (numOfCommonElements == 1) {
		std::cout << commonNum<<"\n";
	} else if (numOfCommonElements > 1) {
		std::cout << "Bad magician!\n";
	} else {
		std::cout << "Volunteer cheated!\n";
	}
}

int main() {
	int t;
	std::cin >> t;
	int count = 1;
	while(t--) {
		int row1, row2;
		std::vector<std::vector<int> > vec1(4, std::vector<int>(4)), vec2(4, std::vector<int>(4));
		std::cin >> row1;
		inputMatrix(vec1);
		std::cin >> row2;
		inputMatrix(vec2);
		std::cout << "Case #" << count <<": ";
		printAns(row1-1, vec1, row2-1, vec2);
		count ++;
	}
}
