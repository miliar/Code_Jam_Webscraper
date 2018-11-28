#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        double c, f, x;
        cin >> c >> f >> x;

        double n = 2.0;
        double ret = x / n;
        double cost = 0.0;
        for(;;){
            cost += c / n;
            n += f;
            double tmp = cost + x / n;
            if(tmp < ret)
                ret = tmp;
            else
                break;
        }

        printf("Case #%d: %.10f\n", tc, ret);
    }

    return 0;
}