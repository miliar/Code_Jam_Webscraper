#include<iostream>
#include<cmath>
using namespace std;
int check_palindrome(long long int n)
{
    long long int temp = n;
    long long int rem,sum=0;
    double i = 0;
    while(n!=0)
    {
               rem = long(n)%10;
               sum = sum*10 +rem;
               i++;
               n = n/10;
    }
    if(sum == temp)return 1;
    else return 0;
}
               
int is_perfect_square(long long int n)
{
    double root1 = sqrt(float(n));
    long long int root2 = long(root1);
    if((root1-root2)==0)
    {
                        int check = check_palindrome(root1);
                        return check;
    }
    else return 0;
}
int main()
{
          long long int T;
          long long int I=1;
          long long int count=0;
          long long int lower;
          long long int upper;
          int flag1,flag2;
          cin>>T;
          while(T--)
          {
                    count=0;
                    flag1=flag2=0;
                    cin>>lower;
                    cin>>upper;
                    for(long long int i=lower;i<=upper;i++)
                    {
                           int flag1 = is_perfect_square(i);
                           if(flag1==1)
                           {
                                       flag2 = check_palindrome(i);
                                       if(flag2==1){count++;}
                           }
                    }
                    cout<<"Case #"<<I<<": "<<count<<endl;
                    I++;
          }
          return 0;
}
                    
                             
     
