#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll k,c,s;

int main()

{
    int T,cased=0;
//    freopen("a.txt","r",stdin);
//    freopen("b.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld%lld%lld",&k,&c,&s);
        printf("Case #%d:",++cased);

        for(ll i=1;i<=s;i++){

            printf(" %lld",i);
        }
        puts("");

    }


    return 0;
}







