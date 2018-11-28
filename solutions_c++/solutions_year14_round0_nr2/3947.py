#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <algorithm>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <queue>
#include <sstream>
#include <cassert>
#include <cctype>
#include <climits>


#define FOR(i, n) for(int i=0; i<n; i++)

using namespace std;


/*

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

C  F  X

*/



int main()
{

    
    int total;
    cin >> total;

    FOR(i, total){
        
        double C, F, X;
        cin >> C >> F >> X;
        
        double curr = 2.0;
                
        double prev_inc;
        
        double first = X / 2.0;
        
        double prev = C / 2.0 + X / (curr + F);
        prev_inc = curr + F;
        
        
        if(prev > first){
        
            printf("Case #%d: %.7f\n", i+1, first);
            
                    
        }
        else
        {
                    
            double sum = 0;
                                
            while(true){
                                    
                sum = prev - X/prev_inc + C/prev_inc + X/(prev_inc + F);
                
                
                if(sum > prev){
                    
            printf("Case #%d: %.7f\n", i+1, prev);
            
            break;
                }
                
                prev = sum;
                prev_inc += F;
                
            }
            
                    
        }


    }


   
   return 0;
}
