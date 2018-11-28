#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#define LL long long
#define maxn 100100
#define inf 0x3f3f3f3f
#define IN freopen("in.txt","r",stdin);
using namespace std;


int main(int argc, char const *argv[])
{
    IN;
    freopen("out.txt","w",stdout);

    int t,ca=1; cin >> t;
    LL n;
    while(t--)
    {
        printf("Case #%d: ",ca++);
        int n;cin>>n;
        LL m = n;

        if(!n) {puts("INSOMNIA");continue;}

        int vis = 0;
        while(1){
            LL tmp = m;
            while(tmp){
                LL x = tmp%10;
                if(x==0) vis |= 1;
                else vis |= 1<<(x);
                tmp /= 10;
            }

            if(vis == 1023) {printf("%lld\n",m);break;}
            m += n;
        }
    }

    return 0;
}
