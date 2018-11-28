/*
 * solution_template.cpp
 * This is the solution template from  rng..58
 *  Created on: Apr 9, 2016
 *      Author: chubin
 */

#include <iostream>
#include <cstdio>
#include <map>
#include <list>
#include <stdint.h>
using namespace std;

#define LOOP(i,n) for((i)=0;(i)<(uint32_t)(n);(i)++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

void solution(void){
	uint32_t number;

	uint32_t count_times = 0;

	map<uint32_t, uint32_t> * map_digits_N = new map<uint32_t, uint32_t>;

	cin >> number;

	if (number == 0) {
		map_digits_N->empty();
		delete map_digits_N;
		cout << "INSOMNIA" << endl;
		return;
	}

	count_times = 0;
	while (count_times < UINT32_MAX) {
		count_times++;
		uint32_t temp_number = count_times * number;

		while (temp_number > 0) {
			map_digits_N->insert(
					std::pair<uint32_t, uint32_t>(temp_number % 10, 0));
			temp_number = temp_number / 10;
			if (map_digits_N->size() == 10) {
				map_digits_N->empty();
				delete map_digits_N;
				cout << count_times * number << endl;
				return;
			}
		}

	}

	map_digits_N->empty();
	delete map_digits_N;
	cout << "INSOMNIA" << endl;
	return;

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
