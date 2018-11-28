#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

void printVector(const vector<int>& v){
for (int q : v) cout << q;
cout << endl;
	}

void flip(vector<int>& v, const int k){
	//cout << "before flip of k " << k << endl;
	//printVector(v);
	vector<int> w = v;
	for (int q = 0; q <= k; q +=1){
		w[q] = -v[k-q];
		}
	v = w;
	//cout << "after flip" << endl;
	//printVector(v);
}
void reduce(vector<int>& v){
while (v.size() > 0 and v[v.size()-1] == 1){
v.pop_back();
}
}
int countPositive(const vector<int>& v){
int k = 0;
while (k < (int)v.size()){
if (v[k] != 1) break;
k += 1;
}
return k;
}
__attribute__ ((const, hot)) int calc(vector<int> v){
//printVector(v);
reduce(v);
if (0 == v.size()){
return 0;
}
int cP = countPositive(v);
//cout << "cP is " << cP << endl;
if (0 == cP){
flip(v, v.size()-1);
return 1 + calc(v);
}
flip(v, cP-1);
flip(v, v.size()-1);
return 2 + calc(v);
}

const bool test = false;
int main(void){
int t;
cin >> t;
cin.ignore();
for (int i = 1; i <= t; i += 1){
vector<int> v;
for( char mander = cin.get(); mander != '\n'; mander = cin.get()){
	v.push_back(mander == '+' ? 1 : -1 );
}
//printVector(v);
cout << "Case #" << i << ": " << calc(v) << "\n";
}
return 0;
}
