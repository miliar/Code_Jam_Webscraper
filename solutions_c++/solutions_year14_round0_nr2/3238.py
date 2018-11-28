#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int INF=0x3f3f3f3f;
int mp[20];

int main()
{
    int tes;
    //freopen("abc.in","r",stdin);
    freopen("abc.txt","w",stdout);
    cin>>tes;
    double x,f,c,now,ans,rate;

    for(int cas=1;cas<=tes;cas++)
    {
        cin>>c>>f>>x;

        now=0,ans=INF,rate=2;
        while(now<ans)
        {
            ans=min(ans,now+x/rate);
            now+=c/rate;
            rate+=f;
        }
        printf("Case #%d: %.7lf\n",cas,ans);
    }
    return 0;
}
