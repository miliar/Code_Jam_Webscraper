#include <bits/stdc++.h>
using namespace std;
 double pi=3.14159265359;
 long long r,c;
 char arr[105][105]={0};
#define infinity (1000000007)
#define ll long long
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define pip pair<int,pii>
typedef vector<int> vi;
typedef vector<pii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define pb push_back
#define s(n) scanf("%lld",&n)
#define s2(n,m) scanf("%lld%lld",&n,&m)
#define s3(n,m,l) scanf("%lld%lld%lld",&n,&m,&l)
#define rep(i,n) for(long long i=0;i<n;i++)
ll pwr(ll a,ll b,ll mod) {ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
long long mod=1000000007;
bool move_up(long long i,long long j)
{
    i--;
	for(;(i>=0);i--)
   	{
     if(arr[i][j]!='.')
    break;
    
    	}
    if(i==-1)
	return false;
	else
	return true;	
}
bool move_down(long long i,long long j)
{
    i++;
	for(;(i<r);i++)
   	{
     if(arr[i][j]!='.')
    break;
    
    	}
    if(i==r)
	return false;
	else
	return true;	
}
bool move_left(long long i,long long j)
{
    j--;
    
	for(;(j>=0);j--)
   	{
   	
     if(arr[i][j]!='.')
    break;
    
    	}
    if(j==-1)
	return false;
	else
	return true;	
}
bool move_right(long long i,long long j)
{
    j++;
   
	for(;(j<c);j++)
   	{
   	
     if(arr[i][j]!='.')
    break;
    
    	}
    
    if(j==c)
	return false;
	else
	return true;	
}
int main()
{
	long long a=0,b,d,i,j,l,sum,result,n,m,k,s,t,flag,count;
	
    scanf("%lld",&t);
    while(t--)
    {
    	scanf("%lld%lld",&r,&c);
    	for(i=0;i<r;i++)
    	{
    		for(j=0;j<c;j++)
    		{
    			scanf(" %c",&arr[i][j]);
    		}
    	}
//    	for(i=0;i<r;i++)
//    	{
//    		for(j=0;j<c;j++)
//    		{
//    			printf(" %c",arr[i][j]);
//    		}
//    		printf("\n");
//    	}
    	count=0;flag=1;
    	for(i=0;i<r;i++)
    	{
    		for(j=0;j<c;j++)
    		{
    			if(arr[i][j]!='.')
    			{
    			    	k=i;l=j;
    					if(arr[k][l]=='>')
    				    {
    				    
    				    	if(move_right(i,j))
    				    	continue;
    				    	else
    				    	{
    				    		count++;
    				    		if(move_left(i,j)||move_up(i,j)||move_down(i,j))
    				    		continue;
    				    		else
    				    		{
    				    			flag=0;
    				    		break;
    				    		}
    				    	}
    				    
    				    }
    				    else if(arr[k][l]=='<')
    				    {
    				    	
    				    	if(move_left(i,j))
    				    	continue;
    				    	else
    				    	{
    				    		count++;
    				    		if(move_right(i,j)||move_up(i,j)||move_down(i,j))
    				    		continue;
    				    		else
    				    		{
    				    			flag=0;
    				    		break;
    				    		}
    				    	}
    				    
    				    }
    				    else if(arr[k][l]=='^')
    				    {
    				    	
    				    	if(move_up(i,j))
    				    	continue;
    				    	else
    				    	{
    				    		count++;
    				    	
    				    		if(move_left(i,j)||move_right(i,j)||move_down(i,j))
    				    		continue;
    				    		else
    				    		{
    				    		
    				    			flag=0;
    				    		break;
    				    		}
    				    	}
    				    	
    				    }
    				    else 
    				    {
    				    	
    				    	if(move_down(i,j))
    				    	continue;
    				    	else
    				    	{
    				    		count++;
    				    		if(move_left(i,j)||move_up(i,j)||move_right(i,j))
    				    		continue;
    				    		else
    				    		{
    				    			flag=0;
    				    		break;
    				    		}
    				    	}
    				    	
    				    }
    				
    			}
    		}
    		if(flag==0)
    		break;
    	}	
    	if(flag==0)
    	printf("Case #%lld: IMPOSSIBLE\n",++a);
    	else
    	printf("Case #%lld: %lld\n",++a,count);
    }
	return 0;
}





