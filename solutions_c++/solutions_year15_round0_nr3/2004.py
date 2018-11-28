/*
* @Author: amber
* @Date:   2015-04-11 13:38:01
* @Last Modified by:   amber
* @Last Modified time: 2015-04-12 03:02:39
*/

#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

char array[10100];

const int quat[4][4] = {
	{'h', 'i', 'j', 'k'},
	{'i', -'h', 'k', -'j'},
	{'j', -'k', -'h', 'i'},
	{'k', 'j', -'i', -'h'}
};

std::vector<char> multi[2][4] = {
	{std::vector<char>(), std::vector<char>(), std::vector<char>(), std::vector<char>()},
	{std::vector<char>(), std::vector<char>(), std::vector<char>(), std::vector<char>()}
};

bool check(int L, int X, char* array, int position, char need, bool negative) {
	// cout << L << " " << X << " " << position << " " << need << endl;
	char res = 'h';
	bool res_neg = false;
	for(int i = position; i < (L * X); i++) {
		int array_pos = i % L;
		char tmp_res = quat[res - 'h'][array[array_pos] - 'h'];
		// cout << "tmp:" << (res_neg?"-":"+") << " # ";
		res_neg = !((tmp_res < 0) == res_neg);
		tmp_res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
		// cout
		// 	<< i << "# "
		// 	<< res << "# "
		// 	<< array[array_pos] << "# "
		// 	<< tmp_res << "# "
		// 	<< (res_neg?"-":"+")
		// 	<< endl;
		res = tmp_res;
		if ((res == need) && (! negative)) {
			if (res == 'j') {
				// check next whole as 'k'
				// cout << "short cut" << endl;
				char j_res = 'h';
				bool j_res_neg = false;
				for (int j = i+1; j < (L * X); ++j) {
					int array_pos = j % L;
					char tmp_res = quat[j_res - 'h'][array[array_pos] - 'h'];
					j_res_neg = !((tmp_res < 0) == j_res_neg);
					tmp_res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
					j_res = tmp_res;
				}
				if((j_res == 'k') && (! j_res_neg))
					return true;
				else
					continue;
			}
			if ((need == 'k') && (i == (L*X-1))) {
				// cout << "find" << endl;
				return true;
			}
			if(check(L, X, array, i+1, need + 1, res_neg))
				return true;
		}
	}
	return false;
}


bool check_try(int L, int X, char* array) {
	// cout << L << "#" << X << "#" << L * X << endl;
	// cout << array << endl;

	char res = 'h';
	bool res_neg = false;
	for(int i = 0; i < (L * X); i++) {
		int array_pos = i % L;
		char tmp_res = quat[res - 'h'][array[array_pos] - 'h'];
		// cout << "tmp:" << (res_neg?"-":"+") << " # ";
		res_neg = !((tmp_res < 0) == res_neg);
		tmp_res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
		// cout
		// 	<< i << "# "
		// 	<< res << "# "
		// 	<< array[array_pos] << "# "
		// 	<< tmp_res << "# "
		// 	<< (res_neg?"-":"+")
		// 	<< endl;
		res = tmp_res;
	}
	if (!((res == 'h') && res_neg)) {
		// all str is not -'h' -> -1
		// cout << "total not pass -1" << endl;
		return false;
	}

	// return true;


	// we find 'i' prefix string
	res = 'h';
	res_neg = false;
	int pos_i = -1;
	for(int i = 0; i < (L * X); i++) {
		int array_pos = i % L;
		char tmp_res = quat[res - 'h'][array[array_pos] - 'h'];
		res_neg = !((tmp_res < 0) == res_neg);
		res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
		// cout << i << ":" << array[array_pos] << endl;
		if ((res == 'i') && (!res_neg)) {
			pos_i = i;
			break;
		}
	}
	if (pos_i < 0)
		return false;
	// cout << "pos_i:" << pos_i << endl;

	res = 'h';
	res_neg = false;
	int pos_k = -1;
	for(int i = (L * X) - 1; i >= 0; i--) {
		int array_pos = i % L;
		char tmp_res = quat[array[array_pos] - 'h'][res - 'h'];
		res_neg = !((tmp_res < 0) == res_neg);
		res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
		// cout << i << ":" << array[array_pos] << endl;
		if ((res == 'k') && (!res_neg)) {
			pos_k = i;
			break;
		}
	}
	if (pos_k < 0)
		return false;

	// cout << pos_k << endl;

	if (pos_i >= pos_k) {
		// cout << "if (pos_i >= pos_k) fail" << endl;
		return false;
	} else
		// cout << "pass!!!!" << endl;

	res = 'h';
	res_neg = false;
	for(int i = pos_i + 1; i < pos_k; i++) {
		int array_pos = i % L;
		char tmp_res = quat[res - 'h'][array[array_pos] - 'h'];
		res_neg = !((tmp_res < 0) == res_neg);
		res = (tmp_res < 0) ? (- tmp_res) : tmp_res;
		// if ((res == 'j') && (!res_neg)) {
		// 	pos_k = i;
		// 	break;
		// }
	}
	// cout << pos_i << " " << pos_k << endl;
	// cout << res << " # " << res_neg << endl;
	// assert(((res == 'j') && (!res_neg)));

	return true;
}


int main(){
	int T;
	scanf("%d", &T);
	// cout << T << endl;

	// for (int i = 0; i < 4; ++i) {
	// 	for (int j = 0; j < 4; ++j)
	// 		cout << quat[i][j] << " ";
	// 	cout << endl;
	// }

	for (int i = 0; i < T; ++i) {
		int L, X;
		scanf("%d %d", &L, &X);
		scanf("%s", array);
		// cout << L << "#" << X << "#" << array << endl;
		// if(i != 3)
		// 	continue;
		//check(L, X, array, 0, 'i', false) ? printf("Case #%d: YES\n", i + 1) : printf("Case #%d: NO\n", i + 1);
		check_try(L, X, array) ? printf("Case #%d: YES\n", i + 1) : printf("Case #%d: NO\n", i + 1);
		// break;
	}

	return 0;
}