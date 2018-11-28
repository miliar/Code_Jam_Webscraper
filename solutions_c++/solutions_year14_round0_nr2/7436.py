#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outlarge01.txt", "w", stdout);
    int T,t,f;
    double C,F,X,y,r,ans;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        r=(double)2;
        y=X/r;
        ans=0;
        //cout<<y<<endl;
        while(1)
        {
            if(y>(C/r + X/(r+F)))
            {
                ans+=C/r;
                r=r+F;
                y=X/r;
                //cout<<"here1\n";
            }
            else
            {
                ans+=X/r;
                //cout<<X/r<<endl;
                //cout<<"here\n";
                break;
            }
        }
            printf("Case #%d: %.7lf\n",t,ans);

    }
    return 0;

}
