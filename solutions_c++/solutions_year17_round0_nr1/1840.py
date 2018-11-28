#include<bits/stdc++.h>
using namespace std;
const int N=1e3+20;
int t,n,k,i,j,ans,T;
char a[N];
bool impossible;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        ans=impossible=false;

        scanf(" %s %d",a,&k);
        n=strlen(a);

        for(i=0;i<n;i++)
        {
            if(a[i]=='+') continue;
            if(n-i<k) impossible=true;
            for(j=i;j<i+k;j++) a[j]=a[j]=='+'?'-':'+';
            ans++;
        }

        printf("Case #%d: ",++T);
        if(impossible) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}
