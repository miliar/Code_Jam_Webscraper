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
    int testCaseNumber, lowerBound, upperBound, fandsqCount;
    //string lowerBound, upperBound;
    
    cin >> testCaseNumber;

    for(int i = 0 ; i < testCaseNumber; i++) {
    
        fandsqCount = 0;
    
        cin >> lowerBound >> upperBound;
        //cin.get();

        
        for(int j=1 ; j*j <= upperBound ; j++) {

            stringstream ss;
            //ss.str("");
            ss << j;
            string sqrt = ss.str();
        
            if(j*j >= lowerBound) {
            
                stringstream ss2;
                ss2 << j*j;
                string sq = ss2.str();
            
                if ((sqrt == string(sqrt.rbegin(), sqrt.rend())) && (sq == string(sq.rbegin(), sq.rend()))) {
                    fandsqCount++;
                }
            
            
            }
 
        }
        
        cout << "Case #" << i+1 << ": " << fandsqCount << endl;
        

        
    }


}


