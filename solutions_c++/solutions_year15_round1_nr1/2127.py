#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int firstmethod(const vector<int>& buffer) {
	int ret = 0;
	int prev = 0;
	
	for(int i = 0; i < buffer.size(); ++i) {
		if(buffer[i] < prev) ret += (prev - buffer[i]);
		prev = buffer[i];
	}
	return ret;
}

int secondmethod(const vector<int>& buffer) {
	int prev = 0;
	int maximum = -1;
	for(int i = 0; i < buffer.size(); ++i) {
	
		maximum = max(maximum, prev - buffer[i]);
		prev = buffer[i];
	}
//	maximum =  ceil(float(maximum) / 10.0);

	int ret = 0;
	for(int i = 0; i < buffer.size() - 1; ++i) {
		if(buffer[i] <= maximum) ret += buffer[i];
		else ret += (maximum );
	}
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; ++i) {
		vector<int> buffer;
		int n;
		cin >> n;
		for(int c = 0; c < n; ++c) {
			int elem;
			cin >> elem;
			buffer.push_back(elem);
		}
		cout << "Case #" << i+1 << ": " << firstmethod(buffer) << " " <<  secondmethod(buffer)<< endl;
	}
	return 0;
}