#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#define maxn 1008
using namespace std;

int a[maxn];

int main()
{
    int n,i,T,j,tt=0;
    char ch;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>T;

    while (T--)
    {
        printf("Case #%d: ",++tt);
        memset(a,0,sizeof(a));
        cin>>n;

        for (i = 0 ; i <= n ; i++)
        {
            scanf(" %c",&ch);
            a[i] = ch - '0';
        }
        int s = 0,ans = 0;
        for (i = 0 ; i <= n ; i++)
        {
            if (s >= i)
                s += a[i];
            else
                ans += i - s,s = i + a[i];
        }
        cout<<ans<<endl;
    }


    return 0;
}
