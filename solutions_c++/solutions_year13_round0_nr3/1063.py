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
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(int i=a;i<b;i++)
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
LL pal[1000];
int cnt;
LL A,B;
int size;
FILE *f1,*f2;

int nod(LL n)
{
int c=0;
while(n){n=n/10;c++;}
return c;    
}

bool isPal(LL n)
{
int a[100],i;
int f=nod(n);
for(i=f-1;i>=0;--i)
    {
    a[i]=n%10;
    n=n/10;
    }
for(i=0;i<=f/2;++i)
    if(a[i]!=a[f-i-1])return false;
return true;     
}
int bs(int l,int h,LL x)
{
    if(pal[l]==x)return l+1;
    if(pal[l]>x) return l;
    if(pal[h]==x) return h+1;
    if(x>pal[h])return h+1;
    int m=(l+h)/2;
    if(m==0){return 1;}
    if(pal[m]>x && pal[m-1]<=x)
    return m;
    if(pal[m]>=x&&pal[m-1]<x)
    return m+1;
    if(x>pal[m]) return bs(m+1,h,x);
    return bs(l,m-1,x);    
}

 
void preprocess()
{
     int i;
     LL sn;
	for(i=1;i<=10000009;++i)
	{
         if(isPal((LL)i))
         {
      //  cout<<"entering for "<<i<<"\n";
         sn=(LL)i*i;
         if(isPal(sn))pal[size++]=sn;            
         }            
    }
    //cout<<"size="<<size<<"\n";
//   for(i=0;i<size;++i)cout<<pal[i]<<" ";
//    cout<<"\n";
}

        
            


void solve()
{
     int x,y;
     x=bs(0,size-1,A-1);
     y=bs(0,size-1,B);
     x=y-x;
     fprintf(f2,"Case #%d: %d\n",testnum,x);return;
     
}
 
 
 
bool input()
{
     int i,j;
     fscanf(f1,"%lld%lld",&A,&B);
     
	return true;
}
 
 
int main()
{
	preprocess();
	int T=1;
	f1=fopen("E:\\A\\input.txt","r+");
	f2=fopen("E:\\output.txt","w");
	if(f1==NULL){cout<<"problem 1\n";}
	if(f2==NULL){cout<<"problem 2\n";}
	fscanf(f1,"%d",&T);
	for(testnum=1;testnum<=T;testnum++)
	{
		if(!input()) break;
		solve();
	}
return 0;
}
 
