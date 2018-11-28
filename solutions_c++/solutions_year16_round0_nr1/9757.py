#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    bool f=0;
    long long int n,temp,ans;
    cin>>t;
    int occur[10];
    for(int i=0;i<t;i++)
    {
        int j=10;
        while(j--)
        occur[j]=0;
        cin>>n;
        if(n==0)
        printf("Case #%d: INSOMNIA\n",i+1); //special case checked
        else
        {
        int j=0;
        while(++j)
        {
        f=0;
        ans=temp=j*n;
        while(temp>0) //loop to go through each digit! :D
                {
                    if(occur[temp%10]==0)
                    occur[temp%10]=1;
                    temp=temp/10;
                }
                for(int k=0;k<10;k++)
                    if(occur[k]==0)
                    {
                        f=1;
                        break;
                    }
                if(f==0)
                	break;
            }
            printf("Case #%d: %lld\n",i+1,ans);
        }
    }
    return 0;
}