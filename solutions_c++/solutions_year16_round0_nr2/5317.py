#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;

bool allTruth(const vector<bool>& v){
	for(bool value : v){
		if(!value){
			return false;
		}
	}
	return true;
}

int main() {
	int t = 0;
	cin >> t;
	for(int tIndex = 1; tIndex <= t; tIndex++){
		string pancakes;
		cin>>pancakes;
		int changes = 0;
		for(int i = 1; i < pancakes.length(); ++i){
			if(pancakes[i-1] != pancakes[i]){
				changes++;
			}
		}
		if(pancakes.back() == '-'){
			changes++;
		}
		cout<<"Case #"<<tIndex<<": "<<changes<<endl;
	}
}
