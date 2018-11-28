#include<bits/stdc++.h>
using namespace std;
char s[1200];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T,i,j,k,sMax=0;
    scanf("%d",&T);
    for(t=0;t<T;t++)
    {
        scanf("%d",&sMax);
        scanf("%s",s);
        for(i=0;i<=sMax;i++)
        {
            s[i]-='0';
        }
        int sum=0;
        int add=0;
        for(i=0;i<sMax;i++)
        {
            sum+=s[i];
            while(sum<=i)
            {
                add++;
                sum++;
            }
        }
        printf("Case #%d: %d\n",t+1,add);
    }
}
