#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <math.h>
#include <vector>
#include <ctime>
#include <cctype>
#include <stack>
#include <set>
#include <bitset>
#include <functional>
#include <numeric>
#include <stdexcept>
#include <utility> 
using namespace std;
#define ll long long 
#define m0(a) memset(a, 0, sizeof(a))
#define m1(a) memset(a, -1, sizeof(a))
#define C1(x)  cout<<x<<endl;
#define C2(x,y)  cout<<x<<" "<<y<<endl;
#define C3(x,y,z)  cout<<x<<" "<<y<<" "<<z<<endl;
struct stu
{
	int x,y,z;
	bool operator < (const stu &b) const
	{
		return x<b.x;	
	}
};
const int inf = 0x3f3f3f3f; 
const double eps = 1e-15;
const double pi = acos((double)-1) ;
const int maxn = 100100;
const ll M = 1e9+7;
ll i,j,k,l,m,n,x,y,z,ans,num;
string s;
int v[maxn]={0};
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int main () 
{
	#ifdef ONLINE_JUDGE
	
	#else
	
	    freopen("B-large.in","r",stdin);
	    freopen("B-large.out","w",stdout);
	
	#endif
	int cas;
	scanf("%d",&cas);
	for (int casi=1;casi<=cas;casi++)
	{
		cin>>s;
		printf("Case #%d: ",casi);
		num=0;
		if (s[0]=='-') num++;
		for (int i=1;i<s.length();i++)
		{
			if (s[i-1]=='+' && s[i]=='-') num++;
		}
		num=num*2-(s[0]=='-'?1:0);
		cout<<num<<endl;
	}
	return 0;
}






