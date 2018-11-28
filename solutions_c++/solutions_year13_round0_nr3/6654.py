#include<iostream>
using namespace std;

int palindrome(int n)
{
    int temp=n,rev=0;
    while(temp>0)
    {
       rev=rev*10+temp%10;       
       temp/=10;       
    }
    if(rev==n) return 1;
    return 0;
}
int main()
{
    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
              int a,b,ans=0;
              cin>>a>>b;
              for(int i=1;i<=100;i++)
              {
                  if(palindrome(i*i) && palindrome(i) && i*i>=a && i*i<=b)
                    ans++;    
              }
              printf("Case #%d: %d",p,ans);
              cout<<"\n";
    }
}
