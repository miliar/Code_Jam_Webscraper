#include<cstdio>
#include<ctype.h>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<iostream>
#include<sstream>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int main()
{
    //freopen("sample.txt","r",stdin);

    freopen("B.in","r",stdin);
    freopen("ans.txt","w",stdout);

    int kase=1;
    int test;
    cin>>test;
    while(test--)
    {
        double C, F, X;
        cin>>C>>F>>X;
        double rate=2.0;
        double sum = 0;
        bool loop = true;
        if ( X <= C)
        {
            sum = X/rate;
            loop = false;
        }
        while (loop)
        {
            sum += C/rate;
            double newTime, oldTime;
            newTime = X/(rate+F);
            oldTime = (X-C)/rate;
            if ( oldTime <= newTime)
            {
                sum += oldTime;
                break;
            }
            rate += F;
        }
        printf("Case #%d: %.7lf \n",kase++,sum);
    }

    return 0;
}
