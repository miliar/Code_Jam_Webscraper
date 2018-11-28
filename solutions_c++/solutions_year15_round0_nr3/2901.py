/*
 * dijkstra.cc
 *
 *  Created on: Apr 11, 2015
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct quaternion{
	int sign;
	char c;
};

quaternion multiply(quaternion q1, quaternion q2){

	quaternion q;

	if ((q1.c == '1') && (q2.c == 'i')){
		q.c = 'i';
		q.sign = 1;
	} else if ((q1.c == '1') && (q2.c == 'j')){
		q.c = 'j';
		q.sign = 1;
	} else if ((q1.c == '1') && (q2.c == 'k')){
		q.c = 'k';
		q.sign = 1;
	} else if ((q1.c == '1') && (q2.c == '1')){
		q.c = '1';
		q.sign = 1;
	} else if ((q1.c == 'i') && (q2.c == '1')){
		q.c = 'i';
		q.sign = 1;
	} else if ((q1.c == 'i') && (q2.c == 'i')){
		q.c = '1';
		q.sign = -1;
	} else if ((q1.c == 'i') && (q2.c == 'j')){
		q.c = 'k';
		q.sign = 1;
	} else if ((q1.c == 'i') && (q2.c == 'k')){
		q.c = 'j';
		q.sign = -1;
	} else if ((q1.c == 'j') && (q2.c == '1')){
		q.c = 'j';
		q.sign = 1;
	} else if ((q1.c == 'j') && (q2.c == 'i')){
		q.c = 'k';
		q.sign = -1;
	} else if ((q1.c == 'j') && (q2.c == 'j')){
		q.c = '1';
		q.sign = -1;
	} else if ((q1.c == 'j') && (q2.c == 'k')){
		q.c = 'i';
		q.sign = 1;
	} else if ((q1.c == 'k') && (q2.c == '1')){
		q.c = 'k';
		q.sign = 1;
	} else if ((q1.c == 'k') && (q2.c == 'i')){
		q.c = 'j';
		q.sign = 1;
	} else if ((q1.c == 'k') && (q2.c == 'j')){
		q.c = 'i';
		q.sign = -1;
	} else if ((q1.c == 'k') && (q2.c == 'k')){
		q.c = '1';
		q.sign = -1;
	}

	q.sign = q.sign * q1.sign * q2.sign;
	return q;

}

int main(int argc,char *argv[]){

	int N;
	int len, mult;
	string s,to_reduce;
	ifstream fs(argv[1]);
	vector<quaternion> pre_product, post_product;
	bool found;
	int k,l,l0;

	getline(fs, s);
	istringstream(s) >> N;
	for(int i = 0; i < N; i++){

		cout << "Case #" << i+1 << ": ";
		getline(fs, s);
		istringstream(s) >> len >> mult;

		getline(fs, s);
		to_reduce.erase();
		for(int j = 0; j < mult; j++)
			to_reduce.append(s);

		quaternion q,q1;
		q.sign = 1;
		q.c = '1';
		pre_product.clear();
		pre_product.resize(to_reduce.length());
		for(int j = 0; j < to_reduce.length(); j++){
			q1.c = to_reduce[j];
			q1.sign = 1;
			q = multiply(q,q1);
			pre_product[j] = q;
		}


		q.sign = 1;
		q.c = '1';
		post_product.clear();
		post_product.resize(to_reduce.length());
		for(int j = to_reduce.length()-1; j >= 0; j--){
			q1.c = to_reduce[j];
			q1.sign = 1;
			q = multiply(q1,q);
			post_product[j] = q;
		}


		if (to_reduce.length() < 3)
			cout << "NO" << endl;
		else{
			k = 0;
			l = 2;
			l0 = k+1;
			q.sign = 1;
			q.c = '1';
			found = false;
			while(k <= to_reduce.length() - 3){
				if (pre_product[k].c == 'i' && post_product[l].c == 'k'){
					// cout << "jest" << k << " " << l << endl;
					for(int j = l0; j < l; j++){
						q1.c = to_reduce[j];
						q1.sign = 1;
						q = multiply(q,q1);
					}
					if (q.c == 'j' && pre_product[k].sign*q.sign*post_product[l].sign == 1){
						found = true;
						break;
					}
					l0 = l;
				}
				if (l < to_reduce.length() - 1){
					l++;
				}
				else{
					k++;
					l0 = k+1;
					l = k + 2;
					q.sign = 1;
					q.c = '1';
				}
			}

				if (found) cout << "YES" << endl;
				else cout << "NO" << endl;
			}
	}

}
