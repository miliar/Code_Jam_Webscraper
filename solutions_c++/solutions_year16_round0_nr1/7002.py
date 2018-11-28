#include<bits/stdc++.h>
#define in freopen("input.txt","r",stdin)
#define out freopen("output.txt","w",stdout)

#define inp freopen(".in","r",stdin)
#define outp freopen(".out","w",stdout)

using namespace std;

#define pb push_back
#define pf push_front
#define p_f pop_front
#define p_b pop_back
#define LL long long int
#define LD long double
#define MP make_pair
#define sqr(x) (x*x)
#define nwl pr("\n")
#define fi first
#define dist(x,y,xx,yy) sqrt( (x-xx)*(x-xx)+(y-yy)*(y-yy) )
#define lenint int intsi(int x){ int cnt=0; while(x>0){cnt++;x/=10;} return (cnt); }
#define se second
#define all(v) v.begin(),v.end()
#define sc scanf
#define DEBUG(a) cout<<#a<<" -> "<<a<<endl;
#define pr printf
#define si size()
#define str strlen
#define time clock()/(double)CLOCKS_PER_SEC
#define gcd LL GCD(LL a,LL b){ if(b==0)return a;else return GCD(b,a%b); }
const int INF=(-1u)/2;
const long long int INF2=(-1ull)/2;
int a,b,i,us[1011000],j,k,n,m,timer=0,l,r,x,y;
int cnt=0,fl=0,a2,a3=-1000000,ans=0;
void deb( bool a )
{
	if(a)return;
	pr("PROGRAM TERMINATED\n");
	exit(0);
}
main()
{
    in;out;
    ios_base::sync_with_stdio(0);
    cin>>k;
    for(i=0;i<k;i++)
    {
    	cin>>n;
    	for(j=0;j<10;j++)us[j]=0;
    	ans=0;
	    x=n;
	    if( x==0 )
	    {
	    	cout<<"Case #"<<i+1<<": ";
	    	cout<<"INSOMNIA\n";
	    	continue;
	    }
	    while( 1 )
	    {
	    	y=x;
	    	while( y>0 )
	    	{
	    		if( us[y%10]==0 )
	    		{
	    			ans++;
	    			us[y%10]=1;
	    		}
	    		y/=10;
	    	}
	    	if(ans==10)
	    	{
	    		cout<<"Case #"<<i+1<<": ";
	    		cout<<x<<"\n";
	    		break;
	    	}
	    	x+=n;
	    }
	}
    return 0;
}
