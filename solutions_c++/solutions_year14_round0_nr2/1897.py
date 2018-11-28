#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int k = 1; k<= T; ++k){
		double ans = 0;
		double C,F,X;
		cin >> C >> F >> X;
		if(X <= C){
			ans = X/2;
		}
		else{
			double t = X/C - 2/F - 1;
			if(t< 0){
				ans = X/2;
			}
			else if(t< 1){
				ans = C/2 + X/(2+F);
			}
			else{
				int st = 0;
				for(st = 0; st <= t; ++st){
					ans += C/(2+st*F);
				}
				ans += X/ (2+st*F);
			}
		}
		printf("Case #%d: %.7lf\n", k, ans);
	}
}