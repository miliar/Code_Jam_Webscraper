#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B large input.in","r",stdin);
    freopen("B large output.out","w",stdout);
    int n,i,j,ans;
    char x[105];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        ans=0;
        for(j=0;j<101;j++)
            x[j]=0;
        scanf("%s",x);
        for(j=1;x[j];j++)
            if(x[j]!=x[j-1])
                ans++;
        if(x[j-1]=='-')
            ans++;
        printf("Case #%d: %d\n",i+1,ans);
    }
}
