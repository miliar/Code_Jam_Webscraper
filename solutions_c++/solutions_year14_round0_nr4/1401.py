#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


class WarProblem {
public:
	vector<double> naomiBlocks;
	vector<double> kenBlocks;
	void printInput();
	string answer();
	WarProblem() {
	}
private:
	int deceitfulScore();
	int warScore();
	bool deceitfulMove();
	bool move();
	vector<double> dnBlocks, dkBlocks;
};

void WarProblem::printInput() {
	for(int i = 0; i<naomiBlocks.size(); ++i) {
		printf("%lf ", naomiBlocks[i]);
	}
	printf("\n");
	for(int i = 0; i<kenBlocks.size(); ++i) {
		printf("%lf ", kenBlocks[i]);
	}
	printf("\n");
}

bool WarProblem::move() {
	//naomi plays biggest
	double nBiggest = naomiBlocks[naomiBlocks.size()-1];
	int nIndex = -1;
	//have a block bigger then naomi's biggest?
	for(int i = 0; i <kenBlocks.size(); ++i) {
		if(kenBlocks[i] > nBiggest)
			nIndex = i;
	}
	if(nIndex >= 0) {
	//yes - ken plays smallest bigger then namoi's biggest
		naomiBlocks.pop_back();
		kenBlocks.erase(kenBlocks.begin()+nIndex);
		return false;
	}
	else {
	//no - ken plays smallest
		naomiBlocks.pop_back();
		kenBlocks.erase(kenBlocks.begin());
		return true;
	}
}

bool WarProblem::deceitfulMove() {
	double kSmallest = dkBlocks[0];
	int nIndex = -1;
	//have a block bigger then ken's smallest?
	for(int i = 0; i < dnBlocks.size(); ++i) {
		if(dnBlocks[i] > kSmallest) {
			nIndex = i;
			break;
		}
	}
	if(nIndex >= 0) {
	//yes - naomi play smallest block bigger then kens smallest but tell ken its big
	//ken will play smallest
		dnBlocks.erase(dnBlocks.begin()+nIndex);
		dkBlocks.erase(dkBlocks.begin());
		return true;
	}
	else {
	//no - naomi play smallest block but tell ken its big
	//ken plays biggest block
		dnBlocks.erase(dnBlocks.begin());
		dkBlocks.pop_back();
		return false;
	}
}

int WarProblem::deceitfulScore() {
	int score = 0;
	dnBlocks = naomiBlocks;
	dkBlocks = kenBlocks;
	while(dnBlocks.size() != 0) {
		if(deceitfulMove())
			++score;
	}
	return score;
}

int WarProblem::warScore() {
	int score = 0;
	while(naomiBlocks.size() != 0) {
		if(move())
			++score;
	}
	return score;
}

string WarProblem::answer() {
	sort(naomiBlocks.begin(), naomiBlocks.end());
	sort(kenBlocks.begin(), kenBlocks.end());
	int dScore = deceitfulScore();
	int score = warScore();
	char tmp[50];
	sprintf(tmp, "%d %d", dScore, score);
	return string(tmp);
}
/*string WarProblem::answer() {
	int dwarScore = 0;
	int warScore = 0;
	sort(naomiBlocks.begin(), naomiBlocks.end());
	sort(kenBlocks.begin(), kenBlocks.end());
	for(int i = naomiBlocks.size()-1; i>=0; --i) {
		if(naomiBlocks[i]  > kenBlocks[i])
			++dwarScore;
	}
	warScore = dwarScore/2;
	char tmp[50];
	sprintf(tmp, "%d %d", dwarScore, warScore);
	return string(tmp);
}*/

WarProblem* readFile(const char* file, int* numCases) {
	FILE* f = fopen(file, "r");
	fscanf(f, "%d\n", numCases);
	WarProblem* result = new WarProblem[*numCases];
	for(int i = 0; i<*numCases; ++i) {
		int numBlocks;
		double tmpBlock;
		fscanf(f, "%d\n", &numBlocks);
		for(int j = 0; j<numBlocks-1; ++j) {
			fscanf(f, "%lf ", &tmpBlock);
			result[i].naomiBlocks.push_back(tmpBlock);
		}
		fscanf(f, "%lf\n", &tmpBlock);
		result[i].naomiBlocks.push_back(tmpBlock);
		for(int j = 0; j<numBlocks-1; ++j) {
			fscanf(f, "%lf ", &tmpBlock);
			result[i].kenBlocks.push_back(tmpBlock);
		}
		fscanf(f, "%lf\n", &tmpBlock);
		result[i].kenBlocks.push_back(tmpBlock);
	}
	return result;
}

int main(int argc, char** argv) {
	int numProblems = 0;
	WarProblem* problems = readFile("input", &numProblems);
	for(int i = 0; i<numProblems; ++i) {
		//problems[i].printInput();
		printf("Case #%d: %s\n", i+1, problems[i].answer().c_str());
	}
}
