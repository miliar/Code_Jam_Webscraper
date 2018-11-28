//#define WYTE
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back(x)
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define EPS 1e-9
#define MOD 1000000007
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int main()
{
    freopen("A-large.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,r,c,i,j,k,U,D,L,R,ans,err;
    char tb[133][133];
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++)
        {
            scanf("%s",tb[i]);
        }
        ans=0;
        err=0;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(tb[i][j]=='.')continue;
                //up
                U=0;
                for(k=i-1;k>=0;k--)
                {
                    if(tb[k][j]!='.')
                    {
                        U=1;
                        break;
                    }
                }
                //down
                D=0;
                for(k=i+1;k<r;k++)
                {
                    if(tb[k][j]!='.')
                    {
                        D=1;
                        break;
                    }
                }
                //left
                L=0;
                for(k=j-1;k>=0;k--)
                {
                    if(tb[i][k]!='.')
                    {
                        L=1;
                        break;
                    }
                }
                //right
                R=0;
                for(k=j+1;k<c;k++)
                {
                    if(tb[i][k]!='.')
                    {
                        R=1;
                        break;
                    }
                }
                if(tb[i][j]=='^')
                {
                    if(!U)
                    {
                        if(D|L|R)ans++;
                        else err=1;
                    }
                }
                else if(tb[i][j]=='v')
                {
                    if(!D)
                    {
                        if(U|L|R)ans++;
                        else err=1;
                    }
                }
                else if(tb[i][j]=='<')
                {
                    if(!L)
                    {
                        if(U|D|R)ans++;
                        else err=1;
                    }
                }
                else if(tb[i][j]=='>')
                {
                    if(!R)
                    {
                        if(U|D|L)ans++;
                        else err=1;
                    }
                }
            }
        }
        printf("Case #%d: ",ii);
        if(err)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n",ans);
        }
    }
}
