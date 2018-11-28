#include <cstdio>
#include <iostream>
using namespace std;

#define S(n)	scanf("%d",&n)
#define EPS 1e-6
#define OO 1e9

int main(){
	//freopen("in.in" , "r" , stdin);
	//freopen("out.txt" , "w" , stdout);

	int TC , cc = 0 ;
	double c , f , x , ans , coo , minn;
	S(TC);
	while(TC--){
		minn = OO;
		ans = 0;
		scanf("%lf %lf %lf", &c , &f , &x);

		coo = 2.0;
		double stemp = c / coo;
		while(stemp > EPS){
			stemp = c / coo;
			ans += x / coo;

			if(ans < minn)
				minn = ans;
			else
				break;

			ans -= x / coo;
			ans += stemp;
			coo += f;
		}

		printf("Case #%d: %.7lf\n" , ++cc , minn);
	}
	return 0;
}