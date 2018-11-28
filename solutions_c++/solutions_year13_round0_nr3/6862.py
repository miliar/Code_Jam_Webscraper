#include<iostream>
#include<math.h>
using namespace std;
int palindrome(long long int a)
{
    long long int temp,sq;
    temp=0;
    sq=a;
    while(sq)
    {
        temp=temp*10+sq%10;
        sq/=10;
    }
    if(temp==a)
    {
        return(1);
    }
    return(0);
}
int main()
{
    int t,count,temp;
    long long int  a,b;
    long long int asq,bsq;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        count=0;
        cin>>a>>b;
     //   cout<<a<<" "<<b<<endl;
        asq=sqrt(a);
        bsq=sqrt(b);
      //  cout<<asq<<" "<<bsq<<endl;
        for(int i=asq;i<=bsq;i++)
        {
            if(palindrome(i))
            {
                if(i*i>=a&&i*i<=b&&palindrome(i*i))
                {
        //            cout<<i*i<<endl;
                    count++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return(0);
}
