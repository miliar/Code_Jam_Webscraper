#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("b_input.txt", "r", stdin);
	freopen("b_output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		
		double rate = 2, rtime = 0;
		while(true){
			double req = rtime + x / rate;
			double nreq = rtime + ( x / (rate + f) ) + ( c / rate );
			if( req < nreq ){
				rtime = req;
				break;
			}
			rtime += c / rate;
			rate += f;
		}
		
		printf("Case #%d: ", t);
		printf("%.7lf", rtime);
		printf("\n");
	}
	return 0;
}
