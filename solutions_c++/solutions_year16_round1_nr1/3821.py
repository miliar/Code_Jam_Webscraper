#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <string>

using namespace std;

int main() {
	
    int t;
    cin >> t;
    assert(t >= 1 && t <= 100);
    
    for( int j = 0; j < t; j++){
	
		string s;
        cin >> s;
		int n = s.size();
        assert(n >= 1 && n <= 1000);
		
		string temp = "";
		temp += s[0];
		for(int i = 1; i < n; i++){
			if(s[i] < temp[0]){
				temp.push_back(s[i]);
			}
			else if ( s[i] >= temp[0]){
				temp.insert(0, 1, s[i]);
			}
		}
		
		cout << "Case #" << j + 1 << ": " << temp << endl;

	}
	
}