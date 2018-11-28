#include<bits/stdc++.h>
using namespace std;
long long solve(long long n)
{
    long long temp2;
    if(n==0)
    {
        return -1;
    }
    else
    {
        long long arr[10];
        memset(arr,0,10*sizeof(long long));
        long long temp=n,i=2;
        while(true)
        {
            //cout<<temp<<endl;
            temp2=temp;
            while(temp>0)
            {
                arr[temp%10]++;
                temp/=10;
            }
            
            
            bool flag=true;
            for(long long j=0;j<10;j++)
            {
                //cout<<arr[j]<<" "<<endl;
                if(arr[j]==0)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)
                break;
          
           temp=n*i;
           i++;
           
        }
    }
    return temp2;
}
int main()
{
    long long t,n;
    cin>>t;
    for(long long i=1;i<=t;i++)
    {
        cin>>n;
        cout<<"Case #"<<i<<": ";
        long long x=solve(n);
        if(x==-1)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            cout<<x<<endl;
        }
        
    }
    return 0;
    
}
