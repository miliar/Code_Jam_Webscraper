#include<cstdio>
#include<iostream>
using namespace std;


int main(){
	int Ttot;
	cin >> Ttot;

	for(int T=1;T<=Ttot;T++){
		double ans=0;
		double r=2;
		double X,C,F;

		cin >> C >> F >> X;

		while(X>=0.){
			//買わないほうが早い
			if(X/r < C/r+X/(r+F)){
				ans += X/r;
				break;
			}

			//farm買う場合
			double T = C/r;
			ans += T;
			r = r+F;

			// printf("ans=%lf T=%lf r=%lf\n",ans,T,r,X);
		}

		printf("Case #%d: %.7lf\n",T,ans);
	}
	return 0;
}
