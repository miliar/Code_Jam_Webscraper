/*
 * solution_template.cpp
 * This is the solution template from  rng..58
 *  Created on: Apr 9, 2016
 *      Author: chubin
 */

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <stdint.h>

using namespace std;

#define LOOP(i,n) for((i)=0;(i)<(uint32_t)(n);(i)++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

void solution(void){

	char state;
	uint32_t num_state = 0;

	string mystring;

	cin >> mystring;

	const char * line = mystring.c_str();

	uint32_t len = mystring.size();

	for(uint32_t i = 0; i < len; i++){
		if((state != line[i])
				&&((line[i] == '-')|| (line[i] == '+'))){
			num_state++;
			state = line[i];
		}
	}
	if(state == '-'){
		cout << num_state <<endl;
	} else {
		cout << num_state - 1 << endl;
	}
}

int main(void){
	uint32_t TC,tc;
	cin >> TC;
	LOOP(tc,TC){
		printf("Case #%d: ", tc+1);
		solution();
	}
	return 0;
}
