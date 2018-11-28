#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int k = 1; k<=t; k++){
		double c, f, x;
		double ans = 0.0;
		double n = 2;
		cin>>c>>f>>x;
		while(true){
			double one = x/n;
			double two = c/n;
			double three = x/(n+f);
			double twoPlusThree = two + three;
			//if one is lesser than two + three, then just add one to the ans & thats the ans.
			//otherwise increment n by 4 and add two to the ans and continue.
			if(one < twoPlusThree){
				ans += one;
				//printf("%.7f ", one);
				break;
			}
			else{
				//printf("%.7f ", two);				
				ans += two;
				n += f;
			}
		}
		printf("Case #%d: %.7f\n", k, ans);
	}
	return 0;
}