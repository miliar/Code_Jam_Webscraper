//============================================================================
// Name        : gcj_2015.cpp
// Author      : dimalit
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>
#include <cstdio>
#include <cassert>
using namespace std;

int b_steps_for_h(const std::vector<int>& array, int h){
	assert(array.empty() || h>0);
	if(array.empty() || array[0]<=h)
		return 0;
	int steps = 0;
	for(int i=0; i<array.size() && array[i]>h; i++){
		int val = array[i];
		steps += val / h;
		if(val % h == 0)
			steps--;
	}// for i
	return steps;
}

// true if can squeeze this vect into sol
bool b_leq(const std::vector<int>& array, int sol){
	for(int h=1; h<=sol; h++){
		if(b_steps_for_h(array, h) <= sol-h)
			return true;
	}
	return false;
}

int b_solve(const vector<int>& array){
	if(array.empty())
		return 0;

	int max = array[0];
	int min = 1;
	if(max<=3)
		return max;

	while(max!=min){
		int mid = (min + max) / 2;			// eqals min if max-min=1, eq min+1 if max-min=2
		if(b_leq(array, mid))
			max = mid;
		else
			min = mid + 1;
	}// while

	return max;
}

int main() {

	freopen("b_large.in", "rb", stdin);
	freopen("b_large.out", "wb", stdout);

	int T;
	cin >> T;
	for(int t=0; t<T; t++){
		//priority_queue<int> array;
		std::vector<int> array;
		int D;
		cin >> D;
		for(int i=0; i<D; i++){
			int tmp;
			cin >> tmp;
			array.push_back(tmp);
		}// for i

		sort(array.begin(), array.end(), std::greater<int>());
		int res = b_solve(array);
		cout << "Case #" << (t+1) << ": " << res << endl;
	}// for test
	return 0;
}

///////////// OLD BUT WORKING //////////////////
//int b_solve(priority_queue<int>& array);
//
//int b_try_div(int my_top, int div, const priority_queue<int>& array){
//	priority_queue<int> array2 = array;
//	int part = my_top / div;
//	if(part*div != my_top)
//		part++;
//	int have=my_top;
//	for(; have >= part; have-=part){				// split it!
//			array2.push(part);
//	}
//	if(have!=0)
//		array2.push(have);
//	return b_solve(array2);
//}
//
//// max first
//int b_solve(priority_queue<int>& array){
//	if(array.empty())
//		return 0;
//
//	int my_top = array.top();
//	if(my_top<=3)
//		return my_top;
//
//	array.pop();
//	int res = my_top;
//	for(int div=2; div<=3; div++){			// try different div
//		int subres = b_try_div(my_top, div, array);
//		res = min(div-1+subres, res);
//	}
//	return res;
//}
