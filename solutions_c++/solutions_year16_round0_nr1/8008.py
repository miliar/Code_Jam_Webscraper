#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
  long long  int a,t,b;
   //freopen("me.in","r",stdin);
   //  freopen("out.txt","w",stdout);
   int arr[10]={0};
    cin>>t;
  long long  int count=1,mcount=0,temp;
   long long int cc=0;
    while(t--)
    {
        for(int i=0;i<10;i++)
            arr[i]=0;
        cc++;
        mcount=0;
        count=1;
        cin>>a;
        if(a==0)
            cout<<"Case #"<<cc<<":"<<" INSOMNIA"<<endl;
        else
        {
        while(1)
        {
        b=a;
        b=b*count;
        while(b!=0)
        {
            temp=b%10;
            if(arr[temp]!=1)
            {
                arr[temp]=1;
                mcount++;
        //        cout<<"dv"<<endl;
            }
            b/=10;
        }
        if(mcount==10)
        {
             cout<<"Case #"<<cc<<": "<<a*count<<endl;
             break;
        }
        else
            count++;
         //     cout<<cc<<" "<<<<endl;
        }
        }
    }
    return 0;
}
