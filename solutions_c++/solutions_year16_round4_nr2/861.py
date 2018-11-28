#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <list>
#include <cassert>



using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-small-attempt0(8)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


double p[222];
double dp[222][222][222];
int n,k;
double go(int cur, int yes, int tot)
{	
	if (tot == k) return yes*2==k;
	if (yes*2>k) return 0;
	if (cur>=n) return 0;

	if (dp[cur][yes][tot]>-0.1) return dp[cur][yes][tot];

	double res = 0;

	res = go(cur+1,yes,tot);

	res = max(res,
		go(cur+1,yes+1,tot+1)*p[cur]+
		go(cur+1,yes,tot+1)*(1-p[cur])
		);

	return dp[cur][yes][tot] = res;
}

int ocnt(int n)
{
	int res = 0;
	while (n)
	{
		n=n&(n-1);
		res++;
	}
	return res;
}

double pr[222];

int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst; cas++)
	{
	
		for (int i=0;i<222;i++)
			for (int j=0;j<222;j++)
				for (int k=0;k<222;k++)
					dp[i][j][k]=-1;

		int N,K;
		scanf("%d%d",&N,&K);

		for (int i=0;i<N;i++)
			scanf("%lf",&pr[i]);
		double res = 0;

		for (int i=0;i<1<<N;i++)
			if (ocnt(i)==K)
			{
				int ps = 0;
				for (int j=0;j<N;j++)
					if (((1<<j)&i)!=0)
					{
						p[ps] = pr[j];
						ps++;					
					}


					for (int i=0;i<=N;i++)
					for (int j=0;j<=N;j++)
					for (int k=0;k<=N;k++)
					dp[i][j][k]=-1;

					n=K;
					k=K;
					res = max(res,go(0,0,0));
			
			}

		

		
	
		printf("Case #%d: %.9lf\n",cas,res);
	}

	


	return 0;
}
