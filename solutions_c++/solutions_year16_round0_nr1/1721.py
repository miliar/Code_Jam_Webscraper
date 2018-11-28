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
#define MOD 1000000007
#define MAX 100005

int k, v[15];
bool flag;

void process(LL x)
{
    while(x > 0)
    {
        int y = x%10;
        if(v[y] == 0) k--;
        v[y] = 1;
        x /= 10;
    }

    if(k == 0) flag = true;
}

int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, i;
    LL n, m;

    cin >> cases;

    while(cases--)
    {
        cin >> n;

        m = n;
        flag = false;
        mem(v,0);
        k = 10;

        FOR(i,0,100000)
        {
            process(m);
            if(flag) break;
            m += n;
        }

        if(flag) cout << "Case #" << ++caseno << ": " << m << NL;
        else cout << "Case #" << ++caseno << ": INSOMNIA\n";
    }

    return 0;
}

