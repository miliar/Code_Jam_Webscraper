#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
#include<iostream>
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
#define EPS                         1e-15
 
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
#define llu long long unsigned
#define ld long
#define INF 1000000000
 
#define mod 1000000007
 #define llu long long unsigned
#define ld long

int adj[11][11];
string a[11];
int arr[11];
ll ans=0;
void swap (int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
  
/* Function to print permutations of string
   This function takes three parameters:
   1. String
   2. Starting index of the string
   3. Ending index of the string. */
   int vis[26];
void permute(int *arr, int i, int n) 
{
   int j; 
   if (i == n)
   {
   	fill(vis,0);
   	char prev='0';
   	for(int j=0;j<=n;j++)
   	{
   		for(int k=0;k<a[arr[j]].size();k++)
   		{
   			if(a[arr[j]][k]!=prev)
   			{
   				if(vis[a[arr[j]][k]-'a'])
   				return;
   				else
   				vis[a[arr[j]][k]-'a']=1;
   			}
   			prev=a[arr[j]][k];
   		}
 
   	}

   	ans++;
   }
   else
   {
        for (j = i; j <= n; j++)
       {
          swap((arr+i), (arr+j));
          permute(arr, i+1, n);
          swap((arr+i), (arr+j)); //backtrack
       }
   }
} 

void solve(int t)
{	
	
	ans=0;
	fill(adj,0);
	int n;
	s(n);
	for(int i=0;i<n;i++)
	arr[i]=i;

	for(int i=0;i<n;i++)
	cin >> a[i];
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(j==i)
			continue;
			if(a[i][a[i].size()-1] == a[j][0])
			adj[i][j]=1;
			else
			adj[i][j]=0;
		}
	}
	permute(arr,0,n-1);
	printf("Case #%d: %lld\n",t,ans%mod);
}

int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}