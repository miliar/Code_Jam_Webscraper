#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outpanmain.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int q=1;q<=t;q++)
    {
        string a;
        int k;
        cin>>a>>k;
        int l=a.length();
        int ans=0,flag=0;
        for(int w=0;w<l;w++)
        {
            //cout<<a<<endl;
            if(a[w]=='+') continue;
            else if(a[w]=='-')
            {
                if((l-w)<k)
                {
                    flag=1;
                    break;
                }
                for(int e=w;e<w+k;e++)
                {
                    if(a[e]=='-') a[e]='+';
                    else a[e]='-';
                }
                ans++;
            }
        }
        if(flag==1)
        {
            printf("Case #%d: IMPOSSIBLE\n",q);
        }
        else
        {
            printf("Case #%d: %d\n",q,ans);
        }
    }
}
