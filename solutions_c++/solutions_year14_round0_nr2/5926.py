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
		double c,f,x;
		in>>c>>f>>x;
		double rate = 2;
		double time = 0;
		while(x/rate > c/rate + x/(rate+f)){
			time += c/rate;
			rate += f;
		}
		time += x/rate;
		out<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<time<<endl;
	}
	return 0;
}
