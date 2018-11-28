/* ***********************************************
Author        :kuangbin
Created Time  :2015/5/30 22:24:26
File Name     :F:\ACM\2015ACM\±»»¸¡∑œ∞\2015GCJ_R2\B.cpp
************************************************ */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <iomanip>
using namespace std;
const long double eps = 1e-13;
pair<double,double>p[110];
int n;
double V,X;
double check(long double tt){
	long double nv = 0;
	long double nl = 0;
	for(int i = 0;i < n;i++){
		long double tmp = p[i].second*tt;
		tmp = min(tmp,V-nv);
		nl += tmp*p[i].first;
		nv += tmp;
	}
	long double nr = 0;
	nv = 0;
	for(int i = n-1;i >= 0;i--){
		long double tmp = p[i].second*tt;
		tmp = min(tmp,V-nv);
		nr += tmp*p[i].first;
		nv += tmp;
	}
	if(nl > V*X+eps || nr < V*X - eps)return false;
	return true;
}

int main()
{
    freopen("B-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	int iCase = 0;
	scanf("%d",&T);
	while(T--){
		iCase++;
		scanf("%d%lf%lf",&n,&V,&X);
		for(int i = 0;i < n;i++)
			scanf("%lf%lf",&p[i].second,&p[i].first);
		sort(p,p+n);
		if(X < p[0].first || X > p[n-1].first){
			printf("Case #%d: IMPOSSIBLE\n",iCase);
			continue;
		}
		long double l = 0;
		long double r = 1e20;
		long double ans = r;
		while(r-l > eps){
			long double mid = (l+r)/2;
			if(check(mid)){
				ans = mid;
				r = mid-eps;
			}
			else l = mid+eps;
		}
		printf("Case #%d: ",iCase);
		cout << setprecision(15) << ans << endl;
		
	}
    return 0;
}
