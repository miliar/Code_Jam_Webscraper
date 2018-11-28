//
//  main.cpp
//  codejam : swinging wild
//
//  Created by Marc Saunders on 2015-12-19.
//  Copyright © 2015 Marc Saunders. All rights reserved.
//

#include <iostream>
#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <stdint.h>
#include <unistd.h>
#include <math.h>

#include <stdio.h>      /* printf */
#include <assert.h>


#define ha //

// 64bitoperations need 32 bit max numbers


using namespace std;

string testcases ;

string levels ;
string results;
int times[10000] ;
long double probs [10000] ;
long double scales [ 10000] ;
int indexs[10000];
int indexe[2000];


long double average ;
long double remaining ;


int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream infile("/Users/marcsMac/Desktop/codejam/in.txt");
    freopen("/Users/marcsMac/Desktop/codejam/out.txt","w",stdout);
    std::getline(infile, testcases) ; // read in string number of test cases
    std::istringstream iss(testcases);
    int N ;
    iss >> N ;
    fprintf(stderr,"\n");
    fprintf(stderr,"there are %d tests in this guy\n",N);
    
    
    for(int n=0;n<N ;n++)
    {
        
        std::getline(infile, testcases) ; // read in the pattern
        std::istringstream issy(testcases);
        
        issy >> levels ;
        
        long unsigned  len = levels.length() ;
        
        results = levels.substr(0,1);
        
        for (int x = 1  ;  x < len ; x ++)
        {
         
            if ( results.substr(0,1) > levels.substr(x,1) )
            {
                results = results + levels.substr(x,1) ;
            }
            else
            {
                results = levels.substr(x,1)  + results ;

            }
            
        }
        
        printf("Case #%d: %s\n",n+1 , results.c_str());
        
        
    }
    return 0 ;
}