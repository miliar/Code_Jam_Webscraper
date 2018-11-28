#include <iostream>
#include <cstdio>
using namespace std;

#define forn(i,n) for(int i=0; i<(int)(n); i++)

int cards[32];

int main(){
	int t; cin>>t;
	forn(tc,t){
		double best_time = 1000000000;
		double c, f, x; cin>>c>>f>>x;
		double cookies = 2;
		double accum_time = 0;
		forn(cf,1+x){
			double time = x/cookies;
			best_time = min(best_time, accum_time+time);
			accum_time += c/cookies;
			cookies += f;
		}
		printf("Case #%d: %.7lf\n",tc+1,best_time);
	}
}
