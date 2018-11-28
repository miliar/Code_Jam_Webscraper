#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        string s;
        cin>>s;
        n=s.size();
        int i,j,k,ans=0;
        for(i=n-1;i>=0;i--)
        {
            for(j=i;j>=0;j--)
                if(s[j]=='-')
                    break;
            if(j==-1)
                break;
            if(j!=0)
            {
                for(k=0;k<j;k++)
                    if(s[k]=='-')
                        break;
                    else
                        s[k]='-';
                if(k!=0)
                    ans++;
            }
            reverse(s.begin(),s.begin()+j+1);
            for(int k=0;k<=j;k++)
                if(s[k]=='-')
                    s[k]='+';
                else
                    s[k]='-';
            ans++;
            i=j;
        }
        printf("Case #%d: %d\n",cs,ans);
        cs++;
    }
    return 0;
}
