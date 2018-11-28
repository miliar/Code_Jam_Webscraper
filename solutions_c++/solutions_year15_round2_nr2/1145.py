/*
TASK: Problem B. Noisy Neighbors
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

int N,M,T,R,C,Mc;
bool tb[20][20];
void iSearch(int x,int y)
{
    if(x==R+1)
    {
        int k=0,co=0;
        for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++)
            {
                if(tb[i][j]==1)
                {
                    k++;
                    co+=(tb[i-1][j]+tb[i+1][j]+tb[i][j-1]+tb[i][j+1]);
                }
            }

        if(k==N)
        {
            Mc=min(Mc,co);
//            for(int i=1;i<=R;i++)
//            {
//                for(int j=1;j<=C;j++)
//                    printf("%d ",tb[i][j]);
//                printf("\n");
//            }
        }
        return;
    }
    tb[x][y]=1;
    if(y<C)
        iSearch(x,y+1);
    else
        iSearch(x+1,1);

    tb[x][y]=0;
    if(y<C)
        iSearch(x,y+1);
    else
        iSearch(x+1,1);
}
int si[9];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        tt++;
        cin >> R >> C >> N;
        M=R*C;
        if(R>C) swap(R,C);
        if((M+1)/2>=N)
            printf("Case #%d: %d\n",tt,0);
        else
        {
            Mc=11111;
            iSearch(1,1);
            printf("Case #%d: %d\n",tt,Mc/2);
        }
    }
}
