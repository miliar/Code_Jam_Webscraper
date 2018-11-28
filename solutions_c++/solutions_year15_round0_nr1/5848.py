#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
#include <string.h>
using namespace std;

#define SQ(x) ((x)*(x))

class Problem {
public:
    //problem variables
    int* levels;
    int maxShy;
    Problem() {
	
    }
    string answer();
    void printInput();
private:
	//internal variables/functions
};

void Problem::printInput() {
    printf("\n");
}


string Problem::answer() {
    //solve problem
    int numFriends = 0;
    int numP = 0;
    for(int i = 0; i<=maxShy; ++i) {
	int j = i-numP;
	if(j > 0) {
	    numFriends += j;
	    numP += j;
	}
	numP += levels[i];
    }
    //return answer
    char tmp[50];
    sprintf(tmp, "%d", numFriends);
    return string(tmp);
}

Problem* readFile(const char* file, int* numCases) {
    FILE* f = fopen(file, "r");
    fscanf(f, "%d", numCases);
    Problem* result = new Problem[*numCases];
    for(int i = 0; i<*numCases; ++i) {
	fscanf(f, "\n%d ", &result[i].maxShy);
	result[i].levels = new int[result[i].maxShy+1];
	for(int j = 0; j<=result[i].maxShy; ++j) {
	    char k;
	    fscanf(f, "%c", &k);
	    result[i].levels[j] = k - '0';
	}
    }
    return result;
}

int main(int argc, char** argv) {
    int numProblems = 0;
    Problem* problems = readFile("input", &numProblems);
    for(int i = 0; i<numProblems; ++i) {
#ifdef TEST_READING
	problems[i].printInput();
#else
	printf("Case #%d: %s\n", i+1, problems[i].answer().c_str());
#endif
    }
}
