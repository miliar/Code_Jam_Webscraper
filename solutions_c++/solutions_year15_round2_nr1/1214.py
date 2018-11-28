/*
TASK: Problem A. Counter Culture
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
int tb[1000005];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0,y;
    tb[1]=1;
    queue<int> Q;
    char str[10];
    Q.push(1);
    while(!Q.empty())
    {
        k=Q.front();
        Q.pop();

        if(k+1<=1000000 && tb[k+1]==0)
        {
            tb[k+1]=tb[k]+1;
            Q.push(k+1);
        }

        sprintf(str,"%d",k);
        reverse(&str[0],&str[strlen(str)]);
        sscanf(str,"%d",&y);

        if(y<=1000000 && tb[y]==0)
        {
            tb[y]=tb[k]+1;
            Q.push(y);
        }
    }
    while(T--)
    {
        cin >> N;
        tt++;
        printf("Case #%d: %d\n",tt,tb[N]);
    }
}
