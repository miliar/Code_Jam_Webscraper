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

typedef unsigned long long ll;

bool ispal(unsigned long long s){
	SS ss;
	ss<<s;
	string temp = ss.str();
	return temp == string(temp.rbegin(),temp.rend());
}

vector<ll> get(unsigned long long a, unsigned long long b){
	vector<ll> final;
	ll min = round(sqrt(a));
	while(true){
		ll temp = min*min;
		if(temp>b)
			break;
		if(temp>=a && ispal(min) && ispal(temp)){
			final.push_back(temp);
		}
		min++;
	}
	return final;
}

int main(){
	int t;
	cin>>t;
	ll min = ULLONG_MAX;
	ll max = 0;
	vector< pair<ll,ll> > my;
	for(int i=1;i<=t;i++){
		unsigned long long a,b;
		cin>>a>>b;
		if(a<min)
			min = a;
		if(b>max)
			max=b;
		my.push_back(make_pair(a,b));
	}
	vector<ll> result = get(min,max);
	int loop=1;
	for(int i=0;i<my.size();i++){
		int currResult = 0;
		for(int j=0;j<result.size();j++)
			if(result[j]>= my[i].first && result[j]<=my[i].second)
				currResult++;
		cout<<"Case #"<<loop++<<": "<<currResult<<endl; 
	}
	return 0;
}