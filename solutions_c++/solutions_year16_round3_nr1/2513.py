//OM
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <algorithm>
using  namespace  std;

#define  x first
#define  y second
#define  pb push_back
#define  mp make_pair
#define  PI (acos(-1.0))
#define  mem(a,b) memset(a,b,sizeof(a))
#define  Sort(x) sort(x.begin(),x.end())
#define  FOR(i, b, e) for(int i = b; i <= (int)(e); i++)
#define  FORR(i, b, e) for(int i = b; i >=(int)(e); i--)
#define  FORI(i, s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
#define  pr(x) cout<<x<<"\n"
#define  prs(x) cout<<x<<" "
#define  pr2(x,y) cout<<x<<" "<<y<<"\n"
#define  pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
#define  ppr(a) cout<<a.x<<" "<<a.y<<"\n"

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double , double> pdd;
typedef  vector <int> vi;
typedef  vector <pii> vpii;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction

#define  EPS 1e-9
#define  MAX 100007
vector<pair<int,int > > a;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,n,w;
    scanf("%d",&T);
    FOR(cs,1,T)
    {
        scanf("%d",&n);
        FOR(i,0,n-1)
        {
            scanf("%d",&w);
            a.pb(mp(w,i));
        }
        printf("Case #%d:",cs);
        while(1)
        {
            bool ache=false;
            int sum=0;
            FOR(i,0,n-1)if(a[i].x>0){
                ache=true;
                //break;
                sum+=a[i].x;
            }
            if(!ache)break;
//            pr(sum);
            sort(a.begin(),a.end(),greater<pair<int,int >  >());
            //if(sum-a[0].x<a[0].x) printf("DEFFEEEEEEEEEE ");
            if((int)a.size()>2 &&a[0].x==a[1].x&&a[1].x==a[2].x )
            {
                printf(" %c",a[0].y+'A');
                a[0].x--;
            }
            else if(a[0].x==a[1].x)
            {
                printf(" %c%c",a[0].y+'A',a[1].y+'A');
                a[0].x--;
                a[1].x--;
            }
            else
            {
                printf(" %c",a[0].y+'A');
                a[0].x--;
            }
        }
        printf("\n");
        a.clear();

    }
    return 0;
}
