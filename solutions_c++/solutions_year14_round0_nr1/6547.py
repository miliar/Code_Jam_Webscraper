//
//  main.cpp
//  GCJ2014QAA


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



const static string kProblemSet = "small";

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        int f_r, s_r, tmp;
        set<int> f_s, s_s;
        ifs >> f_r;
        for (int i = 0; i < (f_r-1)*4; i++) {
            ifs >> tmp;
        }
        for (int i = 0; i < 4; i++) {
            ifs >> tmp;
            f_s.insert(tmp);
        }
        for (int i = 0; i < (4-f_r)*4; i++) {
            ifs >> tmp;
        }
        
        ifs >> s_r;
        for (int i = 0; i < (s_r-1)*4; i++) {
            ifs >> tmp;
        }
        for (int i = 0; i < 4; i++) {
            ifs >> tmp;
            s_s.insert(tmp);
        }
        for (int i = 0; i < (4-s_r)*4; i++) {
            ifs >> tmp;
        }
        
        
        set<int> intersect;
        set_intersection(f_s.begin(),f_s.end(),s_s.begin(),s_s.end(),
                         std::inserter(intersect,intersect.begin()));
        
        string ans;
        if (intersect.size() == 1) ans = std::to_string( *intersect.begin() );
        else if (intersect.size() == 0) ans = "Volunteer cheated!";
        else ans = "Bad magician!";
        
        cout << "Case #" << testCase+1 << ": " << ans << endl;
        ofs << "Case #" << testCase+1 << ": " << ans << endl;
    }
    
	return 0;
}
