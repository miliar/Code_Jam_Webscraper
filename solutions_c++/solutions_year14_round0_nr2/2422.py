#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std; 



double find_result(double C,double F, double X);


int main(int argc, char **argv)
{
	ifstream file("B-large.in", ifstream::in);
	ofstream out("output.in", ofstream::out);

	int T; 

	file >> T; 


	for(int i=0; i<T; i++)
	{
		double C, F, X;

		file >> C; 
		file >> F;
		file >> X; 


		double result = find_result(C,F,X);

		out.precision(7);
		out << "Case #" << i+1 << ": " << result << endl; 

	}



	return 0; 
}




double find_result(double C,double F, double X)
{
	
	double rate = 2.0;
	double t = 0.0; 


	while(((X-C)/rate) > (X/(rate+F)))   //symferei na agorasw farm 
	{

		t = t+ (C/rate); 
		rate += F;

		
	}



	return t + X/rate; 
}
