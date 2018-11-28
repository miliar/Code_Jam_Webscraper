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
    freopen("Large-Input.txt", "w", stdout);
    double c,f,x,cps,cokies,time;
    int T;
    cin>>T;
    for(int Tcase=1;Tcase<=T;Tcase++)
    {
        cps=2.0;cokies=0.0;time=0.0;
        cin>>c>>f>>x;
        while(time<0.0000001){
            if((cokies+(x/cps))<(cokies+(c/cps)+(x/(cps+f))))
            {
                time=(cokies+(x/cps));
            }
            else
            {
                cokies+=(c/cps);
            }
            cps+=f;
        }
        printf("Case #%d: %.7lf\n",Tcase,time);
    }
    return 0;
}
