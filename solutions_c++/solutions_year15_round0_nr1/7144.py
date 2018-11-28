/*SHUBHAM RANJAN*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#include <complex>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FF(i,a,n) for(i=(a);i<(n);++i)
#define REP(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define MAX(a,b) ((a)>(b)?(a):(b))
ill ABS(ill a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    freopen("input.in","r",stdin);
#endif
}
void output()
{
	freopen ("output.txt","w",stdout);
}
/* Input opener ends */
int main()
{
	input();
	output();
	int n,a;
	S(n);
	int n1=n;
	
	while(n--)
	{
		string st;
		S(a);
		cin>>st;
		int count=0,s,ans=0;
		F(i,0,a+1)
		{
			
			s=st[i]-'0';
			if(s>=1)
			{
			  if(count<i)
			  {
			  ans+=(i-count);
			  count+=(i-count);
			  }
			}
			//cout<<"#"<<count;
			count+=s;
		}
		printf("Case #%d: %d\n",n1-n,ans);
	}
	fclose(stdout);
}
