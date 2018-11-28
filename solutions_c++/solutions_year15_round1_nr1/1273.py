/*
TASK: Problem A. Mushroom Monster
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
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        tt++;
        int a=0,b=0;
        cin >> N;
        vi v;
        for(i=0;i<N;i++)
            cin >> k,v.pb(k);
        for(i=1;i<N;i++)
        {
            if(v[i]<v[i-1])
                a+=(v[i-1]-v[i]);
        }

        k=0;
        for(i=0;i<N-1;i++)
        {
            if(v[i]>v[i+1])
                k=max(k,v[i]-v[i+1]);
        }

        int x,y,z;
        for(i=0;i<N-1;i++)
        {
            x=v[i]-k;
            if(x<0) b+=v[i];
            else    b+=k;
        }
        //printf("%d\n",k);
        printf("Case #%d: %d %d\n",tt,a,b);
    }
}
