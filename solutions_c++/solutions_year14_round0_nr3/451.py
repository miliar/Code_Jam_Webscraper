#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <cmath>
#include <stdlib.h>
#include <stack>
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
ll MOD=1000000007;
ll inf=10000000000;
using namespace std;


vector< vector<char> > L;
vector<char> LL;
int n,m;
string Ans="";


bool Solve(int M)
{
	int i,j,dx,dy,k;
	if(M<0)
	{
		return false;
	}
	if(M==0)
	{
		bool e=true;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(L[i][j]=='.')
				{
					if(e)
					{
						bool valid=true;
						for(dx=-1;dx<2;dx++)
						{
							for(dy=-1;dy<2;dy++)
							{
								if(i+dx>=0 && i+dx<n && j+dy>=0 && j+dy<m && L[i+dx][j+dy]=='*')
								{
									valid=false;
									break;
								}
							}
						}
						if(valid)
						{
							e=false;Ans+="c";
						}
						else{Ans+=".";}
					}
					else
					{
						Ans+=".";
					}
				}
				else
				{
					Ans+="*";
				}
			}
			Ans+="\n";
		}
		return true;
	}
	vector< pii > V;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(L[i][j]=='*'){continue;}
			V.clear();
			for(dx=-1;dx<2;dx++)
			{
				for(dy=-1;dy<2;dy++)
				{
					if(i+dx>=0 && i+dx<n && j+dy>=0 && j+dy<m && L[i+dx][j+dy]=='*')
					{
						V.pb(mp(i+dx,j+dy));
					}
				}
			}
			if(V.size()==0 || V.size()>M){continue;}
			for(k=0;k<V.size();k++)
			{
				L[V[k].first][V[k].second]='.';
			}
			if(Solve(M-V.size()))
			{
				return true;
			}
			for(k=0;k<V.size();k++)
			{
				L[V[k].first][V[k].second]='*';
			}
		}
	}
	return false;
}

string STR(int x)
{
	string s="";
	char c;
	while(x!=0)
	{
		c='0'+(x%10);
		s=c+s;
		x/=10;
	}
	return s;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("/home/ahmed_ossama/C-large.in","r",stdin);
	freopen("/home/ahmed_ossama/OutputC.out","w",stdout);
	int T,t,M,F,i,j;
	cin>>T;
	
	for(t=0;t<T;t++)
	{
		//cout<<t+1<<endl;
		Ans+="Case #"+STR(t+1)+":\n";
		cin>>n>>m>>M;
		F=n*m-M;
		
		if(F==1)
		{
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(i==0 && j==0)
					{
						Ans+="c";
					}
					else
					{
						Ans+="*";
					}
				}
				Ans+="\n";
			}
			continue;
		}
		if(M==0)
		{
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(i==0 && j==0)
					{
						Ans+="c";
					}
					else
					{
						Ans+=".";
					}
				}
				Ans+="\n";
			}
			continue;
		}
		if(n==2 && m==2)
		{
			Ans+="Impossible\n";
			continue;
		}
		if((n==2 || m==2) && F%2==1)
		{
			Ans+="Impossible\n";continue;
		}
		L.clear();
		LL.clear();
		for(j=0;j<m;j++)
		{
			LL.pb('*');
		}
		for(i=0;i<n;i++)
		{
			L.pb(LL);
		}
		L[0][0]='.';
		if(Solve(F-1))
		{
			continue;
		}
		Ans+="Impossible\n";
	}
	cout<<Ans;
	
	return 0;
}
