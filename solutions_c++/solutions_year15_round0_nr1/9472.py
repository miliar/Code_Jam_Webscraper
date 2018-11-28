/*
 * main.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Anisha
 */

#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream fin("A-large.in");
	int test_cases;
	fin>>test_cases;

	int result[test_cases];
	for(int i = 0; i < test_cases; ++i){
		result[i] = 0;
	}

	for(int i = 0; i < test_cases; ++i){
		int Smax;
		fin>>Smax;

		string input;
		fin>>input;
		int* S = new int[Smax+1];
		for(int k = 0; k < Smax+1; ++k){
			S[k] = input[k]-'0';
		}


		int res=0;int flag = 0;
		for(int j = 0; j < Smax+1; ++j){
			if(res < j){
				result[i]++;
				flag = 1;

			} else {
				flag = 0;
			}
			res += flag+S[j];
		}
	}

	for(int i = 0; i < test_cases; ++i){

		cout<<"Case #"<<(i+1)<<": "<<result[i]<<endl;

		}
	return 0;
}


