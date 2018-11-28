/************************************************************************************
"DeceitfulWar.cpp" - Problem D. Qualification Round 04/11/2014.

To count the points in the war game, naomi plays her highest block, and ken plays
his lowest if he can't win(1 point to naomi), or his highest if he can win.

To count the deceitful points naomi chooses her lowest block. if it can beat the
lowest of ken, she will say she has a block higher than ken's highest, to force
him to play his lowest, and she will play her lowest block (1point). If she can't
beat the lowest of ken, she will say she has the average of ken's two highest blocks
to force him to play his highest block and she will play her lowest (looses).
************************************************************************************/

#define MAX_ARGS 3
#define ARG_POS_IN 1
#define ARG_POS_OUT 2


#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int compare_doubles (const void *a, const void *b)
{
	const double *da = (const double*) a;
	const double *db = (const double*) b;

	return (*da > *db) - (*da < *db);
}



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

		size_t N, war_points=0, deceitful_points=0;

		//load data

		input_file >> N;
		double *blocks_naomi = new double[N];	
		double *blocks_ken = new double[N];
		size_t bot_ken=0;
		int top_ken;	
	
		for(size_t j=0; j<N; j++){
			input_file >> blocks_naomi[j];
		}

		for(size_t j=0; j<N; j++){
			input_file >> blocks_ken[j];
		}

		qsort(blocks_naomi, N, sizeof(double), compare_doubles);
		qsort(blocks_ken, N, sizeof(double), compare_doubles);

		// evaluate
		//deceitful
		for (size_t j=0; j<N; j++){
			if (blocks_naomi[j]>blocks_ken[bot_ken]){
				bot_ken++;
				deceitful_points++;
			}
		}
				
		//war
		top_ken=N-1;
		for (int k=N-1; k>=0; k--){

			if(blocks_naomi[k]>blocks_ken[top_ken]){
				war_points++;
			}
			else top_ken--;
		}

		//print output
		output_file << "Case #" << i + 1 << ": " << deceitful_points << " " << war_points << endl;
		
		//delete dynamic arrays
		delete blocks_naomi;
		delete blocks_ken;

	}
	
	input_file.close();
	output_file.close();	

	return EXIT_SUCCESS;
}

