#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>


class basicAnalizer{
private:
	std::ifstream* ifs;
	
	double C,F,X;
	
	void readData(){
		*ifs >> C >>F>>X;
	}
public:
	basicAnalizer(std::ifstream *ifs):ifs(ifs){ readData();}
	double doWork(){
		double rate=2;
		
		bool done = false;
		double time=0;
		
		double timeToWin,timeToHome,timeToWinIfHome;
		while(!done){
			timeToWin = X/rate;
			timeToHome = C/rate;
			timeToWinIfHome = timeToHome + X/(rate+F);
			
			if( timeToWinIfHome<timeToWin ){
				time += timeToHome;
				rate += F;
			}else{
				time += timeToWin;
				done=true;
			}
		}
		
		
		return time;
	}
};

int main(){
	double r=0;
	int Testcases=0;
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );
	
	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
		basicAnalizer analizer( &ifs );
		
		r=analizer.doWork();
		
		ofs<<std::setprecision(7)<<std::fixed;
		ofs<<"Case #"<<i+1<<": "<<r<<std::endl;
	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
