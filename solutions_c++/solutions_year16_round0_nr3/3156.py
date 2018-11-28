#include <bits/stdc++.h>

using namespace std;
int N,J;
vector<long long> divi;

void print(long long k)
{
    string s;
    while(k)
    {
        if(k % 2 == 0)
            s += "0";
        else
            s += "1";
        k /= 2;
    }
    reverse(s.begin(),s.end());
    cout << s;
}

long long power(long long x,long long b)
{
    long long x1 = x,x2 = 1;
    while(b)
    {
        if(b&1)
        {
            x2 = x1 * x2;
            --b;
        }
        else
        {
            x1 = x1 * x1;
            b /= 2;
        }
    }
    return x2;
}

long long convert(long long k,long long base)
{
    long long rez = 0;
    for(long long i = 0; i < N; ++i)
        if (k & (1LL<<i))
            rez += power(base,i);
    return rez;
}

bool okay(long long k)
{
    divi.clear();
    long long rez = 0;
    for(int base = 2; base <= 10; ++base)
    {
        rez = convert(k,base);
        for(long long d = 2; d*d <= rez; ++d)
            if(rez % d == 0)
            {
                divi.push_back(d);
                break;
            }
        if(divi.size() != base - 1)
        {
            divi.clear();
            return false;
        }
    }
    return true;
}

void Solve()
{
    scanf("%d%d",&N,&J);
    int cnt = 0;
    long long crt = 1LL << (N-1);
    while(1)
    {
        while(crt % 2 == 0 || !okay(crt))
            ++crt;
        ++cnt;
        print(crt);
        printf(" ");
        for(auto it : divi)
            printf("%d ",it);
        printf("\n");
        if(cnt == J)
            break;
        ++crt;
    }
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    int T;
    scanf("%d",&T);
    printf("Case #1:\n");
    Solve();

    return 0;
}
