#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int r,c,w;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        cin >> r>>c>>w;
        int ans=(r-1)*(c/w) + (c/w - 1) + (c%w != 0) + w;
        t++;
        printf("Case #%d: %d\n",t,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
