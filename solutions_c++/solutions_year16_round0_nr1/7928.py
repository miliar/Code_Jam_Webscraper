#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>
#include<string.h>
#include<math.h>
using namespace std;

void func(long long x,int a[])
{
    int rem;
    while(x)
    {
        rem=x%10;
        if(a[rem]!=rem)
        {
            a[rem]=rem;
        }
        x=x/10;
    }
}

int main()
{

    long long m,n,l;
    int t,y,a[32000],cnt=0,i,k=0;
    cin>>t;
    y=t;
    while(t--)
    {
        cnt=0;
        cin>>n;
        if(n==0)
          {   cout<<"Case #"<<++k<<": "<<"INSOMNIA"<<endl;
                 continue;

          }
        l=n;
        for(i=0;i<32000;i++)
            a[i]=20;
        i=0;
        while(cnt<=9)
        {
            n=l;
            m=n*(++i);

           // cout<<i<<"  "<<n<<"  "<<m<<"  ";
            func(m,a);
            cnt=0;
            for(int j=0;j<10;j++)
            {
                if(a[j]!=20)
                    cnt++;
            }
          //  cout<<cnt<<endl;
        }
      //  int k=1;

        cout<<"Case #"<<++k<<": "<<m<<endl;

    }
    return 0;
}
