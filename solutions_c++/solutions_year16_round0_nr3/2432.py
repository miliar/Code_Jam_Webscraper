#include <bits/stdc++.h>
using namespace std;
#define li long long int
#define rl(n) scanf("%lld", &n)
#define rll(m,n) scanf("%lld %lld", &m, &n)
#define rlll(m,n,o) scanf("%lld %lld %lld", &m, &n, &o)
#define ri(n) scanf("%d", &n)
#define rc(n) scanf("%c", &n)
#define rs(n) gets(s)
#define rst(n) getline(cin,n)
#define rfile(a) freopen(a, "r", stdin)
#define pi acos(-1.00)
#define pb push_back
#define mp make_pair
#define Pr printf
#define For(i,a,b) for(int i = a; i < b; i++)
#define MOD 1000003
#define eps 1e-9
#define ru(n) scanf("%llu",&n)
#define ruuu(m,n,o) scanf("%llu %llu %llu", &m, &n, &o)
#define ui unsigned long long int

li facs[1000001];

template <typename t1> t1 gcd(t1 a, t1 b) { return b == 0 ? a : gcd(b, a % b); }
template <typename t1> t1 lcm(t1 a, t1 b) { return a * (b / gcd(a, b)); }
template <typename t1> bool check (t1 i, t1 k){return i&((t1)1<<k);}
template <typename t1> t1 On(t1 i, t1 k) { return i|((t1)1 << k);}
template <typename t1> t1 Off(t1 i, t1 k) {return (i-((check(i,k))<<k) );}

li pw[12][20];

void power()
{
    for(int i = 1; i <= 10; i++)
    {
        li mul =1;
        for(int p = 0; p <= 18; p++)
        {
            pw[i][p]=mul;
            mul*=i;
        }
    }
}


int main()
{
    power();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tc = 1;  tc <= t; tc ++)
    {
        map<string, vector<li> > ans;
        int n;
        ri(n);
        int j;
        ri(j);
        int lim = 1<<(n-2);

        int bitval = 0;
        int sz=1;
        for(bitval = 0; bitval <= lim && sz <= j; bitval++)
        {
            bool flag = 1;
            vector<li> divs;
            bool faith=1;
            for(int base = 2; base <= 10 && faith; base++)
            {
                li num = 0;
                num+=1;
                for(int i = 0,p=1; i < n-2; i++,p++)
                {
                    num+=(check(bitval,i)*pw[base][p]);
                }
                num+=(1*pw[base][n-1]);
                int sqn = sqrt(num);
                int tri=0;
                for(int i = 2;i <= sqn; i++)
                {
                    if(num%i == 0)
                    {
                        divs.pb((li)i);
                        tri=1;
                        break;
                    }
                }
                faith&=tri;
            }
            if(divs.size() == 9)
            {
                string tmp(n,'0');
                tmp[n-1]='1';
                tmp[0]='1';
                for(int i = 0,j=n-2; i < n-2; i++,j--)
                {
                    int d = check(bitval,i);
                    tmp[j]=d+'0';
                }
//                cout<<bitval<<" "<<tmp<<endl;
                ans[tmp]=divs;
                sz++;
            }
        }
        printf("Case #%d:\n", tc);
        map<string, vector<li> > ::iterator it;
        for(it = ans.begin(); it != ans.end(); it++)
        {
            cout<<it->first;
            vector<li> tm = it->second;
            for(int i = 0; i < 9;i++)
            {
                printf(" %lld", tm[i]);
            }
            printf("\n");
        }
    }
}
