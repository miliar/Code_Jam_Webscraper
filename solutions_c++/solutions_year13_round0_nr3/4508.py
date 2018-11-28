#include <iostream>
#include <math.h>
using namespace std;
bool isPal (int x)
{
 int digits[101];     
 int num_digits = 0;
 while (x>0)
 {
           digits[num_digits] = x%10;
           x = x/10;
           num_digits++;
 }
 for (int i=0;i<num_digits;++i)
 {
     if (digits[i]!=digits[num_digits-i-1])
        return false;    
 }
 return true;
}

int main ()
{
    
    freopen ("C-small.in","r",stdin);
    freopen ("C-small.txt","w",stdout);
    
    int t, a,b,counter;
    
    cin>>t;
    
    for (int trial=1;trial<=t;++trial)
    {
             counter= 0;
        
            cin>>a>>b;
            int a_root = (int)(sqrt(a));
            int b_root = (int)(sqrt(b));
            if (a_root*a_root<a)
               a_root++;             
            
            
            for (int i=a_root;i<=b_root;++i)
            {
                if (isPal(i))
                {
                   if (isPal(i*i))
                   {
                            counter++;      
                   }             
                }    
            }
            
            cout<<"Case #"<<trial<<": "<<counter<<"\n";
    }
    
 
    return 0;   
}
