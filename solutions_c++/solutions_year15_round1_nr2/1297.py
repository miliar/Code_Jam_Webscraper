/*
TASK: Problem B. Haircut
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
    freopen("B-small-attempt1.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        cin >> N >> M;
        vi v,v1;
        int x,y,z;

        priority_queue<pair<int,int> > Q;

        y=1;
        for(i=0;i<N;i++)
        {
            cin >> k,v.pb(k);
            Q.push(mp(0,-i));
            x=__gcd(v[i],y);
            y=v[i]*y;  y/=x;
        }
//        printf("%d\n",y);
        z=M;
        while(M--)
        {
            j=-Q.top().X;
            k=-Q.top().Y;
            if(j==y)
                break;
            v1.pb(k);
            Q.pop();
            Q.push(mp(-(j+v[k]),-k));
        }
        tt++;
//        for(i=0;i<v1.size();i++)
//            printf("%d ",v1[i]);
        z--;
        printf("Case #%d: %d\n",tt,v1[z%v1.size()]+1);
    }
}
