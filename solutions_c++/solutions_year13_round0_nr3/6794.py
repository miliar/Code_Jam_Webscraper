#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>

using namespace std;

#define si(n) scanf("%d",&n);
#define ss(s) scanf("%s",s);
#define pi(n) printf("%d ",n);
#define ps(s) printf("%s",s);
#define loop(i,n) for(i=0;i<n;i++)
#define Loop(i,n) for(i=1;i<=n;i++)
typedef long long int lld;

#define MEM(a,v) memset(a, v, sizeof (a))
//a for address, v for value 
#define FORN(i,n) for(int i=0;i<(int)n;i++)
#define max(x,y) ((x) > (y) ? (x) : (y))
#define min(x,y) ((x) < (y) ? (x) : (y))
bool ascending(int i,int j){return(i<j);}
bool descending(int i,int j){return(i>j);}

#define INF 2100000000
#define N 10000

int main()
{
	int i,j,k,x;
	int n,m,d,t,a,b,c=1;
	cin>>t;
	while(t--)
	{
		int s=0;
		cin>>a>>b;
		for(i=a;i<=b;++i)
		{
			int x=(int)sqrt(i);
			if(i!=x*x)
				continue;
			int m=i;
			int sum=0;
			while(m)
			{
				sum=sum*10+m%10;
				m/=10;
			}
			int n=x;
			int sum1=0;
			while(n)
			{
				sum1=sum1*10+n%10;
				n/=10;
			}
			
			if(sum==i&&sum1==x)
				s++;
		}
		cout<< "Case #"<<c<<": "<<s<<endl;
		c++;
	}
	return 0;
}