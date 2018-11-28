

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

inline int min(int a,int b) {
    return a<b?a:b;
}

int intLength(long long int input) {
    int r=0;
    while (input) {
        input /= 10;
        r++;
    }
    return r;
}

bool checkPalindrome(long long int num) {
    if (num!=0) {
    long long int rem,sum,numCopy;
    sum=0;
    numCopy=num;
    while(num!=0)    //Loop to reverse the number.
    {
        rem=num%10;
        num=num/10;
        sum=sum*10+rem;
        
    }
    if(sum==numCopy) return true;
    }
    return false;
}

int main(int argc, const char * argv[])
{

    ifstream input;
    ofstream output;
    int nCases;
    long long int A,B,lowA,lowB;
    long int goodPalindromes = 0;
    string palindrome;
    
    input.open(argv[1]);
    output.open(argv[2]);
    input >> nCases;
    
    for(int i=0;i<nCases;i++) {
        output << "Case #" << i+1 << ": ";
        input >> A >> B;
        lowA=sqrtl(A);
        lowB=sqrtl(B);
        if(lowA<sqrtl(A)) lowA+=1;
    
        for (long long int j=lowA; j<=lowB; j++) {
            if (checkPalindrome(j)) {
                if (checkPalindrome(j*j)) {
                    goodPalindromes++;
                }
            }
        }
        
        
        output << goodPalindromes << endl;
        goodPalindromes=0;
    }
    return 0;
}