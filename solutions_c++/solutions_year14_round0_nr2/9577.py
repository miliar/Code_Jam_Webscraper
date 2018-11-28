//Solution by Daniyar Maminov                                                                                                                                                                     
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ub upper_bound
#define lb lower_bound
#define inf 1000*1000*1000
using namespace std;

int ts, n, m, i, j;

double t, cur, d, c, f, x, y, e, k;

const double eps=1e-7;

int main()
{
	freopen ("B-small-attempt0.in","r",stdin);
	freopen ("output.txt","w",stdout);
	cin>>ts;
	for (int cs=1; cs<=ts; cs++)
	{
		cout<<"Case #"<<cs<<": ";
		scanf("%lf%lf%lf", &c, &f, &x);
		cur = k = 0;
		while (1)
		{
			if (x/(k*f+2)-(c/(k*f+2)+x/((k+1)*f+2))<eps)
			{
				cur+=(x/(k*f+2));
				break;
			}
			cur+=c/(k*f+2);
//			cout<<cur<<endl;
			k++;
		}
		printf("%.7f\n", cur);
	}
		
		
					
		
	return 0;
}
