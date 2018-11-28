#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <bitset>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
 
using namespace std;

#define MAX 1000
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define mp make_pair
#define F first
#define S second
#define INF 0x3f3f3f3f
#define INT_MAX 2147483647
#define pb push_back
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define itr(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> lli;
typedef pair<int,pii> i3;
 
 int main()
{
	read; write;
    int t,n,i,m=0;
    gi(t);
    while(t--)
    {
    	m++;
    	gi(n);
    	int a[n+1],sum=0,count=0;
    	for(i=1;i<=n;i++)
    	{
    		cin>>a[i];
    		sum=sum+a[i];
    	}
    	cout << "Case #" << m << ": ";
    	if(sum%2!=0)
    	{
    		int max=0,k=0;
    		for(i=1;i<=n;i++)
    		{
    			if(a[i]>max)
    			{
    				max=a[i];
    				k=i;
				}
			}
			char ch =k+64;
			a[k]--;
			count++;
			cout<<ch<<" ";
		}
		while(count<sum)
		{
			int max=0,max1=0,k=0,l=0;
			for(i=1;i<=n;i++)
			{
				if(a[i]>max)
				{
					max1=max;
					max=a[i];
					l=k;
					k=i;
				}
				else if(a[i]>max1)
				{
					max1=a[i];
					l=i;
				}
			}
			count=count+2;
			char c=k+64,c1=l+64;
			cout<<c<<c1<<" ";
			a[k]--;
			a[l]--;
		}
		cout<<endl;
	}
    return 0;
}