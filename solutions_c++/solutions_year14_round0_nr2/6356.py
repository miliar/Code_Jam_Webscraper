#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
    int T, j, d;
    double C, F, X, ans1, ans2, p=2.0, interm;
    cin>>T; //number of cases
    for(int i=1;i<=T;i++)
    {
        j=0;
        scanf("%lf%lf%lf",&C,&F,&X);
        //The iteration begins
        while (true)
        {
            interm=0.0;
            if (j==0)
            {
                ans1=X/p;
                j++;
            }
            for (int d=j;d>=1;d--)  interm+=C/(p+(j-d)*F);
            ans2=interm+X/(p+j*F);
            if (ans1<=ans2)
            {
                break;
            }
            else
            {
                ans1=ans2;
                j++;
            }
        }
        printf("Case #%d: %.7lf\n",i, ans1);
    }
    return 0;
}
