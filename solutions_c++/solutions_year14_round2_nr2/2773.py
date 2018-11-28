
#include<bits/stdc++.h>
#define debug(args...){dbg,args; cerr<<endl;}args
#define sqr(x) ( (x)*(x) )
#define Size(a) int((a).size()) 
#define pb push_back
#define mset(x,v) memset(x,v,sizeof(x))
#define all(c) (c).begin(),(c).end() 
#define SORT(x) sort(all(x))
#define tr(c,i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define chk(x,n) ( x[n>>6] & (1<< ( (n>>1) & 31) )  ) // checks if  the bit corresponding to n is 1 
#define set(x,n) ( x[n>>6] |= (1<< ( (n>>1) & 31) )  ) // sets the bit corresponding to n to 1 - meaning its composite 
#define mod 1000000007
typedef long long int ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long int ull;	
using namespace std;
typedef vector<int> VI;
typedef set<int> SI;
typedef map<int,int> MII;
typedef pair<int,int> PII;
struct debugger
{
template<typename T> debugger& operator , (const T& v)
{	
	cerr<<v<<" ";	
	return *this;	
}
} dbg;
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);int ct=0;
		for (int i = 0; i<a; i++) 
		{
			for (int j = 0; j<b; j++) 
			{
				if((i&j)<k) 
				{
					ct++;
				}
				
			}
		}
		printf("Case #%d: %d\n",t,ct);
	}
	return 0;
}

