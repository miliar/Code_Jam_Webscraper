#include<bits/stdc++.h>
using namespace std;

int a[10005];
int main()
{
    freopen("C:\\Users\\DARPAN\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\DARPAN\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        int maxi=0,n;
        cin>>n;
        for(int i=1;i<=n;i++)
        {
            cin>>a[i];
            if(maxi<a[i]) maxi=a[i];
        }
        int ans=maxi;
        for(int i=1;i<=maxi;i++)
        {
            int tt=0,maxo=0;
            for(int j=1;j<=n;j++)
            {
                if(a[j]>i)
                {
                    int kk;
                    if(a[j]%i==0) kk=0;
                    else kk=1;
                    tt+=(a[j]/i)+(kk)-1;
                    maxo=max(maxo,i);
                }
                else maxo=max(maxo,a[j]);
            }
            tt+=maxo;
            if(tt<ans)ans=tt;
        }
        printf("Case #%d: %d\n",k,ans);
        k++;
    }
    return 0;
}
