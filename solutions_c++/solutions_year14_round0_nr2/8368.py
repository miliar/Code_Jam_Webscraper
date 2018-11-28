#include <iostream>
#include <cmath>
using namespace std;

const double eps = 1e-8;

typedef long long ll;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 0; i < t; i++){
		cout<<"Case #"<<(i + 1)<<": ";
		double c,f,x;
		cin>>c>>f>>x;
		double n = (x*f - 2*c - c*f)/c/f;
		double total, dec;
		dec = modf(n,&total);
		if(dec > 0){
			total += 1;
		}
		
		total = max(total, 0.0);

		double ti = 0;
		for(ll j = 0 ; j <= (ll)total; j++){
			double a = c/(2 + f*j);
			if(a < eps)
				break;
			ti += a;
		}
		ti += (x - c) / (2.0 + f*total);

		printf("%.8lf\n",ti);
	}
}