/*
TASK: Slides
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
int tb[55][55];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k;
    cin >> T;
    long long A,B,C;
    int tt=0;
    while(T--)
    {
        tt++;
        cin >> N >> A;
        memset(tb,0,sizeof tb);
        for(i=1;i<N;i++)
            for(j=i+1;j<N;j++)
                tb[i][j]=1;
        B=0;

            tb[1][N]=1;
            A--;
        for(i=2;i<N;i++)
        {
            if(A&(1LL<<(i-2)))
            {
                B|=(1LL<<(i-2));
                tb[i][N]=1;
            }
        }
        printf("Case #%d:",tt);
        if(B==A)
        {
            printf(" POSSIBLE\n");
            for(i=1;i<=N;i++)
            {
                for(j=1;j<=N;j++)
                    printf("%d",tb[i][j]);
                printf("\n");
            }
        }
        else
            printf(" IMPOSSIBLE\n");
    }
}
