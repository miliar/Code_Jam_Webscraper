#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int i,j,n,k,ans=0;
        string s;
        cin>>s>>k;
        n=s.size();
        for(i=0;i<n;i++)
        {
            if(s[i]=='+'||i+k>n)
                continue;
            ans++;
            for(j=i;j<i+k;j++)
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
        }
        for(i=0;i<n;i++)
            if(s[i]=='-')
                break;
        printf("Case #%d: ",cs);
        cs++;
        if(i!=n)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
