#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
 
#define s(n)					scanf("%d",&n)
#define sc(n)					scanf("%c",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define debug(args...)			{dbg,args; cerr<<endl;}
#define dline					cerr<<endl	
 
 
 
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
 
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;
 
 
/*Main code begins now */
 
int testnum;
FILE *f1,*f2;
int r1,r2;
int a[5][5],b[5][5];

void preprocess()
{
     f1=fopen("E:/input.txt","r");
     f2=fopen("E:/output.txt","w");
}




void solve()
{
     r1--;
     r2--;
     int i,j,ans;
     int flag=0;
     for(i=0;i<4;++i)
     for(j=0;j<4;++j)
     if(a[r1][i]==b[r2][j])
     {
        flag++;
        ans=a[r1][i];                      
     }
     
     if(flag==0)
     fprintf(f2,"%s","Volunteer cheated!\n");
     else if(flag==1)
     fprintf(f2,"%d\n",ans);
     else 
     fprintf(f2,"%s","Bad magician!\n");
}

 
bool input()
{
     int i,j;
    fscanf(f1,"%d",&r1);
    for(i=0;i<4;++i)
    for(j=0;j<4;++j)
    fscanf(f1,"%d",&a[i][j]);
    
    fscanf(f1,"%d",&r2);
    for(i=0;i<4;++i)
    for(j=0;j<4;++j)
    fscanf(f1,"%d",&b[i][j]); 
    return true;
}
 
 
int main()
{
	int T=1;
	preprocess();
	fscanf(f1,"%d",&T);
	for(testnum=1;testnum<=T;testnum++)
	{
        fprintf(f2,"Case #%d: ",testnum);
        input();
		solve();
	}
return 0;
}
