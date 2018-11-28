//#define CUTE_PLATFORM
//#define CUTE_MAIN_RUNNER

#ifdef CUTE_PLATFORM
#include "cute_algostudy.h"
#endif

#include <string>
#include <vector>
#include <iostream>

#include <map>
#include <set>
#include <algorithm>

#include <sstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef CUTE_PLATFORM
namespace code_jam_2016_0_a {
#endif

using namespace std;

void fillNumSet(long long value, set<int>& numSet){
    std::ostringstream oss;
    oss << value;
    string changed = oss.str();
    for(int i = 0; i < changed.size(); ++i){
        numSet.insert(changed[i]);
    }
}

int main(){
	int T;
	cin >> T;

	for(int testCaseNo = 1; testCaseNo <= T; ++testCaseNo){
	    long long startNum;
	    cin >> startNum;
	    if(startNum == 0){
	        cout << "Case #" << testCaseNo << ": " << "INSOMNIA" << endl;
	        continue;
	    }

	    set<int> numSet;
	    long long countingNum = 0;
	    while(true){
	        countingNum += startNum;
	        fillNumSet(countingNum, numSet);
	        if(numSet.size() == 10){
	            break;
	        }
	    }
	    cout << "Case #" << testCaseNo << ": " << countingNum << endl;
	}
	return 0;
}

#ifdef CUTE_PLATFORM
#ifdef CUTE_MAIN_RUNNER
CUTE_MAIN(__FILE__, main);
#endif
}
#endif
