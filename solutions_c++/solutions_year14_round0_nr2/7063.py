//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

using namespace std;

#define inf 1e8

int main()
{
    freopen("/Users/arkanathpathak/Downloads/B-large.in","r",stdin);
    freopen("/Users/arkanathpathak/Downloads/B-large-output","w",stdout);
    cout.precision(15);
    int test;
    cin >> test;
    for(int k=0;k<test;k++)
    {
        long double c, f, x;
        cin >> c >> f >> x;
        long double mina = x/2;
        long double val = c/2;
        for(int i=1;;i++)
        {
            
            long double ans = val + x/(2+i*f);
            if(ans>=mina) break;
            else mina = ans;
            val += c/(2+i*f);
        }
        cout << "Case #"<<k+1<<": "<<mina << endl;
    }

    
    return 0;
}