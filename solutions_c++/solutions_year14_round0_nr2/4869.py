#include<iostream>
#include<fstream>
#include <iomanip>
#include <limits>
using namespace std;

double getTime(double farmPrice, double speedGain, double goal, double speed=2, double init=0){
		double time1,time2;
		time1=init+ (goal/speed);
		time2=init + farmPrice/speed + (goal/(speedGain+speed));
		//cout<<init<<" "<<speed<<" "<<endl<<time1<<" = "<<init<<" + "<<(goal/speed)<<endl<<time2<<" = "<<init<<" + "<<farmPrice/speed<<" + "<<(goal/(speedGain+speed))<<endl;
		if(time1<=time2)return time1;
		else return getTime(farmPrice,speedGain,goal,speed+speedGain,init+(farmPrice/speed));
	}

int main(){
	int t,n=1;
	double c,f,x;
	ifstream ifile("B-small-attempt0.in");
	ofstream ofile("outPut.out");
	ifile>>t;
	std::cout.precision(std::numeric_limits<double>::digits10);
	ofile.precision(std::numeric_limits<double>::digits10);
	
	while(t--){
		ifile>>c>>f>>x;
		ofile<<"Case #"<<n++<<": "<<getTime(c,f,x)<<endl;
	}
}
