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
    int X, R, C;
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
    string r = "RICHARD";
    string g = "GABRIEL";
    
    
    if(X == 1)
	return g;
    //if(R*C%X != 0)
	//return r;
    
    if(R == 1) {
	if( C== 1) {
	    if( X > 1)
		return r;
	}
	if( C == 2) {
	    if( X <= 2)
		return g;
	    else
		return r;
	}
	if( C == 3) {
	    if( X == 2 || X == 4 || X == 3)
		return r;
	    else
		return g;
	}
	if( C == 4) {
	    if( X <= 2)
		return g;
	    else
		return r;
	}
    }

    if(R == 2) {
	if(C == 2) {
	    if( X <= 2)
		return g;
	    else
		return r;
	}
	if(C == 3) {
	    if(X<= 3)
		return g;
	    else
		return r;
	}
	else if(C == 4) {
	    if( X == 3 || X == 4)
		return r;
	    else
		return g;
	}
    }
    if( R == 3) {
	if( C == 3) {
	    if( X==2 || X == 4)
		return r;
	    else 
		return g;
	}
	if( C == 4) {
	    return g;
	}
    }
    if ( R == 4) {
	if(C == 4) {
	    if( X == 3)
		return r;
	    else
		return g;
	}
    }
    int tmp = R;
    R = C;
    C = tmp;
    return answer();
}

Problem* readFile(const char* file, int* numCases) {
    FILE* f = fopen(file, "r");
    fscanf(f, "%d", numCases);
    Problem* result = new Problem[*numCases];
    for(int i = 0; i<*numCases; ++i) {
	fscanf(f, "\n%d %d %d", &result[i].X, &result[i].R, &result[i].C);
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
