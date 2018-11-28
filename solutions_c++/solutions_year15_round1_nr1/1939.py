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
    int N;
    int* mush;
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
    int min1 = 0;
    for(int i = 1; i<N; ++i) {
	if(mush[i-1] - mush[i] > 0)
	    min1 += mush[i-1] - mush[i];
    }
    
    int min2 = 0;
    int max = 0;
    for(int i = 1; i<N; ++i) {
	if(mush[i-1] - mush[i] > max)
	    max = mush[i-1] - mush[i];
    }
    
    for(int i = 0; i<N-1; ++i) {
	min2 += min(mush[i], max);
    }
    
    //return answer
    char tmp[50];
    sprintf(tmp, "%d %d", min1, min2);
    return string(tmp);
}

Problem* readFile(const char* file, int* numCases) {
    FILE* f = fopen(file, "r");
    fscanf(f, "%d", numCases);
    Problem* result = new Problem[*numCases];
    for(int i = 0; i<*numCases; ++i) {
	fscanf(f, "\n%d\n", &result[i].N);
	result[i].mush = new int[result[i].N];
	fscanf(f, "%d", &result[i].mush[0]);    
	for(int j = 1; j<result[i].N; ++j)
	    fscanf(f, " %d", &result[i].mush[j]);    
	    
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
