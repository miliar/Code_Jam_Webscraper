#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <vector>
#include <map>
#include <bitset>
#include <set>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>

#define INF -1

using namespace std;
/* Define Data-types */


int main()
{
    /* Input routine */
    int t; // number of test cases
    scanf("%d", &t);
    for(int test_case = 0; test_case < t; test_case++)
    {
        double c,f,x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double cps = 2.0; // cookies per second
        double c_time = 0; // current time
        double best_time = INF;
        //bool found = false;
        while(true)
        {
            double new_time = c_time + x/cps;
            if(best_time != INF && new_time>best_time)
                break;
            best_time = new_time;
            c_time += c/cps;
            cps+=f;
        }
        printf("Case #%d: %.7f\n", test_case+1, best_time);
    }

    return 0;
}

