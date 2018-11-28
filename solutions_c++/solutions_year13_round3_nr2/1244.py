//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "math.h"
#include <algorithm>
#include <vector>
#include <string>
using namespace std;




int main() {
	int cunt,kunt;
	int coord_x, coord_y, cur_x, cur_y, step;
	string word;

	cin >> cunt;

	for (kunt=1; kunt<=cunt; ++kunt){
		step = 1;
		cur_x = 0;
		cur_y = 0;
		cin >> coord_x;
		cin >> coord_y;
		cout << "Case #" << kunt << ": ";
		char to_x,to_y,from_x,from_y;
			if (coord_y < 0){
				to_y='S'; from_y='N';
				coord_y = -coord_y;
			} else {
				to_y='N'; from_y='S';
			}
			if (coord_x < 0){
				to_x='W'; from_x='E';
				coord_x = -coord_x;
			} else {
				to_x='E'; from_x='W';
		}
		while (coord_x > cur_x + step || coord_y > cur_y + step){
			if ((coord_x-cur_x-step) >= 0 && (coord_y-cur_y-step) >= 0){
				if ((coord_x-cur_x) < (coord_y-cur_y)){
					cur_x += step;
					cout << to_x;
				} else {
					cur_y += step;
					cout << to_y;
				}
			} else if ((coord_x-cur_x-step) >= 0){
				cur_x += step;
				cout << to_x;
			} else if ((coord_y-cur_y-step) >= 0){
				cur_y += step;
				cout << to_y;
			}
			++step;
		}

		while (coord_y != cur_y){
			if (cur_y + step > coord_y){
				cur_y -= step;
				cout << from_y;
			} else {
				cur_y += step;
				cout << to_y;
			}
			++step;
		}
		while (coord_x != cur_x){
			if (cur_x + step > coord_x){
				cur_x -= step;
				cout << from_x;
			} else {
				cur_x += step;
				cout << to_x;
			}
			++step;
		}






		cout << endl;

	}
	return 0;
}
