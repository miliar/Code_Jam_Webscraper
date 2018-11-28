#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int llu;

#define s(x) scanf("%d",&x);
#define p(x) printf("%d \n",x);
#define sl(x) scanf("%ld",&x);
#define sll(x) scanf("%lld",&x);
#define sllu(x) scanf("%llu",&x);
#define pl(x) printf("%ld \n",x);
#define sll(x) scanf("%lld",&x);
#define pll(x) printf("%lld \n",x);
#define pllu(x) printf("%llu \n",x);

FILE *fin=freopen("D-small-attempt1.in","r",stdin);
FILE *fout=freopen("1_jam_q4_small.txt","w",stdout);

int main()
{
    int t;s(t);
    for(int i=1;i<=t;i++)
    {
        int K,C,S;s(K);s(C);s(S);
        printf("Case #%d:",i);
        for(int x=1;x<=K;x++)
            printf(" %d",x);
        printf("\n");
    }
}
