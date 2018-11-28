


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <climits>
#include <iomanip>


const double Pi = acos(-1.0);
typedef long long LL;

#define Set(a, s) memset(a, s, sizeof (a))
#define Rd(r) freopen(r, "r", stdin)
#define Wt(w) freopen(w, "w", stdout)

using namespace std;

double timeItTakes(double farmCost, double farmRate, double cookieGoal, double currentTime, double numFarms, double currentRate){

	double method1Time = currentTime + cookieGoal/currentRate;
	if(currentRate>100){
		return method1Time;
	}
	if(method1Time < timeItTakes(farmCost, farmRate, cookieGoal, currentTime+(farmCost/currentRate), numFarms+1, currentRate+farmRate)){
		return method1Time;
	}
	else{
		//cout<<"current time: "<<currentTime+(farmCost/currentRate)<<" current farms: "<<numFarms+1<<endl;
		return timeItTakes(farmCost, farmRate, cookieGoal, currentTime+(farmCost/currentRate), numFarms+1,currentRate+farmRate);
	}
}

int main(){
	Rd("B-large.in");
	Wt("answers2.out");
	int t;
	cin>>t;
	for(int n=1;n<=t;n++){
		double farmCost, farmRate, cookieGoal;
		cin>>farmCost>>farmRate>>cookieGoal;
		double currentRate=2.000000;
		//double currentCookies=0.000000;
		double time;
		if(cookieGoal<farmCost){
			time = cookieGoal/currentRate;
		}
		else{
			double method1 =0.00000000;
			double method2 =0.00000000;
			double numFarms=0.00000000;
			double currentTime=0.00000000;
			double temp=0;
			while(temp>=method1){
				temp = currentTime+(cookieGoal)/currentRate;
				method2 = currentTime + (farmCost/currentRate);
				numFarms++;
				currentRate+=farmRate;
				method1=method2+(cookieGoal)/currentRate;
				currentTime=method2;
				/*method1=currentTime+(cookieGoal)/currentRate;
				method2=currentTime+(farmCost/currentRate);
				numFarms++;
				currentRate+=farmRate;
				currentTime=method2;*/
			}
			time = temp;
		}
		cout<<"Case #"<<std::setprecision(13)<<n<<": "<<time<<endl;
	}






	return 0;

}
