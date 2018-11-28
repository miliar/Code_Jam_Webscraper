#include <bits/stdc++.h>
#include <cassert>
#include <limits>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define FOR(i,a,b)   for(int(i)=int(a);(i)<int(b);(i)++)
#define FOREQ(i,a,b) for(int(i)=int(a);(i)<=int(b);(i)++)
#define RFOR(i,a,b)  for(int(i)=(a),_b(b);(i)>=_b;--(i))
#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define FILL(arr,val) memset((arr),(val),sizeof(arr))
#define CLR(a)        memset((a),0,sizeof(a))
#define CPY(dest,src) memcpy((dest),(src),sizeof(dest))

#define ALL(a)       (a).begin(),(a).end()
#define SZ(a)        ((int)(a).size())
#define UNIQ(a)      sort(ALL(a)); (a).erase(unique(ALL(a)),(a).end())
#define IDX(arr,ind) (lower_bound(ALL(arr),ind)-arr.begin())

#define fst first
#define snd second
#define pb  push_back
#define mp  make_pair

static int T;

int main()
{
	//double eps = std::numeric_limits<double>::epsilon();
	scanf("%d", &T);
	FOREQ(t,1,T)
	{
		double C = 0.0f, F = 0.0f, X = 0.0f;
		scanf("%lf%lf%lf", &C,&F,&X);
/*
		if(t != 98)
		{
			continue;
		}
*/
		double cookies = 0.0f, ctime = 0.0f, crate = 2.0f;
		double ctime_left1 = 0.0f, ctime_left2 = 0.0f;
		while(cookies < X)
		{
			if(X-cookies < C)
			{
//				printf("%lf: goal %lf < C(%lf) away; current=%lf\n", ctime,X,C,cookies);
				ctime += (X-cookies)/crate;
				break;
			}
			else
			{
				// there exists at least one upgrade point
				// can't do anything before upgrade point -> ie. advance time
				if(cookies < C)
				{
//					printf("%lf: wait %lf for upgrade\n", ctime, (C-cookies)/crate);
					ctime += (C-cookies)/crate;
					cookies += C;
				}
				// at upgrade point
				ctime_left1 = (X-cookies)/crate;
				ctime_left2 = (X-cookies+C)/(crate+F);
				if(ctime_left1 < ctime_left2)
				{
					// better not to upgrade
					ctime += ctime_left1;
					break;
				}
				else
				{
					// better (and able) to upgrade
//					printf("%lf: upgrade %lf->%lf\n", ctime,crate,crate+F);
					cookies -= C;
					crate += F;
				}
			}
		}

		printf("Case #%d: %.7lf\n", t,ctime);
	}
	return 0;
}
