
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
        
        int ret = 0;
        int sum = 0;
        int smax = 0;
        ifs >> smax;
        for (int i = 0; i <= smax; i++) {
            char buf = 0;
            ifs >> buf;
            int si = buf-'0';
            if (i <= sum) {
                sum += si;
            }else {
                ret += (i-sum);
                sum += si + (i-sum);
            }
        }
        
        cout << "Case #" << testCase+1 << ": " << ret << endl;
        ofs << "Case #" << testCase+1 << ": " << ret << endl;
    }
    
	return 0;
}
