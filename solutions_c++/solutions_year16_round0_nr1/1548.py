#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define ff first
#define ss second

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("w.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I=1;I<=t;I++){
        ll x;
        scanf("%I64d",&x);
        ll y=0;
        ll mask = 0;
        bool flag = false;
        for(int i=0;i<100000;i++){
            y+=x;
            ll z = y;
            while(z){
                mask |= (1<<(z%10));
                z/=10;
            }
            if(mask == (1<<10)-1){
                printf("Case #%d: %I64d\n",I,y);
                flag = true;
                break;
            }
        }
        if(!flag)printf("Case #%d: INSOMNIA\n",I);
    }
    return 0;
}
