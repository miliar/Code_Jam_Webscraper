#include <iostream>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <algorithm>
#include <queue>
#include <functional>
#include <fstream>
#include <iomanip>
#include <cstdio>
#define esp 1e-6
using namespace std;
typedef unsigned int uint;
typedef long long ll;

const ll p = 1000000007;
const ll k = 500000004;

inline int Max(int a, int b){
	return a>b?a:b;
}
inline int Min(int a, int b){
	return a<b?a:b;
}

int main(){
	ifstream in;
	in.open("A-small-attempt0.in");
	ofstream out;
	out.open("out.txt");
	int test;
	in>>test;
	for(int t = 1; t <= test; t++){
		int first[4][4], second[4][4];
		int one,two;
		in>>one;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				in>>first[i][j];
			}
		}
		in>>two;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				in>>second[i][j];
			}
		}
		int count = 0;
		int num;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(first[one-1][i] == second[two-1][j]){
					count++;
					num = first[one-1][i];
				}
			}
		}
		if(0 == count)
			out<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		else if(1 == count)
			out<<"Case #"<<t<<": "<<num<<endl;
		else
			out<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}
