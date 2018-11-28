

#include <iostream>
#include<iomanip>
using namespace std;

double getResult(double dCurrentCost,double dAdditional,double dFarmCost,double dToEarn,double dTimeInvested,double dTotalTime){
	double dNewCost;
	double dTimeToBuyFarm;
	double dTimeToEarn;
	double dNewTotalTime;
	double dResult;
	//double dTimeNeeded;
	
	dNewCost=dAdditional+dCurrentCost;
	dTimeToBuyFarm=dFarmCost/dCurrentCost;
	dTimeInvested=dTimeInvested+dTimeToBuyFarm;

	dTimeToEarn=dToEarn/dNewCost;
	//dTimeNeeded=dTimeToEarn+dTimeInvested;
	dNewTotalTime=dTimeToEarn+dTimeInvested;

	if(dNewTotalTime<dTotalTime){
		return getResult(dNewCost,dAdditional,dFarmCost,dToEarn,dTimeInvested,dNewTotalTime);
	}
	else{
return dTotalTime;
		
	}
	
}
int main()
{

	int iCases;
	double dBaseCost=2;
	double dAdditional;
	double dFarmCost;
	double dToEarn;
	double dTotalTime;

	cin>>iCases;
	for(int i=0;i<iCases;i++){
		cin>>dFarmCost;
		cin>>dAdditional;
		cin>>dToEarn;
		
		dTotalTime=dToEarn/dBaseCost;
		cout<<"\nCase #"<<i+1<<": ";
		std::cout<<std::fixed<<std::setprecision(7)<<getResult(dBaseCost,dAdditional,dFarmCost,dToEarn,0,dTotalTime);
	}
	
	
	return 0;
}

