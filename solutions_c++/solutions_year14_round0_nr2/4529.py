#include <fstream>
using namespace std;
int main(){
	ofstream output;
	ifstream input;
	output.open("output.txt");
	input.open("input.txt");
	int nr_test;
	input>>nr_test;
	output.precision(7);
	output.setf(ios::fixed);
	output.setf(ios::showpoint); 
	for(int i=1;i<=nr_test;i++)
	{
		double C,F,X,CPS=2;
		input>>C>>F>>X;
		double total_time=0;
		bool ok=1;
		double time_to_end;
		double time_to_farm;
		double time_farm;
		while(ok){
			time_to_farm=C/CPS;
			time_to_end=X/CPS;
			time_farm=X/(CPS+F);
			if(time_to_end<(time_farm+(time_to_farm)))
			{
				ok=0;
				total_time+=time_to_end;
			}
			else{
				total_time+=time_to_farm;
				CPS=CPS+F;
			}
		}
		output<<"Case #"<<i<<": "<<total_time<<endl;

	}
	input.close();
	output.close();
	return 0;
}