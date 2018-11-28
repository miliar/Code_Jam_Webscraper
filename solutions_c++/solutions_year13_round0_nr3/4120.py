/*Author : Punit Singh */
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<sstream>
using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
bool pali(ll i)
{
    string s = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
    int l=sz(s);
    rep(j,l/2)
    if(s[j]!=s[l-1-j])
        return false;
    return true;
}
vector<ll> pal(11005);
vector<ll>::iterator it;
void precompute()
{
    int cnt=0;
    for(ll i=1;i<10000002LL;i++)
    {
            if(pali(i))
            {
                pal[cnt++]=i;
            }
    }
}
int main()
{
    #ifdef TEST
    freopen("C-large-1.in","r",stdin);
 	freopen("out.txt","w",stdout);
    #endif
    precompute();
    int t,ctr=1;
    ll a,b,ra,rb,c,ans;
    scanf("%d",&t);
    while(ctr<=t)
    {
        ans=0LL;
        scanf("%lld%lld",&a,&b);
        ra=sqrt(a);
        rb=sqrt(b);
        it=lower_bound(pal.begin(),pal.end(),ra);
        if(a>((*it)*(*it)))
            it++;
        while(*it<=rb)
        {
            c=(*it)*(*it);
            if(pali(c))
                ans++;//,cout<<(*it)*(*it)<<",";
            it++;
        }
        printf("Case #%d: %lld\n",ctr++,ans);
    }
    return 0;
}
