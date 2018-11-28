#include<cstdio> 
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int t, n, k, ans, cont, d[1000], c[1000];
char s[1000];
int main()
{
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        scanf("%s",s);
        n=strlen(s);
        for (int j=0; j<n; j++)
        if (s[j]=='-')
        d[j+1]=0;
        else
        d[j+1]=1;
        ans=0;   k=n; cont=0;
        while (k>0 && cont<=1000)
        {
            if (d[k]==1 && k==n)
            n--;
            else
            if (d[k]==1 || (d[k]==0 && d[1]==0))
            {
              ans++;
              if (d[1]==0)
                k=n;
              for (int j=1; j<=k; j++)
              if (d[j]==0)
               c[j]=1;
              else
               c[j]=0;
              for (int j=1; j<=k; j++)
              d[k-j+1]=c[j];
              k=n+1;
            }
            k--;
            cont++;
        } 
        if (cont==1001)
        printf("Case #%d: %s\n",i,s);
        else
        {
        if (n>0)
        ans++;
        printf("Case #%d: %d\n",i,ans);
        }
    } 
    return 0;
}
