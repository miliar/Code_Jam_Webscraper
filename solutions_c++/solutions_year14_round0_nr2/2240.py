//ShivamRana...
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <iterator>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <algorithm>
using namespace std;
int main()
{
    //freopen("2b.in","r",stdin);
    //freopen("2b.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
    {
        printf("Case #%d: ",cs);
        double c,f,x;
        cin>>c>>f>>x;
        double ccount=0.0,time=0.0,rate=2.0;
        while(1)
        {
            //if((x-ccount)<=c)
            if((x/rate)<=(c/rate + x/(rate+f)))
            {
                time=time + (x)/rate;
                break;
            }
            else
            {
                ccount+=c;
                time+=(c/rate);
                rate+=f;
            }
        }
        printf("%.7lf\n",time);
    }
    return 0;
}







