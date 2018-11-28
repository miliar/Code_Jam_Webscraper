#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <utility>
#include <cstdlib>
#include <cassert>

#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define EPS 1e-9

using namespace std;

typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll;

int main()
{
    //freopen("B.txt","r",stdin);
    //freopen("B-small.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-output.txt","w",stdout);
    int T;
    cin>>T;
    rep(TI,T)
    {
        int n,m;
        cin>>n>>m;
        vector<vi> lawn(n,vi(m,0));
        rep(i,n)rep(j,m)cin>>lawn[i][j];
        vi row_high(n,0),col_high(m,0);
        rep(i,n)
        {
            rep(j,m)
            {
                row_high[i]=max(row_high[i],lawn[i][j]);
                col_high[j]=max(col_high[j],lawn[i][j]);
            }
        }
        //vector<vi> newl(n,vi(m,100));
        bool f=true;
        rep(i,n)
        {
            rep(j,m)
            {
                if(lawn[i][j]!=min(row_high[i],col_high[j]))
                {
                    f=false;
                    break;
                }
            }
        }
        printf("Case #%d: ",TI+1);
        if(f)printf("YES\n"); else printf("NO\n");
    }
    return 0;
}
