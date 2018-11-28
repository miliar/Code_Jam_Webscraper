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
void precompute()
{

}
vector<int> p;
int d,ans,limit;
int solve(vector<int> p,int l)
{
    sort(p.begin(),p.end());
    int d=p.size();
    if(p[d-1]<3||l>limit)
        return p[d-1];
    int t=p[d-1];
    p[d-1]/=2;
    int n=t-p[d-1];
    p.push_back(n);
    int t1=solve(p,l+1);
    if(t==9)
    {
        p.pop_back();
        p[d-1]=6;
        p.push_back(3);
        int t9=solve(p,l+1);
        t1=min(t1,t9);
    }

    //p[d-1]=t;
    //p.pop_back();
    //rep(i,sz(p))
    //    p[i]--;
    //int t2=solve(p,l+1);
    return min(1+t1,t);
}
int main()
{
    #ifdef TEST
    freopen("B-small-attempt4.in","r",stdin);
 	freopen("b-out2.txt","w",stdout);
    #endif
    precompute();
    int t,ctr=1,x;
    cin>>t;
    while(ctr<=t)
    {
        cin>>d;
        for(int i=0;i<d;i++){
            cin>>x;
            p.push_back(x);
        }
        sort(p.begin(),p.end());
        limit=p[d-1];
        ans=0;
        ans=solve(p,0);
        printf("Case #%d: %d\n",ctr++,ans);
        p.clear();
    }
    return 0;
}
