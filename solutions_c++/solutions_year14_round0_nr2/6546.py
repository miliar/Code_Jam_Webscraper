

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
    cout.setf(ios::fixed);
    ofs.setf(ios::fixed);
    cout.precision(7);
    ofs.precision(7);
	int T = 0;
    
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        double C, F, X, s = 0, nc = 0, cps = 2;
        ifs >> C >> F >> X;
        while (1) {
            if (nc < C) {
                if ((X-nc)/cps < (C-nc)/cps) {
                    s += (X-nc)/cps;
                    nc = X;
                    break;
                }else {
                    s += (C-nc)/cps;
                    nc = C;
                }
            }else {
                if ((X-nc)/cps < (X-nc+C)/(cps+F)) {
                    s += (X-nc)/cps;
                    nc = X;
                    break;
                }else {
                    cps+=F;
                    s += C/cps;
                }
            }
            

        }
        
        cout << "Case #" << testCase+1 << ": " << s << endl;
        ofs << "Case #" << testCase+1 << ": " << s << endl;
    }
    
	return 0;
}
