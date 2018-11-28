#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
const long long int INF=1000*1000*1000;
const int MAXN=1000*1000;
using namespace std;
long long int t,i,j,a,b,ans[1000];
string cur;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>a>>b;
		for(j=a;j<=b;j++)
		{
			cur="";
			int l=j,r;
			if(double(sqrt(l))!=int(sqrt(l)))continue;
			while(l)
			{
				cur+=char(l%10+'0');
				l/=10;
			}
			r=cur.size()-1;
			for(l=0;l<cur.size()/2;l++)
			{
				if(cur[l]!=cur[r])
				{
					goto qwe;
				}
				r--;
			}
			l=sqrt(j);
			cur="";
			while(l)
			{
				cur+=char(l%10+'0');
				l/=10;
			}
			r=cur.size()-1;
			for(l=0;l<cur.size()/2;l++)
			{
				if(cur[l]!=cur[r])
				{
					goto qwe;
				}
				r--;
			}
			ans[i+1]++;
			qwe:;
		}						
	}		
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": "<<ans[i]<<endl;
	}
	return 0;
}

	