#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define pi 2.0*acos(0.0)
#define MAX 100005

int p[100], d[15], sz;
LL MOD, a[15], power[15][40];

void sieve(int n)
{
    int i, k, sqrtN, status[100];

    sqrtN = (int)sqrt( (double)n );
    mem(status,0);

    for(i=3; i<=sqrtN; i+=2)
    {
        if(status[i>>1]==0)
        {
            for(k=i*i; k<=n; k+=i+i)
                status[k>>1] = 1;
        }
    }

    sz = 0;

    p[sz++] = 2;

    for(i=3; i<=n; i+=2)
    {
        if(status[i>>1]==0)
            p[sz++] = i;
    }
}

bool check()
{
    for(int i = 2; i <= 10; i++)
    {
        bool flag = true;

        for(int j = 0; j < 14; j++)
        {
            if(a[i] % p[j] == 0)
            {
                d[i] = p[j];
                flag = false;
                break;
            }
        }

        if(flag) return false;
    }

    return true;
}

int main()
{
    //READ("C-large.in");
    //WRITE("C-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, k, cnt, m;
    LL i, j, n;

    cin >> cases;
    //cases = 1;

    sieve(100);

    MOD = 1;

    for(i = 0; i < 14; i++)
        MOD = MOD * p[i];

    while(cases--)
    {
        cin >> n >> m;
        //n = 6;
        //m = 3;

        cout << "Case #" << ++caseno << ":\n";

        for(i = 2; i <= 10; i++)
        {
            power[i][0] = 1;

            for(j = 1; j <= n; j++)
                power[i][j] = ((power[i][j-1]%MOD) * i) % MOD;
        }

        LL z = 1LL<<(n-2);

        for(i = 0; i < z; i++)
        {
            if(m == 0) break;

            for(k = 2; k <= 10; k++)
                a[k] = ((power[k][0]%MOD)+(power[k][n-1]%MOD));

            for(j = 0; j < n-2; j++)
            {
                if(i & (1LL<<j))
                {
                    for(k = 2; k <= 10; k++)
                        a[k] = ((a[k]%MOD)+power[k][j+1])%MOD;
                }
            }

            if(check())
            {
                cout << 1;

                for(j = n-3; j >= 0; j--)
                {
                    if(i & (1LL<<j)) cout << 1;
                    else cout << 0;
                }

                cout << 1;

                for(j = 2; j <= 10; j++)
                    cout << " " << d[j];

                cout << NL;
                m--;
            }
        }
    }

    return 0;
}

