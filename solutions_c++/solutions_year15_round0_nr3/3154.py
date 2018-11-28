

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
#include <boost/math/quaternion.hpp>
#include <boost/mpl/list.hpp>

#include <boost/units/pow.hpp>
#include <boost/units/quantity.hpp>
#include <boost/units/io.hpp>

using namespace std;
using boost::math::quaternion;

typedef unsigned long long ull;

const static string kProblemSet = "small";

string seek(vector<boost::math::quaternion<char> > &ar) {
    quaternion<char> as(1,0,0,0);
    for (ull i = 0; i < ar.size(); i++) {
        as *= ar[i];
    }
    if (as.R_component_1() == -1) {
        quaternion<char> left(1,0,0,0);
        for (ull i = 0; i < ar.size(); i++) {
            left *= ar[i];
            
            if (left.R_component_2() == 1) {
                quaternion<char> middle(1,0,0,0);
                for (ull j = i+1; j < ar.size(); j++) {
                    middle *= ar[j];
                    if (middle.R_component_3() == 1) {
                        return "YES";
                    }
                }
            }
            
        }
    }
    return "NO";
}

int main(int argc, const char * argv[]) {
    
    
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        unsigned long long X, L;
        ifs >> L >> X;
        vector<quaternion<char> > text;
        
        for (unsigned long long i = 0; i < L; i++) {
            char buf = 0;
            ifs >> buf;
            switch (buf) {
                case 'i':
                    text.push_back( quaternion<char>(0,1,0,0) );
                    break;
                case 'j':
                    text.push_back( quaternion<char>(0,0,1,0) );
                    break;
                case 'k':
                    text.push_back( quaternion<char>(0,0,0,1) );
                    break;
                default:
                    break;
            }
            

        }
        vector<quaternion<char> > XL = text;
        for (ull i = 1; i < X; i++) {
            XL.insert( XL.end(), text.begin(), text.end() );
        }
        assert(XL.size() == X*L);
        
        
        string ret = seek(XL);
        
        
        cout << "Case #" << testCase+1 << ": " << ret << endl;
        ofs << "Case #" << testCase+1 << ": " << ret << endl;
    }
    
	return 0;
}
