/*
TASK: Problem A. Senate Evacuation
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
    int tt=0;
    while(T--)
    {
        tt++;
        cin >> N;
        priority_queue<pair<int,char> > pq;
        for(i=0;i<N;i++)
        {
            cin >> k;
            pq.push(mp(k,i+'A'));
        }
        printf("Case #%d:",tt);
        pair<int,char> a,b,c;
        while(!pq.empty())
        {
            if(pq.size()==3 && pq.top().X==1)
            {
                a=pq.top();
                pq.pop();
                printf(" %c",a.Y);
                continue;
            }
            a=pq.top(); pq.pop();
            b=pq.top(); pq.pop();
            printf(" %c%c",a.Y,b.Y);
            a.X--;
            if(a.X!=0)
                pq.push(a);
            b.X--;
            if(b.X!=0)
                pq.push(b);
        }
        printf("\n");
    }
}
