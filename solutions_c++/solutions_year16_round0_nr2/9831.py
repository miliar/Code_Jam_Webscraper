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

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef CUTE_PLATFORM
namespace code_jam_2016_b {
#endif

using namespace std;

void removeTailHappies(string& pancakes){
    while(!pancakes.empty()){
        int last = pancakes.size() - 1;
        if(pancakes[last] == '+'){
            pancakes.pop_back();
        }else{
            break;
        }
    }
}

void flipPancakes(string& pancakes){
    int cnt = pancakes.size();
    for(int i = 0; i < cnt; ++i){
        if(pancakes[i] == '-'){
            pancakes[i] = '+';
        }else{
            pancakes[i] = '-';
        }
    }
}

int main(){
	int T;
	cin >> T;

	for(int testCaseNo = 1; testCaseNo <= T; ++testCaseNo){
	    string pancakes;
	    cin >> pancakes;

	    int cnt = 0;
        removeTailHappies(pancakes);
	    while(!pancakes.empty()){
	        flipPancakes(pancakes);
	        removeTailHappies(pancakes);
	        cnt++;
	    }

	    cout << "Case #" << testCaseNo << ": " << cnt << endl;
	}
	return 0;
}

#ifdef CUTE_PLATFORM
#ifdef CUTE_MAIN_RUNNER
CUTE_MAIN(__FILE__, main);
#endif
}
#endif
