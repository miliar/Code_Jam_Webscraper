

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

double c,f,x;//e=0.0000001;
double getmintime(double inc)
{
	double temp1=(x*1.0)/(inc*1.0);
	double temp2=((c*1.0)/(inc*1.0)) + ((x*1.0)/((inc+f)*1.0));
	if(temp1-temp2<0)
		return temp1;
	else
		return ((c*1.0/inc*1.0)+ getmintime(inc+f));
}
int main()
{
	LL t;
	cin >> t;
	REP(i,t)
	{
		cin >> c >> f >> x ;
		double ans =getmintime(2);
		printf("Case #%lld: %.7lf\n",i+1,ans);
	}
	return 0;
}
