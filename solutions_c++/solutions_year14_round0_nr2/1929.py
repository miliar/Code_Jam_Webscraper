#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int TT;
    scanf("%d",&TT);
    for (int T=1;T<=TT;T++)
    {
        double c,f,x,ans=1e9,cnt=0;
        cin>>c>>f>>x;
        for (int i=0;;i++)
        {
            if (ans<cnt+x/(2+f*i)) break;
            else ans=cnt+x/(2+f*i);
            cnt+=c/(2+f*i);
        }
        printf("Case #%d: %.7lf\n",T,ans);
    }
    return 0;
}
