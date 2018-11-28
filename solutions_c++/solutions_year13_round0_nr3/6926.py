#include <iostream>
#include <conio.h>
#include <math.h>
#include <fstream>

using namespace std;

bool findPalindrome(long long);

int main()
{ 
 int count=0;
 long long ll,ul,tc;
 long long rll,rul;
 
 ifstream read("C-small-attempt4.in");
 read>>tc;
 for(long long i=1;i<=tc;i++)
 {
    read>>ll>>ul;
    rll =(long long) sqrt(ll);
    rul =(long long) sqrt(ul);
 
    if( (rll*rll) < ll )
    rll = rll + 1;
 
    for(long long j=rll;j<=rul;j++)
    {
       if(findPalindrome(j))
         if(findPalindrome(j*j))
           count++ ; 
    }
    cout<<"Case #"<<i<<": "<<count<<endl;
    count =0;             
 }
 
 getch();
 return 0;
}

bool findPalindrome(long long a)
{
 long long num=0;
 long long b;
 b=a;
 while(b>0)
 {
   num = 10*num + b%10;          
   b = b/10;
 }
 
 if(num == a)
 return true;
 else
 return false;
}
