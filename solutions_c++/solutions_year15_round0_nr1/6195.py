#include <cstdio>
#include <cstring>

int main()
{
    int t,n,ans,i,np,j;
    char s[1005];
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        ans=0;
        np=0;
        scanf("%d %s",&n,s);
        
        for(i=0;i<n+1;i++)
        {
            
            if(np<=i)
            {
                ans+=i-np;
                np=i;
            }
            np+=s[i]-'0';
            
        }
        printf("Case #%d: %d\n",j,ans);
    }
}
