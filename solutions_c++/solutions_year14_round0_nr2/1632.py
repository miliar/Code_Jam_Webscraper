#include <stdio.h>
#include <string>
using namespace std;


class CookieProblem {
public:
	long double c, f, x;
	void printInput();
	string answer();
	CookieProblem() {
		currentRate = 2.0;
		factoryTime = 0.0;
	}
	bool shouldBuildNewFactory();
	long double timeToWin();
private:
	long double currentRate;
	long double factoryTime;
};

void CookieProblem::printInput() {
	printf("%Lf %Lf %Lf\n", c, f, x);
}

long double CookieProblem::timeToWin() {
	return factoryTime + x/currentRate;
}

bool CookieProblem::shouldBuildNewFactory() {
	CookieProblem next = *this;
	next.factoryTime += next.c/next.currentRate;
	next.currentRate += next.f;
	return (this->timeToWin() > next.timeToWin());
}

string CookieProblem::answer() {
	string answer;
	while(true) {
		if(shouldBuildNewFactory()) {
			factoryTime += c/currentRate;
			currentRate += f;
		}
		else {
			char tmp[500];
			sprintf(tmp, "%.7Lf", timeToWin());
			answer = string(tmp);
			return answer;
		}
	}
}

CookieProblem* readFile(const char* file, int* numCases) {
	FILE* f = fopen(file, "r");
	fscanf(f, "%d\n", numCases);
	CookieProblem* result = new CookieProblem[*numCases];
	for(int i = 0; i<*numCases; ++i) {
		fscanf(f, "%Lf %Lf %Lf\n", &result[i].c, &result[i].f, &result[i].x);
	}
	return result;
}

int main(int argc, char** argv) {
	int numProblems = 0;
	CookieProblem* problems = readFile("input", &numProblems);
	for(int i = 0; i<numProblems; ++i) {
		//problems[i].printInput();
		printf("Case #%d: %s\n", i+1, problems[i].answer().c_str());
	}
}
