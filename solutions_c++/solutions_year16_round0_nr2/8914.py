#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <set>
#include <string>

using namespace std;

bool check(string s){
	for(int i = 0; i < s.size(); i++){
		if(s[i] == '-')
			return false;
	}
	return true;
}

int main() {
	
    int t;
    cin >> t;
    assert(t >= 1 && t <= 100);
    
    for( int j = 0; j < t; j++){
	
		string s;
        cin >> s;
        if(!(s.size() >= 1 && s.size() <= 100))
			continue;
		
		int n = 0;
		while(check(s) != true){
			char start = s[0];
			int p = 1;
			for(int i = 1; i < s.size(); i++){
				if(s[i] == start)
					p++;
				else
					break;
			}
			if(start == '-'){
				for(int i = 0; i < p; i++){
					s[i] = '+';
				}
			}
			if(start == '+'){
				for(int i = 0; i < p; i++){
					s[i] = '-';
				}
			}
			n++;
		}
				
		cout << "Case #" << j + 1 << ": " << n << endl;
		
	}
	
}