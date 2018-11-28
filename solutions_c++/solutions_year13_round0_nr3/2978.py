#include <assert.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <time.h>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/
int intLength(__int64 i) {
    int result = 1; 

    while (i > 9) {
        i /= 10; 
        result ++; 
    }

    return result; 
}

int getNumAtPos(__int64 i, int p) {
    int l = intLength(i); 
    i /= pow(double(10), l - p); 
    if (i > 9)
        i %= 10; 

    return i; 
}

bool isPalin(__int64 i) {
    int l = 1, r = intLength(i); 
    int len = r; 
    bool result = true; 
    while (l < r) {
        if (getNumAtPos(i, l) != getNumAtPos(i, r)) {
            result = false;
            break;
        }

        l++, r--;
    }

    return result; 
}

int main(int argc, char* argv[]) {
    
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

    // srand(time(NULL));

	string ln;  
    inf >> ln;

    int number = atoi(ln.c_str());
    
	for (int cases=0; cases<number; cases++) 
    {
        __int64 a = 0, b = 0; 
        inf >> ln; sscanf(ln.c_str(), "%i64d", &a); 
        inf >> ln; sscanf(ln.c_str(), "%i64d", &b); 

        __int64 aa = sqrt(double(a)); aa += (fabs(sqrt(double(a)) - aa) > 1e-10 ? 1 : 0); 
        __int64 bb = sqrt(double(b)); 

        __int64 result = 0; 
        for (__int64 i = aa; i<=bb; i++) {
            if (isPalin(i) && isPalin(i * i)) 
                result++;
        }

        // print result
        cout << "Case #" << (cases + 1) << ": " << result << endl;
	}

	return 0;
}
