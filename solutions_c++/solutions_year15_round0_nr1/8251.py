#include<bits/stdc++.h>
using namespace std;

// general
#define ll long long
#define pb push_back
#define pob pop_back
#define f first
#define s second
#define mp make_pair
//--------------

// IO funcs
#ifdef fastio

#define SC(x) scanf("%c",&x)
#define SD(x) x=fast_input()
#define SLL(x) scanf("%lld",&x)
#define SS(x) scanf("%s",x)

#define PC(x) printf("%c",x)
#define PD(x) fast_output(x)
#define PLL(x) printf("%lld",x)
#define PS(x) printf("%s",x)

#else // fastio

#define SC(x) cin>>x
#define SD(x) cin>>x
#define SLL(x) cin>>x
#define SS(x) cin>>x

#define PC(x) cout<<x
#define PD(x) cout<<x
#define PLL(x) cout<<x
#define PS(x) cout<<x

#endif

//----fastio-end---

// funcs
#define swap(a,b) a^=b^=a^=b
#define max(a,b) ((a) > (b))? (a) : (b);
//----------------

// statements
#define LP(i,ii,jj) for(int i=(ii);i<(jj);i++)
#define LPR(i,ii,jj) for(int i=(ii);i>=(jj);i--)
//----------------

// DS
#define vi vector<int>
#define pii pair<int,int>
#define mii map<int,int>
//----------------

const int MOD = 1000000007;

void PAns(int ans, int T)
{
    PS("Case #");
    PD(T);
    PS(": ");
    PD(ans);
    PC('\n');
}

void Solve(int T)
{
    int n;
    SD(n);
    string s;
    SS(s);
    int ans=0;
    LP(i,0,n+1)
    {
        bool flag=0;
        int nows=i;
        LP(j,0,n+1)
        {
            if(nows>=j)
            {
                nows+=(s[j]-'0');
            }
            else
            {
                flag=1;
                break;
            }
        }
        if(!flag)
        {
            ans=i;
            break;
        }
    }
    PAns(ans, T);
}

int main()
{
    int t;
    SD(t);
    LP(i,0,t)
    {
        Solve(i+1);
    }
    return 0;
}
