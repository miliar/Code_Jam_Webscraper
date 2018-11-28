#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    double c,f,x,xemof,xemot,sol;
    int T;
    cin>>T;
    for(int h=1;h<=T;h++)
    {
        xemof=2.0;xemot=0.0;sol=0.0;
        cin>>c>>f>>x;
        while(sol<0.0000001){
            if((xemot+(x/xemof))<(xemot+(c/xemof)+(x/(xemof+f))))
            {
                sol=(xemot+(x/xemof));
            }
            else
            {
                xemot+=(c/xemof);
            }
            xemof+=f;
        }
        printf("Case #%d: %.7lf\n",h,sol);
    }
    return 0;
}
