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
#include <bitset>

using namespace std;

unsigned long long is_prime(unsigned long long num){
	unsigned long long sqrt_num = sqrt(num);
	unsigned long long div = -1;
	//bool prime = true;
	for(unsigned long long i=2; i< sqrt_num+1; i++){
		if(num%i ==0){
			//prime = false;
			//cout<<"not prime"<<endl;
			div = i;
			break;
		}
	}
	//if(div==0)
		//cout<<"div is wrong"<<endl;
	return div;
}

unsigned long long get_value(string s, int base){	
    	unsigned long long value = std::stoull(s, 0, base);
    	return value;
}

vector<string> generateGrayarr(int n)
{
    
    vector<string> arr;
 
    // start with one-bit pattern
    arr.push_back("0");
    arr.push_back("1");
 
    // Every iteration of this loop generates 2*i codes from previously
    // generated i codes.
    int i, j;
    for (i = 2; i < (1<<n); i = i<<1)
    {
        // Enter the prviously generated codes again in arr[] in reverse
        // order. Nor arr[] has double number of codes.
        for (j = i-1 ; j >= 0 ; j--)
            arr.push_back(arr[j]);
 
        // append 0 to the first half
        for (j = 0 ; j < i ; j++)
            arr[j] = "0" + arr[j];
 
        // append 1 to the second half
        for (j = i ; j < 2*i ; j++)
            arr[j] = "1" + arr[j];
    }
 
    // print contents of arr[]
    //for (i = 0 ; i < arr.size() ; i++ )
        //cout << arr[i] << endl;
	return arr;
}

int main(){
	//vector<string> codes = generateGrayarr(16);
	//cout<<is_prime(get_value("100011", 9))<<endl;
	//exit(1);
	int T;
	cin >> T;
	if(T<1 || T>100){
		cout<<"Number of testcases should be between 1 and 100 both inclusive"<<endl;
		exit(1);
	}
	
	bool exit_test_case = false;
	int** T_mat = new int*[T];
	for(int T_idx=0; T_idx < T; T_idx++){
		T_mat[T_idx] = new int[2];		
	}
	
	
	for(int T_idx=0; T_idx < T; T_idx++){
		cin >> T_mat[T_idx][0];
		cin >> T_mat[T_idx][1];		
	}

	for(int test_case_idx=0; test_case_idx< T; test_case_idx++){
		int N = T_mat[test_case_idx][0];
		int J = T_mat[test_case_idx][1];
		cout<<"Case #"<<test_case_idx+1<<":"<<endl;
		vector<string> codes = generateGrayarr(N-2);
		int J_idx=0;
		for(int code_idx=0; code_idx< codes.size(); code_idx++){
			bool prime = false;
			string code1 = codes[code_idx];
			//if(code.at(0)!='1' && code.at(N-1)!='1')
				//continue;
			string code = "1" + code1 + "1";
			unsigned long long div_arr[9];
			for(int base=2; base< 11; base++){
				//cout<<"for base = "<< base <<"we got "<<is_prime(get_value(code, base))<<endl;
				unsigned long long div = is_prime(get_value(code, base));
				if(div != -1){
					int base_idx=base-2;
					div_arr[base_idx] = div;
				}else{
					prime = true;
					//cout<<"prime"<<endl;
					break;
				}
			}
			if(prime == false){
				J_idx++;
				cout<<code<<" ";
				for(int div_idx=0; div_idx< 9; div_idx++){
					cout<<div_arr[div_idx]<<" ";
				}
				cout<<endl;
				if(J_idx>=J){
					break;
				}
			}
		}
	}
	
	/*	
	for(int T_idx=0; T_idx < T; T_idx++){
		cout << T_mat[T_idx][0]<<" ";
		cout << T_mat[T_idx][1]<<endl;
	}*/
}
