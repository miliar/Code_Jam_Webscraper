#include <iostream>

using namespace std;

int main()
{
    int tc,i,a,b,kk,j,k;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>tc;
    for(i=1;i<=tc;i++)
    {
        long int ans=0;
        cin>>a>>b>>kk;
        for(j=0;j<a;j++)
        {
            for(k=0;k<b;k++)
            {
                if((j&k)<kk)
                {
                    //printf("%d %d\n",j,k);
                    ans++;
                }
            }
        }
        printf("Case #%d: %ld\n",i,ans);
    }
    return 0;
}
