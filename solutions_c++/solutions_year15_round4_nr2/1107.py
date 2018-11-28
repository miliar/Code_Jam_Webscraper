#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <list>
using namespace std;
typedef long long LL;
#define FOR(k,a,b) for(int k((int)a); k < ((int)b); ++k)
#define FORD(k,a,b) for(int k((int)b-1); k >= ((int)a); --k)
#define REP(k,a) for(int k=0; k < ((int)a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
#define EPS 1e-9
#define INF 1e10

double solver(double c1, double c2, double v1, double v2, double X, double V)
{
	double tmp = 1-(X-c1)/(c2-c1);
	double vv1 = V*tmp;
	double t1 = vv1/v1;
	double vv2 = V*(1-tmp);
	double t2 = vv2/v2;
// 
// 	double tmp = (c2/c1-v2/v1);
// 	if(ABS(tmp)<EPS) return INF;
// 	double t2 = (X/c1-V/v1)/(c2/c1-v2/v1);
// 	double t1 = X/c1-t2*c2/c1;
// 	if(t2<EPS || t1<EPS) return INF;
	return max(t1,t2);
}

int main( int argc, char* argv[] ) {
#ifdef HOME
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","wb",stdout);
#endif
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		int N;
		double X,V;
		cin >> N >> V >> X;
		vector<double> C(N),R(N);
		REP(i,N)
			cin >> R[i] >> C[i];
		double Rl = 0, Cl = 0, Rh=0, Ch = 0, Req = 0;
		REP(i,N)
		{
			if(ABS(C[i]-X)<EPS)
			{
				Req += R[i];
			}
			else if(C[i]<X)
			{
				Rl += R[i];
			}
			else if(C[i]>X)
			{
				Rh += R[i];
			}
		}
		REP(i,N)
		{
			if(ABS(C[i]-X)<EPS)
			{
				continue;
			}
			else if(C[i]<X)
			{
				Cl += (R[i]/Rl)*C[i];
			}
			else if(C[i]>X)
			{
				Ch += (R[i]/Rh)*C[i];
			}
		}
		if(Req < EPS)
		{
			if(Rl <EPS || Rh < EPS)
			{
				//cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
				printf("Case #%d: IMPOSSIBLE\n",tc);
			}
			else
			{
				double ans = solver(Cl,Ch,Rl,Rh,X,V);
				//cout << "Case #" << tc << ": " << ans << endl;
				printf("Case #%d: %.9f\n",tc,ans);
			}
		}
		else
		{
			if(Rl <EPS || Rh < EPS)
			{
				//cout << "Case #" << tc <<": " << V/Req << endl;
				printf("Case #%d: %.9f\n",tc,V/Req);
			}
			else
			{
				double lo = 0, hi = 1000000;
				while((hi-lo)>EPS)
				{
					double mid = (lo+hi)/2;
					double Veq = mid*Req;
					if(Veq>V)
					{
						hi = mid;
						continue;
					}
					double ans = solver(Cl,Ch,Rl,Rh,X,V-Veq);
					if(ABS(mid-ans)<EPS)
					{
						//cout << "Case #" << tc << ": " << ans << endl;
						printf("Case #%d: %.9f\n",tc,ans);
					}
					else
					{
						if(Veq>ans)
						{
							hi=mid;
						}
						else
						{
							lo=mid;
						}
					}
				}
			}
		}
	}
	return 0;
}
