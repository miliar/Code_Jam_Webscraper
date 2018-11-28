//
//  main.cpp
//  round 1
//
//  Created by Khaled on 4/16/16.
//  Copyright © 2016 Khaled. All rights reserved.
//

#include <iostream>
#include <stdlib.h>     /* atoi */
#include <string>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* strtoll */
#include <bitset>
#include <vector>
using namespace std;

template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}

int n,j;
inline bool IsPrime( unsigned long long number )
{
    if ( ( (!(number & 1)) && number != 2 ) || (number < 2) || (number % 3 == 0 && number != 3) )
        return (false);
    
    for( int k = 1; 36*k*k-12*k < number;++k)
        if ( (number % (6*k+1) == 0) || (number % (6*k-1) == 0) )
            return (false);
    return true;
}
unsigned long long count_factors(unsigned long long n)
{
    unsigned long long i,f=1;
    if(n==1)
        return 1;
    else
    {
        for(i=2;i<=(n/2);i++)
        {
            if(n%i == 0)
                f++;
        }
        return (f+1);
    }
    
}

unsigned GCD(unsigned u, unsigned v) {
    while ( v != 0) {
        unsigned r = u % v;
        u = v;
        v = r;
    }
    return u;
}
unsigned LCD(unsigned u, unsigned v) {
    return u*v /GCD(u,v);
}

float stringToFloatingNumber(string s)
{
    return stof(s.c_str());

}

long long int stringToNumber(string s)
{
    return atoi( s.c_str());
//    int i = std::stoi(si);
//    float f = std::stof(sf);
}
int main(int argc, const char * argv[]) {
    // insert code here...
//    write to file
//    freopen("/Users/khaled/Documents/round 1/round 1/file.out", "w", stdout);
//    freopen("/Users/khaled/Documents/round 1/round 1/file.in", "r", stdin);
    
    
    int n;
    
    cin>> n;
    int counter = 1;
    while (n>=counter)
    {
        string s = "",res = "";
        cin>>s;
        res = s[0];
        for (int i = 1 ;i< s.length();i++)
        {
            if (s[i]<=res[res.length()-1])
            {
                res += s[i];
            }
            else if (s[i]>=res[0]){
                res = s[i] + res;
            }
            else{
                res += s[i];
            }
        }
        cout<<"Case #"<<counter<<": "<<res<<endl;
        counter++;
        
    }
    

    
    
    return 0;
}
