#include <iostream>
#include <string>
#include <vector>
#include <fstream>


using namespace std;

struct AStrategy
{
	double rate;
	double left;
	double time;
};
int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; i++){
		double C, F, X;
		in >> C;
		in >> F; 
		in >> X;
		AStrategy as;
		as.rate = 2;
		as.left = 0;
		as.time = 0;
		double MinTile = INT_MAX;
		while (true){
			double time_left = (X - as.left)/as.rate;
			double total_time = as.time + time_left;
			if (total_time < MinTile){
				MinTile = total_time;
			}
			/*by a farm*/
			double time_farm = (C-as.left)/as.rate;
			if (time_farm + as.time > MinTile){
				break;
			}
			as.rate += F;
			as.time += time_farm;
		}
		printf("Case # %d: %.7f\n", i+1, MinTile);
	}
	return 0;
}
