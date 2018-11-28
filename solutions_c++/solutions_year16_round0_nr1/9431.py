#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,i,k,l,n,j,cnt=0;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
         cnt=0;
        int a[10]={0};
        cin>>n;
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",i);
        else
        {
           j=1;
         long long p=n;
        while(true)
        { j++;
           k=p;
           while(k>0)
           {
               l=k%10;
               if(a[l]==0)
                   cnt++;
               a[l]++;
               k=k/10;
           }

           if(cnt>=10)
            break;
           p=n*j;

        }
         printf("Case #%lld: %lld\n",i,p);
        }


    }

    return 0;
}
