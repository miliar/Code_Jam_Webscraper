//Md. Ahsan Kabir Shohagh
#include<bits/stdc++.h>
using namespace std;
#define sz 100000
#define pb(a) push_back(a)
#define ll long long
#define ull unsigned long long
#define fread freopen("input.txt","r",stdin)
#define fwrite freopen("output.txt","w",stdout)
#define inf (1<<29)
#define mem(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
#define quick ios_base::sync_with_stdio(0)

int main()
{
    fread;
    fwrite;
    int t;
    ll n,ans;
    bool flg[10],insomnia;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        mem(flg,false);
        insomnia=true;
        scanf("%lld",&n);
        for(int i=1;n!=0; i++)
        {
            ll tmp = n*i;
            if(tmp==0)
            {
                flg[tmp]=true;
            }
            while(tmp>0)
            {
                flg[tmp%10]=true;
                tmp/=10;
            }
            int j=0;
            while(j<10 && flg[j]==true)
            {
                j++;
            }
            if(j==10)
            {
                ans=n*i;
                insomnia=false;
                break;
            }
//            cout<<i<<endl;
        }
        if(insomnia)
        {
            printf("Case #%d: INSOMNIA\n",ca);
        }
        else
        {
            printf("Case #%d: %lld\n",ca,ans);
        }
    }
    return 0;
}
