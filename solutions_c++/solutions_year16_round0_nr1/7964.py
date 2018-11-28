#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    long long int t,i,j,n,temp,ans,num=0;
    bool arr[10];
    freopen("alar.in","r",stdin);
   freopen("oplar1.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        num++;
        cin>>n;
        if(n==0)
         {

          cout<<"Case #"<<num<<": "<<"INSOMNIA\n";
            continue;
         }

        for(i=0;i<10;i++)
            arr[i]=0;
        bool flag=0;
        j=1;
        while(flag==0)
        {
            temp=n*j;
            ans=temp;
            while(temp)
            {
                arr[temp%10]=1;
                temp/=10;
            }
            flag=1;
            for(i=0;i<10;i++)
            {
               if( arr[i]==0)
                flag=0;
            }
                j++;
        }
        cout<<"Case #"<<num<<": "<<ans<<endl;
    }
return 0;
}
