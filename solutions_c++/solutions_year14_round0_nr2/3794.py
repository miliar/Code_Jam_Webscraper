#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;


int main() 
{

        freopen ("input.txt","r",stdin);
        freopen ("output.txt","w",stdout);


        int cases=0,t;
        scanf("%d",&t);

        while(t--)
        {

            long double C,F,X;
            scanf("%Lf%Lf%Lf",&C,&F,&X);

            long double minn=X;

            long double rate=2.0L;
            long double sum=0.0L;
            while(1)
            {

                if(minn>(sum+X/rate))
                {
                    minn=sum+X/rate;
                    sum=sum+C/rate;
                    rate=rate+F;
                }
                else
                {
                    break;
                }
            }

            printf("Case #%d: %.7Lf\n",++cases,minn);
        }


		return 0;
}


