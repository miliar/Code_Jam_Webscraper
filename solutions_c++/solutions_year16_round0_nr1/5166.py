#include<bits/stdc++.h>
#define nax 1000005
using namespace std;
 bool arr[10];

 bool done()
 {
     for(int i=0;i<10;i++)
     {
         if(arr[i]==false)
         return false;

     }
     return true;
 }
long long check(long long n)
{

    long long i=1;
    long long temp=n;
    for(int i=0;i<10;i++)
        arr[i]=false;
    while(true)
    {
        temp=n*i;
         while(temp!=0)
            {


             arr[(temp%10)]=true;
             temp/=10;
            }
             if(done())
                return (n*i);
                ++i;




    }

}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    long long t,n;
    cin>>t;
    long long num=1;
    while(t--)
    {
        cin>>n;
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",num);
        else
        {
            printf("Case #%lld: %lld\n",num,check(n));

        }
        num++;
    }
}
