
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

int a[4];
int b[4];
int m1[4][4];
int m2[4][4];
int main()
{
	int T;
	scanf("%d",&T);
	for (int t = 1; t<=T; t++) 
	{
		int r1,r2;
		scanf("%d",&r1);
		for(int i=0;i < 4;i++)
		{
			for(int j=0;j < 4;j++)
			{
				scanf("%d",&m1[i][j]);
			}
			if(i+1==r1) 
			{
				for (int k = 0; k<4; k++) 
				{
					a[k]=m1[i][k];
				}
			}
		}
		scanf("%d",&r2);
		for(int i=0;i < 4;i++)
		{
			for(int j=0;j < 4;j++)
			{
				scanf("%d",&m2[i][j]);
			}
			if(i+1==r2) 
			{
				for (int k = 0; k<4; k++) 
				{
					b[k]=m2[i][k];
				}
			}
		}
		int matches=0;int ans;
		for(int i=0;i < 4;i++)
		{
			for(int j=0;j < 4;j++)
			{
				if(a[i]==b[j]) 
				{
					matches++;ans=a[i];
				}	
			}
		}
		printf("Case #%d: ",t);
		if(matches==1) 
		{
			printf("%d\n",ans);
		}
		else if(matches==0) 
		{
			printf("Volunteer cheated!\n");
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
