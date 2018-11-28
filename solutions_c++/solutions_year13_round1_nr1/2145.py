#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
    int testCaseNumber;
   
    long long int radius, paint, ringNumber;

    cin >> testCaseNumber;
     
    for(int i = 0 ; i < testCaseNumber; i++) {
    
        ringNumber = radius = paint = 0;
        
        cin >> radius >> paint;

        
        int j=1;
        
        while(paint>=0) {
    
            paint -= (j*1+radius)*(j*1+radius)-(((j-1)+radius)*((j-1)+radius));
            j+=2;
            if(paint>=0)
                ringNumber++;
            else
                break;
            
        }
        
        cout << "Case #" << i+1 << ": " << ringNumber << endl;
    
    
    }
    
    
    
    
}

