#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <iomanip>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;
//--------------------
double a,b,c,d,f,x,ans;
ll t,i,j,t1;

//--------------------
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf ("%d", &t);
	for(t1 = 1; t1 <= t; ++t1){
		ans = d = 0;
		printf ("Case #%d: ", t1);
		scanf ("%lf %lf %lf", &c, &f, &x);

		ans = x/2.;
		a = 2;

		while(true){
			d += c / a;
			a += f;
			if (d + x/a < ans) ans = d + x/a;
			else break;
		}
		printf("%.7lf\n", ans);
		

	}

	return 0;
}