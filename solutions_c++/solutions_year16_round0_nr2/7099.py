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
string s;
main()
{
    in;out;
    ios_base::sync_with_stdio(0);
    cin>>k;
    for(a=0;a<k;a++)
    {
    	cin>>s;
    	n=s.si;
    	l=0;
    	while(1)
    	{
    		fl=-1;
    		for( i=0;i<n;i++ )
    		{
    			if( s[i]=='-' )fl=i;
    		}
    		if(fl==-1)
    		{
	    		cout<<"Case #"<<a+1<<": ";
    			cout<<l<<endl;
    			break;
    		}
    		i=0;
    		x=0;
    		while( i<n && s[i]=='+' )
    		{
    			s[i]='-';
    			i++;
    		}
    		if(i!=0)l++;
    		x=(fl+1)/2;
    		for( i=0;i<x;i++ )
    		{
    			swap(s[i],s[fl-i]);
    		}
    		for(i=0;i<=fl;i++)
    		{
    			if(s[i]=='-')s[i]='+';
    			else s[i]='-';
    		}
    		l++;
    	}
	}
    return 0;
}
