#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
 
using namespace std;

int compare(const void *x, const void *y)
{
  double x_value = *(double*)x;
  double y_value = *(double*)y;
  if (x_value < y_value) return -1;
  if (x_value > y_value) return  1;
  return 0;
}

 
int main() {

	fstream output("output_p4.txt", fstream::out);
	//outputFile << "writing to file";
	fstream input("input.txt", fstream::in);


	int testcases = 0;
	int nr_blocks = 0;
	int dec_war = 0;
	int war = 0;

	input >> testcases;

	for(int i = 0; i < testcases; i++){
		input.ignore(1, '\n');
		input >> nr_blocks;

		war = 0;
		dec_war = 0;

		double* blocks_naomi = new double[nr_blocks];
		double* blocks_ken = new double[nr_blocks];
		double* blocks_ken2 = new double[nr_blocks];

    	for(int j = 0; j < nr_blocks; j++){
    		input >> blocks_naomi[j];
    	}
    	input.ignore(1, '\n');
       	for(int j = 0; j < nr_blocks; j++){
    		input >> blocks_ken[j];
    		blocks_ken2[j] = blocks_ken[j];
    	}

		qsort(blocks_naomi, nr_blocks , sizeof(double), compare);
		qsort(blocks_ken, nr_blocks, sizeof(double), compare);
		qsort(blocks_ken2, nr_blocks, sizeof(double), compare);

		for(int k = 0; k < nr_blocks; k++){
			bool found_bigger = false;
			for(int l = 0; l < nr_blocks; l++){
				if(!found_bigger && blocks_ken2[l] > blocks_naomi[k]){
					found_bigger = true;
					blocks_ken2[l] = -1.0;
				}
			}
			if(!found_bigger){
				war++;
			}
		}
		
		bool quit = false;
		for(int k = 0; k < nr_blocks; k++){
			bool found_bigger = false;
			bool all_bigger = true;
			int n = 0;
			for(int m = k; m<nr_blocks;m++){
				if(!(blocks_naomi[m] > blocks_ken[n]))
					all_bigger = false;
				n++;
			}
			if(all_bigger){
				dec_war = nr_blocks-k;
				quit = true;
				break;
			}
			if(quit){
				break;
			}
			for(int l = nr_blocks-1; l >= 0; l--){
				if(!found_bigger && blocks_ken[l] > blocks_naomi[k]){
					found_bigger = true;
					blocks_ken[l] = -1.0;
				}
			}
		}
		output << "Case #" << i+1 << ": ";
		output << dec_war << " " << war;

    	delete [] blocks_ken;
    	delete [] blocks_naomi;
    	delete [] blocks_ken2;
		if(i != testcases-1){
			output << endl;
		}
	}
	
	return 0;
}