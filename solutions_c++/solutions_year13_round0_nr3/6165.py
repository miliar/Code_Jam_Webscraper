#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <utility>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cassert>
#include <algorithm>
#define debug(x) cerr<<#x<<"="<<(x)<<endl
#define ISS istringstream
#define _USE_MATH_DEFINES
#define SS stringstream

using namespace std;

bool ispal(unsigned long long s){
	SS ss;
	ss<<s;
	string temp = ss.str();
	return temp == string(temp.rbegin(),temp.rend());
}

unsigned long long get(unsigned long long a, unsigned long long b){
	unsigned long long result =0;
	unsigned long long min = round(sqrt(a));
	while(true){
		unsigned long long temp = min*min;
		if(temp>b)
			break;
		if(temp>=a && ispal(min) && ispal(temp)){
			result++;
		}
		min++;
	}
	return result;
}

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		unsigned long long a,b;
		cin>>a>>b;
		cout<<"Case #"<<i<<": "<<get(a,b)<<endl;
	}
	return 0;
}