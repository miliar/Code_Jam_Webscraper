#include <stdio.h>
#include <string>
using namespace std;


class MagicProblem {
public:
	unsigned int firstAnswer, secondAnswer;
	unsigned int arangmentOne[4][4], arangmentTwo[4][4];
	void printInput();
	string answer();
	bool firstRowContains(int row, int num);
};

void MagicProblem::printInput() {
	printf("%d\n", firstAnswer);
	for(int y = 0; y<4; ++y) {
		for(int x = 0; x<4; ++x) {
			printf("%d ", arangmentOne[y][x]);
		}
		printf("\n");
	}
	printf("%d\n", secondAnswer);
	for(int y = 0; y<4; ++y) {
		for(int x = 0; x<4; ++x) {
			printf("%d ", arangmentTwo[y][x]);
		}
		printf("\n");
	}
}

bool MagicProblem::firstRowContains(int row, int num) {
	for(int x = 0; x<4; ++x) {
		if(arangmentOne[row][x] == num)
			return true;
	}
	return false;
}

string MagicProblem::answer() {
	string answer;
	int possibility = -1;
	for(int x = 0; x<4; ++x) {
		if(firstRowContains(firstAnswer-1, arangmentTwo[secondAnswer-1][x])) {
			if(possibility != -1) {
				answer = "Bad magician!";
				return answer;
			}
			else
				possibility = arangmentTwo[secondAnswer-1][x];
		}
	}
	if(possibility == -1)
		answer = "Volunteer cheated!";
	else {
		char tmp[2];
		sprintf(tmp, "%d", possibility);
		answer = string(tmp);
	}
	return answer;
}

MagicProblem* readFile(const char* file, int* numCases) {
	FILE* f = fopen(file, "r");
	fscanf(f, "%d\n", numCases);
	MagicProblem* result = new MagicProblem[*numCases];
	for(int i = 0; i<*numCases; ++i) {
		fscanf(f, "%d\n", &result[i].firstAnswer);
		for(int y = 0; y<4; ++y) {
			for(int x = 0; x<4; ++x) {
				fscanf(f, "%d ", &result[i].arangmentOne[y][x]);
			}
			fscanf(f, "\n");
		}
		fscanf(f, "%d\n", &result[i].secondAnswer);
		for(int y = 0; y<4; ++y) {
			for(int x = 0; x<4; ++x) {
				fscanf(f, "%d ", &result[i].arangmentTwo[y][x]);
			}
			fscanf(f, "\n");
		}
	}
	return result;
}

int main(int argc, char** argv) {
	int numProblems = 0;
	MagicProblem* problems = readFile("input", &numProblems);
	for(int i = 0; i<numProblems; ++i) {
		//problems[i].printInput();
		printf("Case #%d: %s\n", i+1, problems[i].answer().c_str());
	}
}
