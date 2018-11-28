#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int fil[100100];
bool use[100100];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int cas=1;
    scanf("%d",&T);
    while(T--)
    {
        memset(use,0,sizeof(use));
        int n,cap;
        scanf("%d%d",&n,&cap);
        for(int i=0;i<n;i++)
            scanf("%d",&fil[i]);
        sort(fil,fil+n);
        int ans=0;
        for(int j=n-1;j>=0;j--)
            if(!use[j])
        {

            ans++;
            int i=upper_bound(fil,fil+j,cap-fil[j])-fil;

            int k;
            for( k=i-1;k>=0;k--)
                if(!use[k])
            {
                use[k]=1;
                break;
            }

        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
