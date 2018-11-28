#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cctype>
#include <stack>
#include <ctime>
#include <strstream>
#include <unordered_map>
#include <unordered_set>
typedef long long ll;
#define EPS 1e-8
using namespace std;
typedef pair<int,int> pii;
template<class T> inline T euclide(T a,T b,T &x,T &y)//NOTES:a*x+b*y=1;
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}

bool solve(const vector<int>&p, int ti)
{
	int i,et,nv;
	for(et=1;et<=ti;et++)
	{
		nv=0;
		for(i=0;i<p.size();i++)
		{
			nv+=(p[i]-1)/et;
			if(et+nv>ti)break;
		}
		if(et+nv<=ti)return 1;
	}
	return 0;
}
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j;
	scanf("%d",&cas);
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		int d,t;
		cin>>d;
		vector<int> p(d,0);
		int hi=0,lo=1,mid;
		for(i=0;i<d;i++)
		{
			cin>>p[i];
			if(p[i]>hi)hi=p[i];
		}
		while(hi>=lo)
		{
			mid=(hi+lo)/2;
			if(solve(p,mid))hi=mid-1;
			else lo=mid+1;
		}
		cout<<lo<<endl;
		fflush(stdout);
	}
	return 0;
}