/*
TASK: Counting Sheep
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    cin >> T;
    long long a,b,c,d,Mc=(1LL<<10)-1;
    int tt=0;
    while(T--)
    {
        cin >> a;
        tt++;
        if(a==0)
        {
            printf("Case #%d: INSOMNIA\n",tt);
            continue;
        }
        d=0;
        k=0;
        do
        {
            k++;
            b=a*k;
            while(b)
            {
                d|=(1LL<<(b%10));
                b/=10;
            }
        }
        while(Mc!=d);
        printf("Case #%d: %I64d\n",tt,a*k);
    }
}
