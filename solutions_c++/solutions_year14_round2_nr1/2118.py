

/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Sagar Balwani IIIT-H
 _._._._._._._._._._._._._._._._._._._._._.*/

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include <bitset>
#include <string>
#include <queue>

using namespace std;

/* General Declarations */
#define SZ(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors

#define INF	        1000000007
#define LL	        long long int
#define INFL	        (LL)1000000007
#define SI(n)		scanf("%lld",&n)
#define SC(c)		scanf("%c",&c)
#define SS(s)		scanf("%s",s)
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP	    	make_pair
#define PB	    	push_back
#define	F	       	first
#define S		second
#define SCAN(v,n)	vector<int> v;REP(i,n){ int j;SI(j);v.PB(j);}
#define PRINT(v,n)	REP(i,n){printf("%lld ",v[i]);}printf("\n");

/* Container's */

#define	VI	       	vector<LL>
#define PLL         	pair<LL,LL>  /* A Single Pair  */
#define VP	    	vector<PLL> /* Vector of Pairs */
#define VS	    	vector<string>
#define VVI		vector<VI>
#define VVS	    	vector<VS>
//Note a & b should both fit in LL
template<class T>inline T GCD(T a,T b){return b?GCD(b,a%b):a;}
template<class T> inline T LCM(T a,T b){if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/GCD(a,b));}
template<class T>inline T POW1(T a,T b,T m){long long x=1,y=a;while(b > 0){if(b%2 == 1){x=(x*y);if(x>m) x%=m;}y = (y*y);if(y>m) y%=m;b /= 2;}return x;}
template<class T>inline T INV(T n,T m){return POW1(n,m-2,m);}
template<class T>inline T SUB(T a,T b,T m){return (a%m-b%m+m)%m;}
template<class T>inline T ADD(T a,T b,T m){return (a%m+b%m)%m;}
template<class T>inline T MUL(T a,T b,T m){return (a%m*b%m)%m;}
template<class T>inline T DIV(T a,T b,T m){return (a%m*(INV(b,m))%m)%m;}
LL foo(VI v)
{
	LL avg=0,a=0,b=0;
	REP(i,SZ(v))
	{
		avg+=v[i];
	}
	avg/=SZ(v);
	REP(i,SZ(v))
	{
		a+=abs(v[i]-avg);
	}
	REP(i,SZ(v))
	{
		b+=abs(v[i]-(avg+1));

	}
	return min(a,b);
}
int main()
{
	LL t,tc=1;
	cin >> t;
	while(t--)
	{
		LL n,flag=0,ans=0,ct=0;
		cin >> n;
		vector<string> s(105);
		vector<char> prev,curr;
		vector<LL> v[105];
		REP(i,n)
		{
			cin >> s[i];
		}
		REP(i,SZ(s[0]))
		{
			if(i==0)
			{
				prev.PB(s[0][i]);
				ct++;
			}
			else
			{
				if(s[0][i-1]==s[0][i])
				{
					ct++;
				}
				else
				{
					v[0].PB(ct);
					ct=1;
					prev.PB(s[0][i]);
				}
			}
		}
		v[0].PB(ct);
		FOR(j,1,n)
		{
			ct=0;
			REP(i,SZ(s[j]))
			{
				if(i==0)
				{
					curr.PB(s[j][i]);
				ct++;
				}
				else
				{
					if(s[j][i-1]==s[j][i])
					{
				ct++;
					}
					else
					{
					v[j].PB(ct);
					ct=1;
						curr.PB(s[j][i]);
					}
				}
			}
			v[j].PB(ct);
			if(curr!=prev)
			{
				flag=1;
				break;
			}
			else
			{
				prev=curr;
				curr.clear();
			}
		}
		REP(i,v[0].size())
		{
			vector<LL> temp;
			REP(j,n)
			{
				temp.PB(v[j][i]);
			}
			ans+=foo(temp);
		}
		if(flag==1)
		{
			cout << "Case #" << tc << ": Fegla Won\n";
		}
		else
		{
			cout << "Case #" << tc << ": " << ans << endl;
		}
		tc++;
	}
	return 0;
}
