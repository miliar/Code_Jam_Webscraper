#include <iostream>
#include <fstream>
#include <limits.h>
#include <iomanip>
using namespace std;

class OptimizationOfCookies
{
	private:
		double OriginCookiesPerSecond;
		double CostOfFarm;
		double CookiePerFarm;
		double ObjectCookies;
		
		double NextEventTime;
		double TotalTime;
		double UntilCoverObject;
		double TimeForAnotherFarm;
		double FarmCount;
		double TotalCookiesProduction;
		double TimeForObject;
		
		void FindOptimization( void )
		{
			double flag=0.0;
			this->NextEventTime = 0.0;
			this->TotalTime = 0.0;
			this->UntilCoverObject = 0.0;
			this->TimeForAnotherFarm = 0.0;
			this->FarmCount = 0.0;
			this->TotalCookiesProduction = 0;
			this->TimeForObject = 0;
			
			this->TotalCookiesProduction = this->OriginCookiesPerSecond + this->CookiePerFarm * this->FarmCount;
			this->TimeForAnotherFarm = this->CostOfFarm / this->TotalCookiesProduction;
			this->TimeForObject = this->ObjectCookies / this->TotalCookiesProduction;
			this->TotalTime = this->TotalTime + this->NextEventTime;
			this->NextEventTime = this->TimeForAnotherFarm;
			flag = this->TotalTime + this->TimeForObject;
			this->FarmCount++;
			
			//cout << "Until Cover Object: " << this->UntilCoverObject << endl;
			//cout << "Total Time: " << this->TotalTime << endl;
			//cout << "Time For Object: " << this->TimeForObject << endl;
			
			while( true )
			{
				this->UntilCoverObject = flag;
				this->TotalCookiesProduction = this->OriginCookiesPerSecond + this->CookiePerFarm * this->FarmCount;
				this->TimeForAnotherFarm = this->CostOfFarm / this->TotalCookiesProduction;
				this->TimeForObject = this->ObjectCookies / this->TotalCookiesProduction;
				this->TotalTime = this->TotalTime + this->NextEventTime;
				this->NextEventTime = this->TimeForAnotherFarm;
				flag = this->TotalTime + this->TimeForObject;
				this->FarmCount++;
			
				//cout << "Until Cover Object: " << this->UntilCoverObject << endl;
				//cout << "Total Time: " << this->TotalTime << endl;
				//cout << "Time For Object: " << this->TimeForObject << endl;
				
				if( this->UntilCoverObject < flag )
					break;
			}
		}
	public:
		void InputValues( double OCPS, double COF, double CPF, double OC )
		{
			this->OriginCookiesPerSecond = OCPS;
			this->CostOfFarm = COF;
			this->CookiePerFarm = CPF;
			this->ObjectCookies = OC;
			
			this->FindOptimization();
		}
		double OutputOptima()
		{
			return this->UntilCoverObject;
		}		
};

int main( int argc, char** argv )
{
	ifstream myfile;
	int CaseNum;
	double OriginCookiesPerSecond = 2;
	double CostOfFarm;
	double CookiePerFarm;
	double ObjectCookies;
	
	OptimizationOfCookies optcookies;
	
	myfile.open(argv[1]);
	
	if( myfile.is_open() )
	{
		myfile >> CaseNum;
		
		for( int i=0; i<CaseNum; i++ )
		{
			myfile >> CostOfFarm >> CookiePerFarm >> ObjectCookies;
			
			optcookies.InputValues( OriginCookiesPerSecond, CostOfFarm, CookiePerFarm, ObjectCookies );
			
			cout << "Case #" << i+1 << ": " << setprecision(7) << optcookies.OutputOptima() << endl;
		}
	}
	
	myfile.close();
	return 0;
}
