#include<stdio.h>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
#include<cstdlib>
#include<cstring>
#include<string>
#include<set>
using namespace std;
 
#define DEBUG //on-off switch for printing statements
 
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9
 
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())

#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
 
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define mod 1000000007
#define F first
#define S second
#define pb push_back
#define B 27

void solve(int t)
{

	int l;
	s(l);
	int x;
	s(x);
	string a,b;
	cin >> a;
	b=a;
	for(int i=1;i<x;i++)
	a=a.append(b);
	int toget=0;
	int n=l*x;
	char prev='1';
	int sgn=0;
	int idx=-1;
	for(int i=0;i<n;i++)
	{
		if(a[i] == '1')
		continue;
		if(a[i] == 'i')
		{
			if(prev == '1')
			{
				prev='i';
			}
			else if(prev == 'j')
			{
				prev='k';
				sgn=(sgn+1)%2;
			}
			else if(prev == 'i')
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
			else
			{
				prev='j';
				
			}
		}
		else if(a[i] == 'j')
		{
			if(prev == '1')
			{
				prev='j';
			}
			else if(prev == 'j')
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
			else if(prev == 'i')
			{
				prev='k';
			}
			else
			{
				prev='i';
				sgn=(sgn+1)%2;
			}
		}
		else
		{
			if(prev == '1')
			{
				prev='k';
			}
			else if(prev == 'j')
			{
				prev='i';
			}
			else if(prev == 'i')
			{
				prev='j';
				sgn=(sgn+1)%2;
			}
			else
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
		}
		if(toget == 0 && prev == 'i' && sgn == 0)
		{
			toget++;
			prev='1';
		}
		else if(toget == 1 && prev == 'j' && sgn==0)
		{
			toget++;
			prev='1';
		}
		else if(toget == 2 && prev == 'k' && sgn==0)
		{
			toget++;
			idx=i;
			break;
		}
	}
	if(toget != 3)
	{
		printf("Case #%d: NO\n",t);
		return;
	}
	prev='1';
	sgn=0;
	for(int i=idx+1;i<n;i++)
	{
		if(a[i] == '1')
		continue;
		if(a[i] == 'i')
		{
			if(prev == '1')
			{
				prev='i';
			}
			else if(prev == 'j')
			{
				prev='k';
				sgn=(sgn+1)%2;
			}
			else if(prev == 'i')
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
			else
			{
				prev='j';
				
			}
		}
		else if(a[i] == 'j')
		{
			if(prev == '1')
			{
				prev='j';
			}
			else if(prev == 'j')
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
			else if(prev == 'i')
			{
				prev='k';
			}
			else
			{
				prev='i';
				sgn=(sgn+1)%2;
			}
		}
		else
		{
			if(prev == '1')
			{
				prev='k';
			}
			else if(prev == 'j')
			{
				prev='i';
			}
			else if(prev == 'i')
			{
				prev='j';
				sgn=(sgn+1)%2;
			}
			else
			{
				prev='1';
				sgn=(sgn+1)%2;
			}
		}
	}
	if(prev == '1' && sgn == 0)
	{
		printf("Case #%d: YES\n",t);
	}
	else
	{
		printf("Case #%d: NO\n",t);
	}		
	
	
}	
int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	{
		solve(i+1);
	}
}