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
namespace code_jam_2015_0_a {
#endif

using namespace std;

int solve(){
    int s;
    string persons;
    cin >> s >> persons;
    int levelCnt = s + 1;
    int prevLevelPerson = 0;
    int invitedPerson = 0;
    for(int level = 0; level < levelCnt; level++){

        int currentLevelPerson = (int)(persons[level] - '0');

        // pass
        if(prevLevelPerson >= level ){
            prevLevelPerson += currentLevelPerson;
            continue;
        }

        // non pass
        int minInvted = level - prevLevelPerson;
        invitedPerson += minInvted;
        prevLevelPerson += (minInvted + currentLevelPerson);
    }

    return invitedPerson;
}

int main(){
	int T;
	cin >> T;

	for(int testCaseNo = 1; testCaseNo <= T; ++testCaseNo){
	    int ret = solve();
	    cout << "Case #" << testCaseNo << ": " << ret << endl;
	}
	return 0;
}

#ifdef CUTE_PLATFORM
#ifdef CUTE_MAIN_RUNNER
CUTE_MAIN(__FILE__, main);
#endif
}
#endif
