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


int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j;
	scanf("%d",&cas);
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		int sm;
		string s;
		cin>>sm>>s;
		int sum=0,ret=0;
		for(i=0;i<=sm;i++)
		{
			if(i>sum)
			{
				ret+=i-sum;
				sum=i;
			}
			sum+=s[i]-'0';
		}
		printf("%d\n",ret);
		fflush(stdout);
	}
	return 0;
}