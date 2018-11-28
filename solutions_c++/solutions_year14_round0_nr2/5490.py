#include<iostream>
using namespace std;
double c, f, x;
#define eps 1e-9
bool test(double t){
	double now = 0;
	double in = 2;
	if ((t - now) * in >= x) return true;
	while (true){
		//cout<<t - now<<' '<<c / f<<' '<<c / in<<endl;
		if (t - now <= c / f)return ((t - now) * in >= x);
		//if (t - now <= c / in) return ((t - now) * in >= x);
		now += c / in;
		in += f;
		
		if ((t - now) * in >= x) return true;
	}
}
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out2.txt", "w", stdout);
	int t, tt;
	for(scanf("%d ", &tt), t = 0; t < tt; ++t){
		cin>>c>>f>>x;
		double a = 0, b = 100000;
		/**/
		while (b - a > eps){
			double mid = (a + b) / 2;
			//cout<<a<<' '<<b<<' '<<mid<<' '<<test(mid)<<endl;
			if (test(mid)) b = mid;
			else a = mid; 
		}
		test(0.5);
		printf("Case #%d: %.10lf\n", t + 1, a);
	}
}
