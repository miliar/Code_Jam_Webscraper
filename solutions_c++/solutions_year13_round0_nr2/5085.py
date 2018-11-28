#include <iostream>
#include <string>
#include <math.h>

#include <stdlib.h>
#include <stdio.h>

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(v,p,k) for(int v=p;v<=k;v++)

using namespace std;


int main()
{
	int ground[100][100];
	bool good[100][100];
	int t,n,m,n_good;
	cin>>t;
	FOR(c,1,t)
	{
		cin>>n;
		cin>>m;
		n_good=0;
		REP(i,n)
		{
			REP(j,m)
			{
				cin>>ground[i][j];
				good[i][j]=false;
			}
		}
		REP(i,n)
		{
			int maxi=0;
			REP(j,m)
			{
				maxi=max(maxi,ground[i][j]);
			}
			REP(j,m)
			{
				if(ground[i][j]==maxi && !good[i][j])
				{
					good[i][j]=true;
					n_good++;
				}
			}
		}
		REP(j,m)
		{
			int maxi=0;
			REP(i,n)
			{
				maxi=max(maxi,ground[i][j]);
			}
			REP(i,n)
			{
				if(ground[i][j]==maxi && !good[i][j])
				{
					good[i][j]=true;
					n_good++;
				}
			}
		}
		string res=(n_good==n*m?"YES":"NO");
		printf("Case #%d: %s\n",c,res.c_str());
	}
}
