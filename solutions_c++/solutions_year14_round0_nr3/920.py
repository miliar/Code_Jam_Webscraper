#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cassert>
 
using namespace std;
 
#define DEBUG //on-off switch for prlling statements
 
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants
#define EPS                         1e-12
 
// Useful hardware instructions
#define bitcount1                    __builtin_popcount1
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(ll i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((ll)(a.size()))
 
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define mod 1000000009
#define llu long long unsigned
#define ld long
#define INF 1000000000
int a[51][51];
int vis[51][51];
int r,c,m;
void print()
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(i == r-1 && j == 0)
			{
				printf("c");
				continue;
			}
			if(vis[i][j] == 0)
			{
				printf("*");
			}
			else
			printf(".");
		}
		printf("\n");
	}
	//printf("\n");
}
void blast(int i,int j)
{
	vis[i][j]=1;
	if(i!=0)
	vis[i-1][j]=1;
	if(i!=0 && j!=c-1)
	vis[i-1][j+1]=1;
	if(j!=c-1)
	vis[i][j+1]=1;

}
void solve(int t)
{
	printf("Case #%d:\n",t);
	s(r);
	s(c);
	s(m);
	//printf("%d %d %d\n",r,c,m);
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		vis[i][j]=0;
	}
	m=r*c-m;
	if(m == 0)
	{
		print();
		return;
	}
	if(m == 1)
	{
		vis[r-1][0]=1;
		print();
		return;
	}
	if( r == 1 || c == 1)
	{
		int flag=0;
		for(int i=0;i<r;i++)
		{

			for(int j=0;j<c;j++)
			{
				if(m==0){
				flag=1;
				}
				if(i == 0 && j== 0)
				{
					printf("c");
					m--;
					if(m==0)
					flag=1;
					continue;
				}		
				if(flag == 0){
				printf(".");
				m--;
				if(m==0)
				flag=1;
				}
				else
				{
					printf("*");
				}
			}
			printf("\n");
		}
		//	printf("haha");
		//print();
		return;
	}
	else if(r == 2 || c == 2) 
	{
		if(m == 2 || m == 3 || (m%2) == 1)
		{
			printf("Impossible\n");
			return;
		}
		blast(r-1,0);
		m=m-4;
		if(m == 0)
		{
			print();
			return;
		}
		for(int j=1;j<c-1;j++)
		{
			blast(r-1,j);
			m=m-2;
			if(m == 0)
			{
				print();
				return;
			}
		}
		for(int i=r-2;i>=0;i--)
		{
			for(int j=0;j<c-1;j++)
			{
				blast(i,j);
				m=m-2;
				if(m == 0)
				{
					print();
					return;
				}
			}
		}
	}	
	else
	{
		if(m == 2 || m == 3 || m==5 || m == 7)
		{
			printf("Impossible\n");
			return;
		}
		blast(r-1,0);
		m=m-4;
		if(m == 0)
		{
			print();
			return;
		}
		blast(r-1,1);
		m=m-2;
		if(m == 0)
		{	
			print();
			return;
		}
		blast(r-2,0);
		m=m-2;
		if(m==0)
		{
			print();
			return;
		}
		for(int j=2;j<c-1;j++)
		{
			if(m == 1)
			{
				blast(r-2,1);
				print();
				return;
			}
			blast(r-1,j);
			m=m-2;
			if(m == 0)
			{
				print();
				return;
			}
		}
		for(int i=r-2;i>=0;i--)
		{
				//printf("%d %d\n",m,i);
		//		print();
			if(i!=1)
			{
				if(m == 1)
				{
					blast(i,1);
					print();
					return;
				}
				blast(i-1,0);
				m=m-2;
			}
			if(m == 0)
			{
				print();
				return;
			}
			for(int j=1;j<c-1;j++)
			{
				blast(i,j);
				m=m-1;
				if(m==0)
				{
					print();
					return;
				}
			}
		}
		print();
		return;	
	}
}
		
			


int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}