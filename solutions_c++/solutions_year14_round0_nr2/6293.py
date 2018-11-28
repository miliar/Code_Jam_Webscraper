/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  4/12/2014 12:43:39 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Terry Cheong. (terry182)
 *   Organization:  
 *
 * =====================================================================================
 */

#include <cstdio>
#include <iostream>
using namespace std;
int main()
{ FILE *output;
    int T;
    scanf("%d",&T);
    output = fopen("output.out","w");
     for (int count = 1; count <= T; count++)
     {
         double c,f,x;
            scanf("%lf %lf %lf",&c,&f,&x);
         double prev = -1.0, factory = 0.0;
         double r = 2.0; 
            while ( true )
            {  
                double total = 0.0;
                total = factory + x/r;
                if (prev == -1)
                    prev = total;
                else if (total > prev)
                {  
                    break;
                }

                factory += c/r;
                r += f;
                prev = total;
            }
        fprintf(output,"Case #%d: %.7f\n",count,prev);
     }   
    return 0;
}
