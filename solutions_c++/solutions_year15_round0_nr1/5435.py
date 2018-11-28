#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

char str[10000];
int main()
{
  long long int t,ans,sum,n,i,ind;
  freopen ("input.txt","r",stdin);
  freopen ("output.txt","w",stdout);
    cin>>t;
    ind=t;
    while(t)
    {
        cin>>n;
        cin>>str;

        ans=0;
        sum=0;

        for(i=0;i<=n;i++)
        {
            if(sum<i)
                {ans=ans+i-sum;
                 sum=sum+i-sum;}
            sum=sum+str[i]-'0';

        }
        //Case #1: 0
        cout<<"Case #"<<ind-t+1<<": "<<ans<<endl;
        t--;
    }
    return 0;

}
