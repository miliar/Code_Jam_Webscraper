#include <bits/stdc++.h>
using namespace std;
#define N 10000000
typedef long long ll;
#define M 100000000
int sieve[M + 10];
int prime[N + 10];
int head;
void SIEVE()
{
    for(int i = 2 ; i<=N ; i++)
    {
        if(i <= 10000)
        {
            if(sieve[i] == 0)
            {
                head++;
                prime[head] = i;
                for(int j = i*i ; j<=N ; j+=i) sieve[j] = 1;
            }
        }
        else
        {
            if(sieve[i] == 0)
            {
                head++;
                prime[head] = i;
            }
        }
    }
}
vector<int> check(ll x,int len)
{
    vector <int> pdiv;
    for(int b = 2 ; b <= 10 ; b++)
    {
        ll temp = x;
        ll nu = 0;
        for(int i = 0 ; i<len ; i++)
        {
            nu = 1ll*nu*b;
            if(temp%2 == 1) nu = nu + 1;
            temp /= 2;
        }
        int flag = 0;
        for(int i = 1 ; i<=head && prime[i] < nu ; i++)
        {
            if(nu%prime[i] == 0)
            {
                pdiv.push_back(prime[i]);
                flag = 1;
                break;
            }
        }
        if(flag == 0) return pdiv;
    }
    return pdiv;
}
int JamCoin(int J,int TAR)
{
    ll p2 = pow(2,J-2);
    int cnt = 0;
    for(ll i = 0 ; i<p2 && cnt < TAR; i++)
    {
        ll temp = i + i + 1 + (1 << (J-1));
        vector <int> pdiv = check(temp,J);
        if(pdiv.size() == 9)
        {
            //printf("%lld ",i);
            for(int i = 0 ; i<J ; i++)
            {
                printf("%lld",temp%2);
                temp /= 2;
            }
            for(int i = 0 ; i<9 ; i++) printf(" %d",pdiv[i]);
            printf("\n");
            cnt++;
        }
    }
}
void Solve(int TestCase)
{
    int J,TAR;
    scanf("%d %d",&J,&TAR);
    printf("Case #%d:\n",TestCase);
    JamCoin(J,TAR);
}
int main()
{
    SIEVE();
    //freopen("C:\\Users\\dell\\Downloads\\inputc.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputc.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++) Solve(t);
    return 0;
}


