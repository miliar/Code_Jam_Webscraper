// Brute force for 10p!

#include <math.h>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm> 
#include <sstream>



using namespace std;

int min(int a, int b) {
	if (a < b) 
		return a;
		
	return b;
}

int ops(unsigned long long& cur, vector< int >* motes, int counter) {	
	
		
	while (motes->back() < cur) {
		
		cur += motes->back();
		motes->pop_back();
	}
		
	if (motes->empty()) {
		
		return counter;
	}
	
	if (motes->back() < 2*cur - 1) {
		
		cur = cur + (cur - 1);
		return ops(cur, motes, counter + 1);
	} else {
		if (cur == 1) 
			return counter + (motes->size());
		
		int stl = motes->size();
		cur = cur + (cur - 1);
		int derp =  ops(cur, motes, counter + 1);
		
		return min(counter + stl, derp);
	}	
}

bool after(int a, int b) {
	return a > b;
}

int main(){
	int cases, tmp, n;
	vector< int > motes;	
	unsigned long long cur;	
	
	cin >> cases;
	
	for (int i=1; i<= cases; i++) {
		cin >> cur >> n;
		for (int j=0; j<n; j++) {
			cin >> tmp;
			motes.push_back(tmp);
		}
		sort(motes.begin(), motes.end(), after);				
		cout <<"Case #" << i<<": " << ops(cur, &motes, 0) << endl;
		motes.clear();
	}

	return 0;
	
}
	
	
