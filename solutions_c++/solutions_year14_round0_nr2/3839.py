/************************************************************************************
"Cookies.cpp" - Cookie Clicker Alpha. Problem B. Qualification Round 04/11/2014.

When you start, first check if the line y=m1*t intersects the line y=m2*t+A2 below
the constant line y=X, where m2= m1+F, and A2=C/m1. What we are doing is to check
if the fastest way to get to X is by the line 1 or the line 2 (buying or not the
farm). If we don't get faster by buying the farm, then we wait untill we get there.
But if we do get faster by buying the farm, then we add the time A2, to the total,
shift the time axis and repeat the proces, but now we use m2, m3=m2+F, A3=C/m2.
************************************************************************************/

#define MAX_ARGS 3
#define ARG_POS_IN 1
#define ARG_POS_OUT 2
#define INITIAL_SLOPE 2 // initially we get 2 cookies per second.


#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;


int main(int argc, char* argv[])
{

	ifstream input_file;
	ofstream output_file;

	if (argc != MAX_ARGS) {
		cerr << "Usage: " << argv[0] << " <INPUT-FILE> <OUTPUT-FILE>" << endl;
		return EXIT_FAILURE;
	}

	input_file.open(argv[ARG_POS_IN]);
	output_file.open(argv[ARG_POS_OUT]);

	size_t T; // Amount of test cases.

	input_file >> T;

	for (size_t i=0; i<T; i++){

		double total_time = 0;
		double C, F, X; // X is the goal, F is the farm bonus, and C is the cost of a farm.
		double m_1=INITIAL_SLOPE, m_2, A_2; // A_2 is the intersection with the time axis of the line 2.
								// m_1 and m_2 are the slopes of the lines.
		double intersection; //this is the value of the ordinate where the 2 lines intersect.
		bool keep_going=true;
			
		//load data

		input_file >> C;
		input_file >> F;
		input_file >> X;

		
		// evaluate

		do {

			A_2 = (C)/m_1;
			m_2 = m_1 + F;
			intersection=A_2*m_1*(m_1+F)/F;


			if (intersection >= X) { total_time += X/m_1; keep_going=false; }
			
			else{
				total_time += A_2;
				m_1 = m_2;
			}
		
		} while(keep_going);


		//print output
		output_file.setf(ios::fixed);
		output_file.setf(ios::showpoint);
		output_file.precision(7);
		output_file << "Case #" << i + 1 << ": " << total_time << endl;


	}
	
	input_file.close();
	output_file.close();	

	return EXIT_SUCCESS;
}

