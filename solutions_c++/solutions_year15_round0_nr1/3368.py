//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

int ar[1000009];
string aa;

int  main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);

    int i,j,k,N,T,S,ans,temp,cas=0;
    cin>>T;
    while(T--)
    {
        cas++;
        cin>>S>>aa;
        for(i=0;i<=S;i++)
        {
            ar[i]=aa[i]-'0';
        }

        ans=0;
        temp=0;

        for(i=0;i<=S;i++)
        {
            if(temp<i)
            {
                ans+=(i-temp);
                temp=i;
            }
            temp+=ar[i];
        }

        printf("Case #%d: %d\n",cas,ans);

    }

}
