
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("bb.txt","w",stdout);
    int T ;
    scanf("%d",&T);
    for( int ca = 1 ; ca <= T ; ++ca )
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double best_time = 2000000000;
        double time ;
        double rate ;
        for( int i = 0 ; i < 2000 ; ++i )
        {
            rate = 2.0 ;
            time = 0.0 ;
            for( int j = 0 ; j < i ; ++j )
            {
                time += (c/rate) ;
                rate += f ;
            }
            time += (x/rate);
            if( time < best_time && time > 0.0000001 )
                best_time = time ;
        }
        printf("Case #%d: %.7lf\n",ca,best_time);
    }

	//system("pause");
    return 0 ;
}

