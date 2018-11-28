
//darshan.sonde
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <sstream>
#include <limits>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

string processTestCase(long long t);

template<typename T>
std::ostream &operator <<(std::ostream &os, const std::vector<T> &v) {
    using namespace std;
    copy(v.begin(), v.end(), ostream_iterator<T>(os, " "));
    return os;
}

int main(int argc, char **argv)
{
    long long testcases;
    cin >> testcases;
    
    for(long long t=1;t<=testcases;t++) {
        string output =  processTestCase(t);
        cout << "Case #" << t << ": " << output << endl;
    }
    return 0;
}

//============================================


string processTestCase(long long t)
{
    stringstream ss;
    ss.precision(7);
   
    double C,F,X;
    cin >> C >> F >> X;

    double T = 0;
    double b = 2; 

    int dbg = 0;
    time_t start;
    time(&start);
    while(C/b < X/b) {
        dbg++;
        cerr << dbg << " time(" << difftime(start,time(NULL)) << ") NEXTSUM:" << (C/b)+(X/(b+F))<< " CURSUM:" << T+(X/b) << " T:" << T << " b:" << b << endl;
        if(T+(C/b)+(X/(b+F)) < T+(X/b)) {
            T += (C/b);
            b += F;
        }
        else {
            break;
        }
    }

    ss << fixed << T+X/b;
    
    
    return ss.str();
}

