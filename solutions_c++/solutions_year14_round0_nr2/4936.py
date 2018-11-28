#include <iostream>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits.h>
#include <set>
#include <stack>
#include <vector>
#include <map>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-Large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        double c,f,x;
        double increase=2;
        scanf("%lf %lf %lf",&c,&f,&x);
        double tot=0,score=0;

        while(fabs(score-x)>10e-7)
        {
            if(score+c>=x)
            {
                tot+=(x-score)/increase;
                score=x;
            }
            else
            {
                tot+=c/increase;
                score+=c;
                if((x-score)/increase<(x)/(increase+f))
                {
                    tot+=(x-score)/increase;
                    score=x;
                }
                else
                {
                    increase=increase+f;
                    score=0;
                }
            }
        }
        printf("Case #%d: ",z++);
        printf("%lf",tot);
        printf("\n");
    }
    return 0;
}
