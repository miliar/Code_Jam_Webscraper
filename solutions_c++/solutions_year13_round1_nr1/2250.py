#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <fstream>
#include <math.h>
#include <cmath>
#include <vector>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <iomanip>
#include <deque>
#include <list>
#include <cctype>
#include <utility>

#define min(a,b) (a<b)?a:b
#define max(a,b) (a>b)?a:b

using namespace std;


const double PI = 2 * acos (0);

int main()
{
    //Problem A. Bullseye
/*
5
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000
*/

    int T;
    cin>>T;
    for(int i=1; i<=T; i++)
    {
        double r, t, j=0;
        cin>>r>>t;
        double c=0;
        while(1)
        {
            t-=(2*r+1);
            if(t>=0)j++;
            else break;
            r+=2;
        }
        cout.setf(ios::fixed);
        cout.precision(0);
        cout<<"Case #"<<i<<": "<<j<<endl;
    }


    return 0;
}

