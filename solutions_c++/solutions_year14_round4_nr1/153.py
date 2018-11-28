#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<cstring>
#include<iostream>
int a[20000];
int t,n,m,o,r;
bool u[20000];
using namespace std;
int main()
{
    freopen("a-large.out","w",stdout);
    freopen("a-large.in","r",stdin);
    cin>>t;
    for(int zz=1;zz<=t;zz++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);
        o=0;
        r=n;
        memset(u,0,sizeof(u));
        while(r>0)
        {
            for(int i=n-1;i>=0;i--)
                if(!u[i])
                {
                    u[i]=true;
                    r--;
                    o++;
                    for(int j=n-1;j>=0;j--)
                        if(!u[j]&&a[i]+a[j]<=m)
                        {
                            u[j]=true;
                            r--;
                            break;
                        }
                    break;
                }
        }
        printf("Case #%d: %d\n",zz,o);
    }
    return 0;
}
