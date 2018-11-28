/*
* @Author: amber
* @Date:   2015-04-11 16:38:37
* @Last Modified by:   amber
* @Last Modified time: 2015-04-12 01:49:29
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

void print_v(std::vector<int>& v){
	for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i) {
		cout << *i << "|";
	}
	cout << endl;
}

// this func is wrong
int duct_wrong(int num) {
	int half = (num >> 1);
	if (num <= 2)
		return num;
	if ((half << 1) == num) {
		return duct_wrong(half) + 1;
	} else {
		return duct_wrong(half + 1) + 1;
	}
}

// int duct(std::vector<int>& v) {
// 	int num = v.front();
// 	cout << "num:" << num << endl;
// 	print_v(v);
// 	std::pop_heap(v.begin(),v.end()); v.pop_back();
// 	if (num <= 3)
// 		return num;
// 	int half = (num >> 1);
// 	if ((half << 1) == num) {
// 		v.push_back(half);
// 		std::push_heap(v.begin(),v.end());
// 		v.push_back(half);
// 		std::push_heap(v.begin(),v.end());
// 		return min(duct(v) + 1, num);
// 	} else {
// 		v.push_back(half);
// 		std::push_heap(v.begin(),v.end());
// 		v.push_back(half + 1);
// 		std::push_heap(v.begin(),v.end());
// 		return min(duct(v) + 1, num);
// 	}
// }

#define d(i, j) ((int)std::ceil(i/(double)(j+1)))

//((i+j)/(j+1))

int s[1001][1001];

int duct(std::vector<int>& v) {
	// print_v(v);
	int max_v = *(std::max_element(v.begin(), v.end()));
	s[0][0] = d(v[0], 0);
	for(int i = 1; i < v.size(); i++) {
		s[0][i] = max(s[0][i-1], d(v[i], 0));
	}
	// cout << 0 << " :";
	// for(int j = 0; j < v.size(); j++) { // j is vec head j elements
	// 	cout << s[0][j] << " ";
	// }
	// cout << endl;
	for(int i = 1; i < max_v; i++) { // i is split times
		s[i][0] = d(v[0], i);
		for(int j = 1; j < v.size(); j++) { // j is vec head j elements
			// s[i][j] = max(s[i][j-1], d(v[j], i));
			int tmp = max_v;
			for(int k = 0; k < i; k++)
				tmp = std::min(
							tmp,
							max(s[k][j-1], d(v[j], i - k))
						);
			s[i][j] = std::min(
							tmp,
							max(s[i][j-1], d(v[j], 0))
						);
		}
		// for(int j = 0; j < v.size(); j++) { // j is vec head j elements
		// 	s[i][j] += i;
		// }
		// cout << i << " :";
		// for(int j = 0; j < v.size(); j++) { // j is vec head j elements
		// 	cout << s[i][j] << " ";
		// }
		// cout << endl;
	}
	int min_res = max_v;
	for (int i = 0; i < max_v; ++i) {
		min_res = std::min(min_res, s[i][v.size() - 1] + i);
	}
	return min_res;
}

int main(){
	int T;
	scanf("%d", &T);
	// cout << T << endl;

	// cout << 3 / 2 << endl;
	// for (int i = 1; i < 10; ++i) {
	// 	cout << i << " : " << duct(i) << endl;
	// }

	for (int i = 0; i < T; i++) {
		int D;
		scanf("%d", &D);
		// cout << 'D' << D << endl;
		vector<int> v;
		for (int j = 0; j < D; ++j) {
			int p;
			scanf("%d", &p);
			// cout << p << " ";
			v.push_back(p);
		}
		// cout << endl;
		// now that we have D and vec_p
		// print_v(v);
		// std::make_heap(v.begin(), v.end());
		// print_v(v);
		// cout << duct(v) << endl;
		printf("Case #%d: %d\n", i + 1, duct(v));

		// // break;
		// if (i > 5)
		// 	break;
	}
	return 0;
}