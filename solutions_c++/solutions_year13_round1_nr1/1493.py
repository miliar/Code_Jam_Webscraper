#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    int T=0;
    cin >> T;
    map<int, long long> m;
    for(int i=1;i<1001;i++) {
       m[i] = i*i; 
    }
    for(int test=1;test<=T;test++) {
        int result = 1;
        int r, t;
        cin >> r >> t;
        t -= (r+1)*(r+1) - r*r;
        for(int i=r+2;1;i+=2) {
            t -= (i+1)*(1+i)-i*i;
            if(t>=0) {
                result++;
            }else {
                break;
            }
        }
        cout << "Case #" << test << ": " << result <<  endl;
    }
    return 0;
}
/* vim: set ts=4 sw=4 sts=4 tw=100 et: */
