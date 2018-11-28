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

FILE *fin=freopen("A-large.in","r",stdin);
FILE *fout=freopen("jam_final_q1_large_out.txt","w",stdout);

int main()
{
    int t;s(t);
    for(int i=1;i<=t;i++)
    {
        ll n,temp,step;sll(n);
        step=n;
        set<int> S;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i);continue;
        }
        while(true)
        {
            temp=n;
            while(temp)
            {
                S.insert(temp%10);
                temp /= 10;
            }


            if(S.size()==10)
            {
                    printf("Case #%d: %lld\n",i,n);

                    break;
            }
            n+=step;
        }
    }
}
