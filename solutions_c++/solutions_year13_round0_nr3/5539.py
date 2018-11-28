#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
bool is_palindrome(unsigned long orig);
int main()
{
     ifstream in("C-small-attempt0.in");
     ofstream out("output.txt");
     int size,begin,end,count=0;
     in>>size;
     for(int i=0;i<size;i++)
     {
           in>>begin>>end;
           for(int j=begin;j<=end;j++)
           {
                if(is_palindrome(j))
                {
                   float sqroot=sqrt(j);
                   if((sqroot-(int)(sqroot))==0)
                   {
                        if(is_palindrome(sqroot))
                        {
                             count++;                         
                        }
                   }                      
                }
           }
           cout<<"Case #"<<i+1<<": "<<count<<endl;
           out<<"Case #"<<i+1<<": "<<count<<endl;
           count=0;
     }
     return 0;    
}

bool is_palindrome(unsigned long orig)
{
  unsigned long reversed = 0, n = orig;

  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return orig == reversed;
}
