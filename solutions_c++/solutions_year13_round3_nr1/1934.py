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
VL nums;
 
int cnt;
char s[200];
int l,n; 
bool flag[200][200];
FILE *f1,*f2; 
void preprocess()
{
	
}
bool isvowel(char ch)
{
     if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')return true;
     return false;
}
bool check(int i,int j)
{
     int x,y;
  //   cout<<"inside chk for i="<<i<<" and j="<<j<<"\n";
     for(x=i;x<=j-n+1;++x)
     {
     if(!isvowel(s[x]))
        {
        for(y=0;y<n;++y)  if(isvowel(s[x+y])) break; 
        if(y==n){return true;}         
        }                  
     }  
    // cout<<"returning false\n";
     return false;  
} 
void solve()
{
     int ans=0,i,j;
     for(i=0;i<l;++i)for(j=0;j<l;++j)flag[i][j]=false;
	for(i=0;i<l;++i)
	{
    for(j=i+n-1;j<l;++j)
    {
        if((j-1-i+1)>=n&&flag[i][j-1])flag[i][j]=true;    
        if(!flag[i][j])
        {
        flag[i][j]=check(i,j);               
        }        
    }                
    }
    
    for(i=0;i<l;++i)
	{
    for(j=i+n-1;j<l;++j)
    {
        if(flag[i][j])ans++;          
    }                
    }
	fprintf(f2,"Case #%d: %d\n",testnum,ans);
    cout<<ans<<"\n";	
}
 
 
 
bool input()
{
     fscanf(f1,"%s",s);
     while(strlen(s)==0)gets(s);
     l=strlen(s);
     fscanf(f1,"%d",&n);
	return true;
}
 
 
int main()
{
	preprocess();
	f1=fopen("E:/A/input.txt","r");
	f2=fopen("E:/A/output.txt","w");
	if(f1==NULL || f2==NULL)cout<<"error\n";
	int T=1;
	fscanf(f1,"%d",&T);
	for(testnum=1;testnum<=T;testnum++)
	{
		if(!input()) break;
		solve();
	}
return 0;
}
 
