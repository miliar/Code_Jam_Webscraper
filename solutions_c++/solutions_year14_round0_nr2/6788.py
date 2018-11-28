#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int tc, tcc;
	cin>>tc;
	for (tcc=1; tcc<=tc; tcc++){
		double r = 2;
		double c, f, x;
		cin>>c>>f>>x;

		double ans=0;

		while (1){
			//cout<<ans<<endl;
			double y = c/r;
			if (c<x && x/(r+f) < (x-c)/r){
				ans += y;
				r = r+f;
			} else {
				ans += x/r;
				break;
			}
		}

		printf("Case #%d: %lf\n", tcc, ans);
	}
	return 0;
}