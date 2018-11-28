//
//  main.cpp
//  test4
//
//  Created by Khaled on 4/9/16.
//  Copyright © 2016 Khaled. All rights reserved.
//

#include <iostream>
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
bool prime(unsigned long long  base10,unsigned long long  base2,unsigned long long  base3,unsigned long long  base4,unsigned long long  base5,unsigned long long  base6,unsigned long long  base7,unsigned long long  base8,unsigned long long  base9)
{
    for(unsigned long long  i=2; i<= sqrt(base10); i++) {
        if ((base10%i) == 0||(base2%i) == 0||(base3%i) == 0||(base4%i) == 0||(base5%i) == 0||(base6%i) == 0||(base7%i) == 0||(base8%i) == 0||(base9%i) == 0) return false;
    }
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
void getDevisor(unsigned long long  &base10,unsigned long long  &base2,unsigned long long  &base3,unsigned long long  &base4,unsigned long long  &base5,unsigned long long  &base6,unsigned long long  &base7,unsigned long long  &base8,unsigned long long  &base9)
{
    bool b2= false,b3= false,b4= false,b5= false,b6= false,b7= false,b8= false,b9= false,b10= false;
    for(unsigned long long  i=2; i<sqrt(base10); i++) {
        if ((base10%i) == 0&&!b10)
        {
            base10 = base10/i;
            b10 = true;
        }
        
        if((base2%i) == 0&& !b2)
        {
            base2= base2/i;
             b2 = true;
        }
        if((base3%i) == 0&& !b3)
        {
            base3= base3/i;
            b3 = true;
        }
        if((base4%i) == 0&& !b4)
        {
            base4= base4/i;
            b4 = true;
        }
        if((base5%i) == 0&& !b5)
        {
            base5= base5/i;
            b5 = true;
        }
        if((base6%i) == 0&& !b6)
        {
            base6= base6/i;
            b6 = true;
        }
        if((base7%i) == 0&& !b7)
        {
            base7= base7/i;
            b7 = true;
        }
        if((base8%i) == 0&& !b8)
        {
            base8= base8/i;
            b8 = true;
        }
        if((base9%i) == 0&& !b9)
        {
            base9= base9/i;
            b9 = true;
        }
        
    }

}
unsigned long long GCD(unsigned long long u, unsigned long long v) {
    while ( v != 0) {
        unsigned long long r = u % v;
        u = v;
        v = r;
    }
    return u;
}
unsigned long long convert(int base,string s)
{
    unsigned long long value = 0 ;
    int counter = 0;
    for (int i = s.length() - 1; i>= 0; i--) {
        if (s[i] == '1')
        {
            value += pow(base, counter);
        }
        counter++;
    }
    return value;
}
vector<unsigned long long> primes;

int main(int argc, const char * argv[]) {

    int all ;
    cin>>all;
    int c = 1;
    while( c<= all)
    {
        cin>>n>>j;
        string maxOne = "",maxZero = "1";
        
        for (int i=0;i<n;i++)
        {
            maxOne += "1";
        }
        for(int i = 1 ; i < n-1 ; i++)
        {
            maxZero += "0";
        }
        maxZero += "1";
        unsigned long long min = std::bitset<64>(maxZero).to_ullong();
        unsigned long long max = std::bitset<64>(maxOne).to_ullong();
        
        std::bitset<16> b(min);
        int counter = 0;
        string s = b.to_string();
        for (int count = 0;count<s.length();count++)
        {
            if (s[count] == '0')
            {
                counter++;
            }
            else{
                break;
            }
        }
        cout<<"Case #"<<c<<":"<<endl;
        for (unsigned long long  count = min ;count<= max; count ++)
        {
    //        const int x = n;
            std::bitset<16> b(count);
            string current = b.to_string();
            current = current.substr(counter,current.length());
            if( current[current.length() -1] == '0')
                continue;
//            int i_bin =
            unsigned long long base2 = stoull(current,NULL,2);
//            if (prime(base2))
//                continue;
//            base2=  getDevisor(base2);
            unsigned long long base3 = stoull(current,NULL,3);
//            if (prime(base3))
//                continue;
//            base3=  getDevisor(base3);
            unsigned long long base4 = stoull(current,NULL,4);
//            if (prime(base4))
//                continue;
//            base4=  getDevisor(base4);
            unsigned long long base5 = stoull(current,NULL,5);
//            if (prime(base5))
//                continue;
//            base5=  getDevisor(base5);
            unsigned long long base6 = stoull(current,NULL,6);
//            if (prime(base6))
//                continue;
//            base6=  getDevisor(base6);
            unsigned long long base7 = stoull(current,NULL,7);
//            if (prime(base7))
//                continue;
//            base7=  getDevisor(base7);
            unsigned long long base8 = stoull(current,NULL,8);
//            if (prime(base8))
//                continue;
//            base8=  getDevisor(base8);
            unsigned long long base9 = stoull(current,NULL,9);
            
//            base9=  getDevisor(base9);
            unsigned long long base10 = stoull(current,NULL,10);
            unsigned long long base110 = base10,base12 = base2,base13 = base3,base14 = base4,base15 = base5,base16 = base6,base17 = base7,base18 = base8,base19 = base9;

            getDevisor(base10,base2,base3,base4,base5,base6,base7,base8,base9);
            if (base10 == base110 ||  base10 == 1 || base9 == base19 ||  base9 == 1||base8 == base18 ||  base8 == 1||base7 == base17 ||  base7 == 1||base6 == base16 ||  base6 == 1||base5 == base15 ||  base5 == 1||base4 == base14 ||  base4 == 1||base3 == base13 ||  base3 == 1||base2 == base12 ||  base2 == 1)
                continue;

            
//            base3=  getDevisor(base3);
//            base4=  getDevisor(base4);
//            base5=  getDevisor(base5);
//            base6=  getDevisor(base6);
//            base7=  getDevisor(base7);
//            base8=  getDevisor(base8);
//            base9=  getDevisor(base9);
//            base10=  getDevisor(base10);
//            if (count_factors(base10)==2)
//                continue;
//            base10=  getDevisor(base10);
//            if (base2 == 1 || base3 == 1 ||base4 == 1 ||base5 == 1 ||base6 == 1 ||base7 == 1 ||base8 == 1 ||base9 == 1 ||base10 == 1 )
//                continue;
            cout<<current<<" "<<base2<<" "<<base3<<" "<<base4<<" "<<base5<<" "<<base6<<" "<<base7<<" "<<base8<<" "<<base9<<" "<<base10<<endl;
            j--;
            if (j==0)
                break;
        }
        c++;
    }
    return 0;
}
