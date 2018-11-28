
/*
 
 Hossam Ghareeb (hossam.ghareb@gmail.com)
 
 */

#include <cstring>
#include <string.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <complex>
#include <list>
#include <map>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <deque>
#include <queue>

using namespace std;


#define all(v) v.begin(),v.end()
#define forloop(i,m) for(int i=0;i<(int)(m);i++)
#define forloop2(i,n,m) for(int i=n;i<(int)(m);i++)
#define printCase(i) printf("Case #%d: ", i)
#define printEndLine cout << endl


typedef vector<string> vs;
typedef  stringstream ss;
typedef vector<int> vi;
typedef istringstream iss;


#define SMALL

#define SMALL_FILE_IN "B-small-attempt0.in"
#define SMALL_FILE_OUT "B-small-attempt0.out"
#define LARGE_FILE_IN "A-large-practice.in"
#define LARGE_FILE_OUT "A-large-practice.out"


double minTime(double c, double f, double x)
{
    double rate = 2.0;
    double minTime = INT32_MAX;
    
    forloop(i, INT32_MAX)
    {
        double t = 0;
        double r = 2.0;
        forloop(j, i)
        {
            t += c / r;
            r  += f;
            
        }
        
            if (minTime < t) {
                break;
              }
        
        double clickTime = x / r;
        t += clickTime;
        
        if (t < minTime) {
            minTime = t;
        }
        

    }
    
    return minTime;
}

int main(int argc, const char * argv[])
{
    
    
#ifdef SMALL
	freopen(SMALL_FILE_IN, "rt", stdin);
	freopen(SMALL_FILE_OUT, "wt", stdout);
#endif
#ifdef LARGE
	freopen(LARGE_FILE_IN, "rt", stdin);
	freopen(LARGE_FILE_OUT, "wt", stdout);
#endif
    
    
    int N;
    
    cin >> N;
    
    cout << setprecision(7) << fixed;
    
    forloop2(i, 1, N + 1)
    {
        double C, F, X;
        cin >> C >> F >> X;
        
        double min = minTime(C, F, X);
        printCase(i);
        cout << min << endl;
        
    }
    
    
    
    return 0;
}

