#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,n,c1,c2,k;
    string a;
    long long ans;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        cin>>a;
        n=a.size();
        c1=-1;c2=-1;
        ans=0;
        for(i=0;i<n;i++)
        {
            if(a[i]=='-')
            {

                if(i==0)
                 {
                     c1=i;
                     c2=i;
                 }
                else if(a[i-1]=='+')
                {
                    c1=i;
                    c2=i;
                }
                else if(a[i-1]=='-')
                    c2++;

            }
            else
            {
                if(c1==0&&c2!=-1)
                {
                    ans+=1;
                }
                else if(c1>0&&c2>=0)
                {
                    ans+=2;
                }
                c1=-1;
                c2=-1;
            }


        }
        if(c1!=-1&&c2!=-1)
        {
            if(c1>0)
            ans+=2;
            else
            ans+=1;
        }
        printf("Case #%d: %lld\n",k,ans);

    }

}
