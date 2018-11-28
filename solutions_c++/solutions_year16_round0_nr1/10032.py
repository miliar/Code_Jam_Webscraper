#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <ctype.h>
#include <stdlib.h>
#include <string>
#include <thread>
#include <mutex>
#include <iomanip> 
#include <gsl/gsl_poly.h>
#include <omp.h>
#include <ctime>
#include <fstream>
#include <sstream>

using namespace std;

int main(){
	int T;
	cin >> T;
	if(T<1 || T>100){
		cout<<"Number of testcases should be between 1 and 100 both inclusive"<<endl;
		exit(1);
	}
	
	bool exit_test_case = false;
	int* T_arr = new int[T];
	
	for(int T_idx=0; T_idx < T; T_idx++){
		cin >> T_arr[T_idx];		
	}
	
		
	for(int T_idx=0; T_idx < T; T_idx++){
		exit_test_case = false;
		bool map[10];
		for(int map_idx=0; map_idx< 10; map_idx++){
			map[map_idx] = false;
		} 
		vector<int> d_v;
		int N;
		N = T_arr[T_idx];
		if(N <0){
			cout<<"Invalid input"<<endl;
			continue;
		}
		if(N == 0){
			cout<<"Case #"<<T_idx+1<<": "<< "INSOMNIA" << endl;
			continue;
		}
		if(N == 1){
			cout<<"Case #"<<T_idx+1<<": "<< "10" << endl;
			continue;
		}
		int times = 0;
		int back_N = N;
		while(!exit_test_case){
			times++;
			back_N = times * N;
			
			while(true){
				int q = back_N/10;
				int r = back_N%10;
							
				if(map[r]==false){
					
						
					map[r] = true;
					d_v.push_back(r);					
				}
				back_N = back_N/10;
				if(back_N == 0){
					break;
				}
				if(back_N<=9){
					r = back_N;
													
					if(map[r]==false){						
						map[r] = true;
						d_v.push_back(r);					
					}
					break;
				}		
			}
			if(d_v.size()<10){				
				exit_test_case = false;				
				
			}else{
				cout<<"Case #"<<T_idx+1<<": "<< times*N << endl;
				times=0;				
				exit_test_case = true;
			}
		}
	}
}
