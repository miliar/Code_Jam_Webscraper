#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <math.h>
using namespace std;

int t;
int n;

int main(void){
	cin >> t;
	for(int i = 0;i < t;i++){
		cin >> n;
		int h[1000] = {};
		vector<int> nothing;
		for(int j = 0;j < (2*n-1)*n;j++){
			int a;
			cin >> a;
			h[a]++;
		}
		for(int j = 0;j < 1000;j++){
			if(h[j]%2 != 0){
				nothing.push_back(j);
			}
		}
		sort(nothing.begin(), nothing.end());
		cout << "Case #" << i+1 << ":";
		for(int j = 0;j < nothing.size();j++){
			cout << " " << nothing[j];
		}
		cout << endl;
	}
	return 0;
}
