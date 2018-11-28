#include <bits/stdc++.h>
using namespace std;

const int MAXN=1007; 
const int MOD=1000000007; 
const int INF=2147483647;
const double EPS=1e-8;

int i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
string s;
int a[MAXN]; 
bool imp;

int main()
{
#ifdef Smile
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": ";
			cin>>s>>k;
			n=s.length();
			cnt=0;
			imp=false;
			for (int i = 0; i < n; ++i)
			{
				if (s[i]=='-')
				{
					cnt++;
					for (int j = 0; j < k; ++j)
					{
						if (i+j>=n)
						{
							imp=true;
							break;
						}
						s[i+j]=(s[i+j]=='-')?'+':'-';
					}
				}
			}
			if (imp)
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
			else
			{
				cout<<cnt<<endl;
			}
		}	
	}
	return 0;
}