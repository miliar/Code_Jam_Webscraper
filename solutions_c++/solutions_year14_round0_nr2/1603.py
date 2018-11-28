#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<assert.h>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
const int inf=0x7fffffff;
const double pi=acos(-1.0);
#define eps (1e-15)
#define L(x) ((x)<<1)
#define R(x) ((x)<<1|1)
#define see(x)(cerr<<"[line:"<<__LINE__<<" "<<#x<<" "<<x<<endl)
#define se(x) cerr<<x<<" "
template<class T>T& ls(T& a,T b)
{ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b)
{ if(b>a) a=b; return a;}
inline int to_i(const string& s)
{int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n)
{char buf[32];sprintf(buf,"%d",n);return string(buf);}


int main()
{
    // freopen("in","r",stdin);
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
    	double c,f,x;
    	cin>>c>>f>>x;
    	double ans = x/2;
    	double speed = 2;
    	if(c<x)
    	{
    		double house=0;
    		double ansnow =0;
    		double anshouse =0;
	    	while(1)
	    	{
	    		ansnow+=(c/speed);
	    		speed+=f;
	    		if(ansnow+x/speed<ans)
	    			ans = ansnow+x/speed;
	    		else
	    			break;

	    	}
    	}
    	printf("Case #%d: %.7lf\n",++cas,ans);
    }
}