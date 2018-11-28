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
    while(t--)
    {
        int k,c,s; cin>>k>>c>>s;
        printf("Case #%d:",ca++);

        LL tmp = 1;
        for(int i=1; i<c; i++)
            tmp *= k;

        LL x = 1;
        for(int i=1; i<=k; i++){
            printf(" %lld", x);
            x += tmp;
        }
        printf("\n");
    }

    return 0;
}
