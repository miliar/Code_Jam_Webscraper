#include<bits/stdc++.h>

using namespace std;
int a[10000];
int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("pancakesres1.out", "wt", stdout);
    int k,t;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int n,i,j,mi=1e9,temp,r;
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }

        sort(a,a+n);
        for(i=1;i<=a[n-1];i++)
        {
            temp=0;
            for(j=n-1;j>=0;j--)
            {
                if(a[j]>i)
                {
                    r=a[j]-i;
                    temp+=1;
                    if(r%i==0)
                        temp+=(r/i-1);
                    else
                        temp+=r/i;
                }
            }
            temp=temp+i;
            mi=min(mi,temp);
        }
        printf("Case #%d: %d\n",k,mi);
    }
    return 0;
}
