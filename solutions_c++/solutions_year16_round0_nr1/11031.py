#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;



const static string kProblemSet = "large";

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        unsigned long long N = 0, tmp0 = 0, tmp1 = 0;
        ifs >> N;
        
        if (N == 0) {
            cout << "Case #" << testCase+1 << ": " << "INSOMNIA" << endl;
            ofs << "Case #" << testCase+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        
        int digits = 0;
        while(digits != (1 << 10) -1){
            tmp1 = (tmp0 += N);
            while(tmp1) {
                digits = digits | (1 << (tmp1%10));
                tmp1 /= 10;
            }
        }
        
        cout << "Case #" << testCase+1 << ": " << tmp0 << endl;
        ofs << "Case #" << testCase+1 << ": " << tmp0 << endl;
    }
    
	return 0;
}
