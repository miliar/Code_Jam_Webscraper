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

const int maxn = 20000;
double a[maxn];
double b[maxn];
int n;
int main()
{
	int i,j,k,end;
    // freopen("in","r",stdin);
    int t,cas=0;
    cin>>t;
    while(t--)
    {
    	cin>>n;
    	for(i=0; i<n; i++)
    		cin>>a[i];
    	for(i=0; i<n; i++)
    		cin>>b[i];
    	sort(a,a+n);
    	sort(b,b+n);
    	// reverse(b,b+n);
    	// for(i=0; i<n; i++)
    	// {
    	// 	printf("%lf ",a[i]);
    	// }
    	// cout<<endl;
    	// for(i=0; i<n; i++)
    	// {
    	// 	printf("%lf ",b[i]);
    	// }
    	// cout<<endl;
    	int numa =0;
    	j =0 , end = n-1;
		for(i=0; i<n; i++)
		{
			if(a[i]>b[j]){
				numa++;
				j++;
			}
			else{
				end--;
			}
    	}
    	int numb = 0 ;
    	j=0,end =n-1 ;


    	reverse(a,a+n);
    	
    	for(i=0; i<n; i++)
    	{
    		if(a[i]>b[end])
    		{
    			j++;
    			numb++;
    		}
    		else
    		{
    			end--;
    		}
    	}
    	printf("Case #%d: %d %d\n",++cas, numa,numb);
    }
}