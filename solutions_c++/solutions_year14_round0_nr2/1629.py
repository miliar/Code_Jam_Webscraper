#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;
#define eps 1e-12
double need[100010];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int T = 0, Cas = 0, n = 0;
	scanf("%d",&T); 
    while(T--)
    {
      	double C, F, X;
      	scanf("%lf%lf%lf", &C, &F, &X);
      	int top = int(X) + 5;
      	double ans = X / 2.0;
      	need[0] = 0;
      	double speed = 2.0, now = 0.0;
      	for(int i = 1; i <= top; i++) {
      		now += (C / speed);
      		speed += F;
      		need[i] = now;
      	}
      	for(int i = 0; i <= top; i++) {
      		double l = need[i], r = 10000000000000.0, mid;
      		//X = (mid - need[i]) * (2.0 + i * F);
      		r = X / (2.0 + i * F) + need[i];
      		//ans = min(ans, r);
      		ans = min(ans, r);
      	}
      	printf("Case #%d: %.7f\n", ++Cas, ans);
    }
      	
}