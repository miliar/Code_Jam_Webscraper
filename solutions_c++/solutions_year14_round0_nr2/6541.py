#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

double C,F,X;
int T;
double ret,rate;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> T;
	for (int t = 0; t < T; t++){
		cin >> C >> F >> X;
		ret=0.0f;
		rate=2.0f;
		while(true){
			ret+=(C/rate);
			if ((X-C)/rate < X/(rate+F)){
				ret+=(X-C)/rate;
				break;
			}else rate+=F;
		}
		cout << "Case #" << t+1 << ": " << setiosflags(ios::fixed) << setprecision(7) << ret << endl;
	}
	
	return 0;
}
