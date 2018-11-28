#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
constexpr long long square(long long x){return x*x;}
constexpr long long pow(long long a, long long b){return b == 0 ? 1 : b % 2 ==  0 ? square(pow(a,b/2)) : a*square(pow(a,b/2));}
void printVector(const vector<int>& v){for (int q : v) {cout << q << " ";} cout << endl;}
__attribute__ ((const, hot)) int number_in_base(const vector<int>& v, const int base){
	int acc = 1;
	int sum = 0;
	for (int i = -1+v.size(); i >= 0; i -= 1){
		sum += v[i]*acc;
		acc *= base;
	}
	return sum;
}
int main(void){
long long t, K, C, S;
cin >> t;
for (long long i = 1; i <= t; i +=1 ){
	cin >> K >> C >> S;
	cout << "Case #" << i << ":";
	for (long long q = 0; q < K; q +=1){
		/*long long acc = 1;
		for (long long j = 0; j < C; j+=1 ){
			acc += q*pow(K, j);
		}*/
		cout << " " << 1+q; //acc;
	}
	cout << "\n";
}
return 0;
}
