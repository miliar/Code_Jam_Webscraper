#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include<sstream>
#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t,tt;
    double c,f,x,time1,f_old,last,answer1,answer2,answer;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        f_old=2;
        last=0;
        while(1)
        {
            answer1=last+x/f_old;
            answer2=last+(c/f_old)+(x/(f_old+f));
            if((answer1<answer2) )
            {
                answer=answer1;
                break;
            }
            last+=(c/f_old);
            f_old+= f;
        }
        printf("Case #%d: %.7lf\n",tt,answer);
    }

	return 0;
}
