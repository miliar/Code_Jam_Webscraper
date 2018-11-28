#include<iostream>
#include<math.h>
using namespace std;
int reverse(int a)
{
    int n=a,rev=0;
    while(n)
    {
        rev=(rev*10)+(n%10);
        n/=10;
    }
    return rev;
}
int palindrome(int a,int b)
{
    int res=0;
    while(a<=b)
    {
            if(a==reverse(a))
                if(sqrt(a)==reverse(sqrt(a)))
                    res++;
            a++;
    }
    return res;
}
int main()
{
    int t,a,b,sum=0;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>a>>b;
        sum=palindrome(a,b);
        cout<<"\n"<<"Case #"<<i<<":"<<" "<<sum;
    }
}
