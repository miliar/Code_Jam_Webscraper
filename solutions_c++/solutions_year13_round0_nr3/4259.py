//
//  main.cpp
//  QualifyingC
//
//  Created by Sambhav on 4/13/13.
//  Copyright (c) 2013 Sword Software. All rights reserved.
//

#include <iostream>
#include<fstream>
#include "math.h"

using namespace std;

bool checkPalindrome (unsigned long int n) {
    unsigned long int rev=0;
    unsigned long int num;
    num = n;
    do
    {
        rev = (rev*10) + num%10;
        num = num/10;
    }while (num!=0);

    if (n == rev)
        return true;
    else
        return false;
}

unsigned long int reverseOf (unsigned long int n) {
    unsigned long int rev=0;
    unsigned long int num;
    num = n;
    do
    {
        rev = (rev*10) + num%10;
        num = num/10;
    }while (num!=0);
    return rev;
}

int getDigits (unsigned long int n) {
    int count = 0;
    while (n!=0) {
        count++;
        n = n/10;
    }
    return count;
}

int main(int argc, const char * argv[])
{
    
    ofstream op("/Users/sambhav/Dropbox/codejam/2013/QualifyingC/C-large-1.op");
	ifstream ip("/Users/sambhav/Dropbox/codejam/2013/QualifyingC/C-large-1.in");
    
    int T,count,i,digits,digitsToDiscard;
    unsigned long int A,B,a,b,ar,ac,ab,af,ao;
    
    ip>>T;
    
    for(i=0;i<T;i++)
    {
        count = 0;
        
        ip>>A>>B;
        a = ceil(sqrt(A));
        b = floor(sqrt(B));
        ao=a;
        
        digits = getDigits(a);
        
        if (digits%2)
            digitsToDiscard = (digits-1)/2;
        else
            digitsToDiscard = digits/2;
        ar=0;
        ab = a;
        for (int j=0;j<digitsToDiscard;j++) {
            ab = ab/10;
        }
        ac=ab;
        if (digits%2) ac = ac/10;
        af=reverseOf(ac);
        a=(ab*pow(10, getDigits(ac)))+af;
        
        for (;a<=b ;) {
            
            if (checkPalindrome(a*a) && a>=ao) count++;
            ab++;
            a=(ab*pow(10, getDigits(ac)))+af;
            digits = getDigits(a);
            
            if (digits%2)
                digitsToDiscard = (digits-1)/2;
            else
                digitsToDiscard = digits/2;
            ar=0;
            ab = a;
            for (int j=0;j<digitsToDiscard;j++) {
                ab = ab/10;
            }
            ac=ab;
            if (digits%2) ac = ac/10;
            af=reverseOf(ac);
            a=(ab*pow(10, getDigits(ac)))+af;
        }
        
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
        op<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    op.close();
    ip.close();
    return 0;
}