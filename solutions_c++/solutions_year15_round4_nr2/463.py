#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define inf (9999999999999999LL)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define eps 1e-15
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) //fprintf(stderr,args)
#endif

#define pb push_back	
#define mod 1000000007
#define maxn 100100

using namespace std;

long double flow[maxn];
long double temp[maxn];

long double vol[maxn];


main(){


		int te;
		scanf("%d",&te);
		
		for(int t=1;t<=te;t++){

			int n;
			scanf("%d",&n);

			long double ma = 0, mi = 100;

			vector<pair<long double,long double> > vv;
			
			long double vf, tf;
			cin >> vf >> tf;

			for(int i=0;i<n;i++){
				cin >> flow[i] >> temp[i];
				vv.pb(pair<long double,long double> (temp[i],flow[i]));
				ma = max(ma,temp[i]);
				mi = min(mi,temp[i]);
			}

			sort(vv.begin(),vv.end());
			for(int i=0;i<n;i++)
				flow[i] = vv[i].second,
				temp[i] = vv[i].first;

			printf("Case #%d: ",t);
			if(tf > ma + eps || tf < mi - eps){
				printf("IMPOSSIBLE\n");
				continue;
			}

			long double low = 0, up = 1000000;

			for(int u=0;u<1000;u++){
			//while(abs(up-low) > eps){

				//low = up = 0.5;
				long double mid = (low+up)/2;

				long double sum = 0;

				for(int i=0;i<n;i++)
					vol[i] = mid * flow[i], sum += vol[i];

				if(sum < vf){
					low = mid;
					continue;
				}

				long double cold=0, hot=0;
				
				long double v = 0;

				for(int i=0;i<n;i++){
					if(v + vol[i] < vf + eps){
						v += vol[i];
						cold += vol[i] * temp[i];
					}
					else {
						cold += (vf-v) * temp[i];
						v += vf - v;
						
					}
				}

				//cout << v << endl;

				v = 0;

				for(int i=n-1;i>=0;i--){
					if(v + vol[i] < vf + eps){
						v += vol[i];
						hot += vol[i] * temp[i];
					}
					else {
						hot += (vf-v) * temp[i];
						v += vf - v;	
					}
				}

				//cout << v << endl;
				cold /= vf;
				hot /= vf;

				//debug("mid ");
				//scout << mid << " " << cold << " " << hot << endl;

				if(tf > hot + eps || tf < cold - eps)
					low = mid;
				else
					up = mid;

			}

			printf("%.8lf\n",(double)low);

		}

}
