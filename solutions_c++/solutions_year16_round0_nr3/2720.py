#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>

using namespace std;

int t, n, j;
int answers;
bool digits[32];


int get_divisor (long long num)
{
 int upper = floor(sqrt(num));
 for (int i=2; i<=upper; ++i)
 {
     if (num % i ==0)
        return i;
 } 
 return 1;
}

void check_num ()
{
     int divisors[11];
     bool is_coin = true;
     for (int base =2; base<11; ++base)
     {
         long long num = 0;
         long long cur_amount = 1;
         for (int i=n-1; i>=0; i--)
         {
                 if (digits[i])
                 {
                    num += cur_amount;              
                 }
                 cur_amount = cur_amount * base;
         }   
         //cout<<"Base: "<<base<<" Num: "<<num<<"\n"; 
         
         
         divisors[base] = get_divisor (num);
         if (divisors[base]==1)
         {
            return;                      
         }
     }
     
     for (int i=0;i<n;++i)
     {
      if (digits[i])
         cout<<1;
      else
          cout<<0;    
     }
     for (int i=2;i<11;++i)
         cout<<" "<<divisors[i];
     cout<<"\n";
     answers++;
}

void generate_nums (int index)
{
     if (answers==j)
        return;
     if (index == n-1)
     {
        check_num();
     }
     else
     {
         digits[index] = true;
         generate_nums(index+1);
         digits[index] = false;
         generate_nums(index+1);
     }
}

int main ()
{
  freopen("C-small-attempt0.in","r",stdin);   
  freopen("Cs.txt","w",stdout);
    
 cin>>t;
 cin>>n>>j;
 digits[0] = true;
 digits[n-1] = true;
 answers = 0;
 
 cout<<"Case #1:\n";
 generate_nums(1);
 //cin>>t;
 return 0;
}
