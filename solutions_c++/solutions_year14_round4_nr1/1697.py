#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;


bool ff[10009];
int main()
{
    freopen("inputA.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    int t=0;
    scanf("%d",&t);
    for(int h=0;h<t;h++)
    {
        int n,c;
        scanf("%d %d",&n,&c);
        int f[n];
        for(int g=0;g<n;g++) scanf("%d",&f[g]);
        sort(f,f+n);
        for(int bg=0;bg<10009;bg++) ff[bg]=false;
        int ans=0;
        while(1)
        {
            int nsum=0;
            int nco=0;
            for(int r=n-1;r>=0;r--)
            {
                if(nco<2 && c-nsum>=f[r] && ff[r]==false)
                {
                    ff[r]=true;
                    nsum+=f[r];
                    nco++;
                }
            }
            if(nsum==0) break;
            ans++;
        }
        printf("Case #%d: %d\n",h+1,ans);
    }
    return 0;
}
