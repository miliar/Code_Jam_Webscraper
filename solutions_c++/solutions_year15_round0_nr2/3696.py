#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n;
int p[3000];


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--)
    {
        cin>>n;
        for (int i=0;i<n;++i)
            cin>>p[i];
        int ans = (1<<30);
        for (int i=1;i<=1000;++i)
        {
            int sum=0;
            for (int j=0;j<n;++j)
                sum+=(p[j]+i-1)/i-1;
            ans = min(ans,sum+i);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }




}
