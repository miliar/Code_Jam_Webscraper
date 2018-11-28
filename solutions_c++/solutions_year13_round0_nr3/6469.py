#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

bool palindrome(int num)
{
     int reverse=0, rem,temp;
  temp=num;
  while(temp!=0)
  {
     rem=temp%10;
     reverse=reverse*10+rem;
     temp/=10;
  }  

  if(reverse==num)  
      return true;
  else
     return false;
  
}



bool chek_sqr(int number)
{
double d_sqrt = sqrt(number);
int i_sqrt = d_sqrt;
if ( d_sqrt == i_sqrt )
     {
         if(palindrome(i_sqrt))
         {
             return true;                      
         }    
     }
     return false;
}


int main()
{
    ifstream in;
    in.open("C-small-attempt0.in");
    ofstream out;
    out.open("output.txt");
    int test;
    in>>test;
    test++;
    int iteration=1;
    int lower=0,upper=0;
    int number=0,count=0,square=0;
    
    while(iteration!=test)
    {
         in>>lower;
         in>>upper;
        // cout<<lower<<" "<<upper<<endl;
        // number=lower;
         count=0;
         square=0;
      for(int i=lower;i<=upper;i++)
      {
              if(palindrome(i)==true)
              {
                      if(chek_sqr(i))
                      count++;              
              }
              
      }
                          
    out<<"Case #"<<iteration<<": "<<count<<endl;    
    iteration++;                  
    }



system("pause");    
return 0;    
}
