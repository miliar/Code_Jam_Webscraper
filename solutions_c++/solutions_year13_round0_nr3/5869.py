#include <cstdlib>
#include <iostream>
#include<fstream>
using namespace std;
bool palindrome(int n)
{
   int reverse = 0, temp;
  
   temp = n;
 
   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }

   if ( n == reverse )
   return true;
   else
   return false;
}

int main(int argc, char *argv[])
{
    ifstream in("C-small-attempt1.in");
  ofstream out("out.out");
    int arr[31];
    int k=0; 
    
    for(int i=1;i<32;i++)
    {
            arr[i]=i*i;
    }
   
int a,b,t;
in>>t;
if(t>=1&&t<=100)
for(int g=0;g<t;g++){
in>>a>>b;
k=0;
for(int i=a;i<=b;i++)
{
        
        for(int j=1;j<32;j++)
        {
                if(i==arr[j])
                {
                       if(palindrome(j)==true && palindrome(arr[j])==true)
                       k++;
                }
        }
}      
                
out<<"Case #"<<(g+1)<<": "<<k<<endl;
}
    system("PAUSE");
    return EXIT_SUCCESS;
}
