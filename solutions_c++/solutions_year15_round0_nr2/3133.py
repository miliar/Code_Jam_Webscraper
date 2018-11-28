#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<queue>
#define maxn 1008
using namespace std;

int a[maxn];

int main()
{
    int n,i,T,j,tt=0;
    char ch;
    int minn;
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    cin>>T;

    while (T--)
    {
        printf("Case #%d: ",++tt);

        int n,x,i,j,maxx=0;

        cin>>n;

        for (i=1;i<=n;i++)
        {
            cin>>a[i];
            maxx=max(maxx,a[i]);
        }

        for (i=1;i<=maxx;i++)
        {
            int s=0;
            for (j=1;j<=n;j++)
            {
                if (a[j]%i==0) s+=a[j]/i-1;
                else s+=a[j]/i;
            }
            s+=i;
            maxx=min(maxx,s);
        }
        cout<<maxx<<endl;

    }


    return 0;
}
