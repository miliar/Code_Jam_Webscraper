#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[] )
{
	ifstream inFile;
	ofstream outFile;
	string outputFilename;

	if(argv[2] == NULL){
		outputFilename = "out.txt";
	}
	else
		outputFilename = argv[2];

	inFile.open(argv[1], ios::in);
	outFile.open(outputFilename, ios::out);

	char output[100];
	if(!inFile.is_open())
	{
		cout<<"Invalid input file!"<<endl;
		return -1;
	}

	//Begin calculations
	//First line is number of test cases
	inFile>>output;
	int T = atoi(output);

	

	// Run for T test cases
	for(int i=0; i < T; i++)
	{
		// Initial cookie generation rate
		double G = 2.0;

		// Total time elapsed
		double totalTime = 0.0f;

		//Cost of new house
		inFile >> output;
		double C = atof(output);

		//Increase in generation rate
		inFile >> output;
		double F = atof(output);

		//Final target
		inFile >> output;
		double X = atof(output);

		bool done = false;
		while(!done)
		{
			//Time required to buy new house
			double t_new_house = C/G;

			//Time required to reach target after buying new house
			double t_X_with_house = X/(G + F);
			
			//Time required to reach target without buying new house
			double t_X_no_house = X/G;

			// Buy house if it is worth it :)
			if (t_X_no_house > (t_X_with_house + t_new_house))
			{
				G += F;
				totalTime += t_new_house;
			}
			else
			{
				totalTime += t_X_no_house;
				done = true;
			}
		}
		
		
		outFile<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<totalTime<<endl; 
		
	 }
	
	inFile.close();

	outFile.close();
	return 0;
}