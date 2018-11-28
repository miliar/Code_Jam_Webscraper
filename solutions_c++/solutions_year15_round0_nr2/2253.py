/*
TASK: Problem B. Infinite House of Pancakes
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
int v[1005];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        tt++;
        cin >> N;
        memset(v,0,sizeof v);
        j=0;
        for(i=0;i<N;i++)
            cin >> k ,v[k]++,j=max(j,k);
        int Mc=j;

        for(i=j-1;i>=1;i--)
        {
            k=0;
            for(int a=j;a>i;a--)
            {
                k+=(((a-1)/i)*v[a]);
            }
            //printf("[%d] %d\n",i,k+i);
            Mc=min(Mc,k+i);
        }
        printf("Case #%d: %d\n",tt,Mc);
    }
}
