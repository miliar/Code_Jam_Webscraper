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


string solve(row_t& row_1,row_t& row_2){

    string solution;
    
    std::sort(row_1.begin(),row_1.end());
    std::sort(row_2.begin(),row_2.end());
    
    int num_found=0;
    int answer=0;
    
    for(auto& n: row_2){
    
    	auto s = std::find(row_1.begin(),row_1.end(),n);
    	
    	if( s != row_1.end() ){
    	
    		answer = n;
    		num_found++;
    	
    	}
    
    }
    
    if(num_found==1){
    
    	solution = to_string(answer);
    
    }else if(num_found>1){
    
    	solution = "Bad magician!";
    
    }else{
    
    	solution = "Volunteer cheated!";
    
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

			int noop;
			int answer_1;
			int answer_2;
			row_t row_1 = {0,0,0,0};
			row_t row_2 = {0,0,0,0};
		    
			f >> answer_1;
			
			for(int x=0;x<4;x++){
			
				for(int y=0;y<4;y++){
					
					if(x==answer_1-1){
					
						f >> row_1[y];
						
					}else{
					
						f >> noop;
					
					}
				}
				
			}
			
			f >> answer_2;
			
			for(int x=0;x<4;x++){
			
				for(int y=0;y<4;y++){
					
					if(x==answer_2-1){
					
						f >> row_2[y];
						
					}else{
					
						f >> noop;
					
					}
				
				}
				
			}
			
			
			if(!test_case || test_case==case_no){
				
				string solution = solve(row_1,row_2);
				cout << "Case #" << case_no << ": " << solution << endl;
				if(!test_case) out << "Case #" << case_no << ": " << solution << endl;
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
