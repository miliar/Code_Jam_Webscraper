#include <iostream>
#include <math.h>
using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;

bool is_square(int a)
{
    int s = sqrt((double)a);
    if(s*s == a)
           return true;
    return false;
}

bool is_palindrome(int a)
{
    int s = 0;
    int n = a;
    while(a>0)
    {
     s = s*10 + a%10;
     a = a/10;
    }
    if(s==n)
     return true;
     
    return false;
}

int main()
{
    ifstream indata;
    indata.open("C-small-attempt0.in");
    ofstream outdata;
    outdata.open("C-small-attempt0.txt");
	int t;
    indata>>t;
	for(int i=1; i<=t; i++)
	{
     int o = 0;
     int a, b;
     indata>>a>>b;
     for(int j=a; j<=b; j++)
     {
//                        outdata<<"j = "<<j<<"\n";
      if(is_square(j))
      {
//                       outdata<<j<<" is a square.\n";
       if(is_palindrome(j) && is_palindrome((int)sqrt((double)j)))
       { 
//       outdata<<j<<" is a palindrome.\n";
        o=o+1;
       }  
      }
     }
     outdata<<"Case #"<<i<<": "<<o<<"\n";
    }
    indata.close();
    outdata.close(); 
}
