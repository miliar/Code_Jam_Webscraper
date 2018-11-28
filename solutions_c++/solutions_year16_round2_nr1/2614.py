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
namespace code_jam_2016_1b_a {
#endif

using namespace std;

void removeAndAdd(size_t pos, const string& src, string& input, int value, vector<int>& ret){
    input.erase(pos, 1);
    for(int i = 0; i < src.size(); ++i){
        pos = input.find(src[i]);
        input.erase(pos, 1);
    }
    ret.push_back(value);
}

bool procLevel1(string& input, vector<int>& ret){
    size_t pos = input.find('Z');
    if(pos != string::npos){
        removeAndAdd(pos, "ERO", input, 0, ret);
        return true;
    }

    pos = input.find('W');
    if(pos != string::npos){
        removeAndAdd(pos, "TO", input, 2, ret);
        return true;
    }

    pos = input.find('U');
    if(pos != string::npos){
        removeAndAdd(pos, "FOR", input, 4, ret);
        return true;
    }

    pos = input.find('X');
    if(pos != string::npos){
        removeAndAdd(pos, "SI", input, 6, ret);
        return true;
    }

    pos = input.find('G');
    if(pos != string::npos){
        removeAndAdd(pos, "EIHT", input, 8, ret);
        return true;
    }

    return false;
}

bool procLevel2(string& input, vector<int>& ret){
    size_t pos = input.find('F');
    if(pos != string::npos){
        removeAndAdd(pos, "IVE", input, 5, ret);
        return true;
    }
    pos = input.find('S');
    if(pos != string::npos){
        removeAndAdd(pos, "EVEN", input, 7, ret);
        return true;
    }
    return false;
}

bool procLevel3(string& input, vector<int>& ret){
    size_t pos = input.find('O');
    if(pos != string::npos){
        removeAndAdd(pos, "NE", input, 1, ret);
        return true;
    }
    pos = input.find('T');
    if(pos != string::npos){
        removeAndAdd(pos, "HREE", input, 3, ret);
        return true;
    }
    pos = input.find('I');
    if(pos != string::npos){
        removeAndAdd(pos, "NNE", input, 9, ret);
        return true;
    }
    return false;
}
string solve(string& input){
    vector<int> ret;

    while(procLevel1(input, ret)){}
    while(procLevel2(input, ret)){}
    while(procLevel3(input, ret)){}

    sort(ret.begin(), ret.end());
    string retStr;
    for(int i = 0; i < ret.size(); ++ i) {
        retStr.push_back(ret[i] + '0');
    }
    return retStr;
}

int main(){
	int T;
	cin >> T;

	for(int testCaseNo = 1; testCaseNo <= T; ++testCaseNo){
	    string S;
	    cin >> S;
	    string ret = solve(S);
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
