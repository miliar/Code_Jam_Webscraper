#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < ((int) n); i++)
#define EPS 0.0000000000000001

double r[128], c[128];

int sg(double f)
{
	if(f>EPS) return 1;
	if(f<-EPS) return -1;
	return 0;
}

int main()
{	
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	
	forn(tc, T)
	{
		int N;
		cin >> N;
		
		double v, x;
		cin >> v >> x;
		
		forn(i, N) cin >> r[i] >> c[i];
		
		if(N==1)
		{
			double ans=-1;
			
			if(fabs(x-c[0])<EPS) ans = v/r[0];
			cout << "Case #" << tc+1 << ": ";
			if(ans < 0) cout << "IMPOSSIBLE" << endl; else printf("%.9f\n", ans);
	
		}
		else
		{
			double ans=-1;
			
			
			
			if(sg(x-c[0])*sg(x-c[1])<=0)
			{
				if(fabs(c[0]-c[1])<EPS)
				{
					ans = v/(r[0]+r[1]);
				}
				else
				{
					double v0 = v*(x-c[1])/(c[0]-c[1]);
					double v1 = v-v0;
					
					ans = max(v0/r[0], v1/r[1]);
				}
			}
			cout << "Case #" << tc+1 << ": ";
			if(ans < 0) cout << "IMPOSSIBLE" << endl; else printf("%.9f\n", ans);
	
		}
		
	}
	
}
