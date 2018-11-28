/*
	g++ --std=c++11 main.cpp -o main
	
*/


#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <array>
#include <vector>
#include <numeric>
#include <limits>
#include <random>
#include <functional>
#include <chrono>
#include <ctime>
#include <algorithm>
#include <queue>
#include <utility>
#include <list>
#include <map>
#include <cmath>
#include <bitset>

using namespace std;
typedef array<int,4> row_t;



double solve(double C,double F,double X){

    double solution=0.0;  
	
	if(X>solution){
	
		double r = 2;
		
		double s = X/r;
	
		if(F>0){
		
			double e = 0;
	
			while(1){
		
				e += C/r;
		
				r += F;
	
				double t = e + (X/r);
			
				if(t<s){
			
					s=t;
					continue;
			
				}
			
				break;
			
			}
	
		}
		
		solution = s;
	
	}
	
    return solution;

}



int main(int argc,char** argv){

	string sample_in;
    string sample_out("codejam.out");
    
	if(argc>1)sample_in = argv[1];
    if(argc>2)sample_out = argv[2];
    
    size_t case_no = 1;
    size_t test_case = 0; //zero is bypass because case_no starts at 1
	size_t stop_case = 0;
	
    ifstream f(sample_in);
    ofstream out(sample_out);

    if(f.is_open()){
        
        size_t cb;
        f >> cb;

        while(cb--){

			double C,F,X;
			
			f >> C;
			f >> F;
			f >> X;
			
			if(!test_case || test_case==case_no){

				float solution = solve(C,F,X);
				cout << "Case #" << case_no << ": " << fixed << setprecision(7) << solution << endl;
				if(!test_case) out << "Case #" << case_no << ": " << fixed << setprecision(7) << solution << endl;
				if(test_case)break;
				
			}

			if(case_no==stop_case)break;
			
			case_no++;

        }


    }else{
	
		if(!sample_in.length())cout << "you need to specify an input file" << endl;
		else cout << "input file missing" << endl;
	
	}


    return 0;

}
