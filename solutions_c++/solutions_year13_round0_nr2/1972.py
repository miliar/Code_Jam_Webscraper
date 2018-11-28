#include<iostream>
using namespace std;
#include<algorithm>
#include<set>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<deque>
#include<cstdio>
#include<map>

typedef long long lli;

#define fi(i,a,b,d) for(i=a;i<=b;i+=d)
#define fir(i,a,b,d) for(i=a;i>=b;i-=d)

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

#define vi vector<int>
#define all(v) v.begin(), v.end()

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front


#define inpi(i) scanf("%d", &i)
#define inplli(i) scanf("%lld", &i)
#define inpc(ch) scanf("%c", &ch)
#define printi(i) printf("%d\n", i)
#define printlli(i) printf("%lld\n", i)
#define printc(ch) printf("%c\n", ch)
#define inpfl(fl) scanf("%f", &fl)
#define printfl(fl) printf("%f", fl)


class className
{
    public:
    void solve()
    {
        int k, t, i, j, n, m, num;
        int mat[105][105], cols[105], rows[105];
        bool poss;

        cin>>t;

        fi(k,1,t,1)
        {
            cin>>n>>m;

            fi(i,0,104,1)
            {
                cols[i] = rows[i] = 0;
            }

            poss = true;

            fi(i,1,n,1)
            fi(j,1,m,1)
            {
                cin>>num;
                mat[i][j] = num;

                if(num>cols[j])
                cols[j] = num;

                if(num>rows[i])
                rows[i] = num;
            }

            fi(i,1,n,1)
            fi(j,1,m,1)
            {
                if(mat[i][j]<cols[j] && mat[i][j]<rows[i])
                {
                    poss=false;
                }
            }

            cout<<"Case #"<<k<<": ";

            if(poss)
            cout<<"YES\n";
            else
            cout<<"NO\n";
        }
    }
};

int main()
{
    className obj;

    obj.solve();
    return 0;
}
