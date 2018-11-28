#include <iostream> 
#include <fstream>
#include <vector>
#include <math.h>
#include "MyReal.h"

using namespace std;

int main() {
	cout.precision(20); 

	ifstream input("B-large.in");
	ofstream output("output.ou");
	double my_C, my_F, my_X;
	int sets, n;
	double C1, F1, X1;
	double C2, F2, X2;
	vector<double> vec1, vec2;
	
	if(input.is_open()){
		input >> sets;
		output.precision(20);
		n = 1;
		
		while(sets > 0){
			vec1.clear();
			vec2.clear();
			input >> my_C >> my_F >> my_X;
			
			for(int i = 0; i < 100000; i++){
				if(i == 0){
					vec1.push_back(my_C / 2);
					vec2.push_back(2 + my_F);
				}
				else{
					vec1.push_back(vec1[i - 1] + my_C / vec2[i - 1]);
					vec2.push_back(vec2[i - 1] + my_F);
				}
			}
			
		//	for(int i = 0; i < 30; i++){
		//		cout << i << " " << vec1[i] << " " << vec2[i] << "\n";
		//	}
			double min = my_X / 2;
			int k = 0;
			
			while(min > vec1[k]  + my_X / vec2[k]){
				min = vec1[k] + my_X / vec2[k];
				k++;
			}
			
			output << "Case #" << n << ": " << min << "\n";
			cout << n << " " << min << "\n";
			
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
