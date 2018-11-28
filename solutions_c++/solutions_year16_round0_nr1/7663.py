#include<bits/stdc++.h>
#define MOD 1000000007
#define MX 100010
#define ll long long
#define sc(n) scanf("%d",&n)
#define pr(m) printf("%d\n",m)
#define pi acos(-1.0)

using namespace std;
ll save[1000100];

ll check(ll n)
{
    ll saven=n,it=1;
    bool arr[10];
    memset(arr,0,sizeof(arr));
    while(arr[0]==0 || arr[1]==0 || arr[2]==0 || arr[3]==0 || arr[4]==0 || arr[5]==0 || arr[6]==0 || arr[7]==0 || arr[8]==0 || arr[9]==0)
    {
        saven=n*it++;
        while(saven){
            arr[saven%10]=1;
            saven/=10;
        }
    }
    saven=n*(it-1);
    return saven;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1large.txt","w",stdout);

    int t,tc=1,i;
    save[0]=-1;
    for(ll i=1;i<=1000000;i++){
        save[i]=check(i);
    }
//    for(ll i=1;i<=1000000;i++){
//        printf("%lld %lld\n",i,save[i]);
//    }
    sc(t);
    while(t--)
    {
        ll n;
        scanf("%lld",&n);
        if(save[n]==-1)printf("Case #%d: INSOMNIA\n",tc++);
        else printf("Case #%d: %lld\n",tc++,save[n]);

    }


    return 0;
}
