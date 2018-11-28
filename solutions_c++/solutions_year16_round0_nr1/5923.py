#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

ll cal(ll a)
{
    bool v[10]={false};
    for (ll i=a;i<=1000000000;i+=a)
    {
        ll j=i;
        while(j>0)
        {
            v[j%10]=true;
            j/=10;
        }
        int cnt=0;
        for(int k=0;k<10;k++)
            cnt+=v[k];
        if (cnt==10)
            return i;
    }
    return -1;
}
int main() {
    freopen("C:\\Users\\lpc\\Downloads\\A-large.in","r",stdin);
    freopen("e:\\codejam\\outL.txt","w",stdout);
    int t;
    int cs=0;
    scanf("%d",&t);
    while(t--)
    {
        int a;
        int ans;
        scanf("%d",&a);
        if (a==0)
            ans=0;
        else
            ans = cal(a);
        printf("Case #%d: ",++cs);
        if(ans==0)
            printf("INSOMNIA\n");
        else
            printf("%d\n",ans);

    }
//    for (int i = 1 ; i < 1000001; ++i) {
//        if (cal(i)==-1)
//        {
//            cout<<i<<endl;
//            break;
//        }
//    }
    return 0;
}