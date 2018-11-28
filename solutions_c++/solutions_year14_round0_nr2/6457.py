#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int ch;
	cin >> ch;
	for(int j = 1; j<=ch;j++){
		double c,x,f;
		double currentRate = 2, backlogTime = 0;
		double timeWithNewFarm = 0;
		double timeWithCurrentRate = 0;

		cin >> c >> f >> x;
		while(1){
			timeWithCurrentRate = (x/currentRate) + backlogTime;
			timeWithNewFarm = backlogTime + (c/currentRate) + (x/(currentRate+f));

			if(timeWithCurrentRate <= timeWithNewFarm){
				break;
			}

			backlogTime = backlogTime + (c/currentRate);
			currentRate = currentRate + f;

		}

		printf("Case #%d: %.7f", j,timeWithCurrentRate);
		cout<<endl;
	}
	return 0;
}