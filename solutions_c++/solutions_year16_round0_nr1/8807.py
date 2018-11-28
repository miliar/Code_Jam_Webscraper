#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

int main() {
	
    int t;
    cin >> t;
    assert(t >= 1 && t <= 100);
    
    for( int j = 0; j < t; j++){
	
		int n;
        cin >> n;
        if(!(n >= 0 && n <= 1000000))
			continue;
		
		else if(n == 0){
		cout << "Case #" << j + 1 << ": " << "INSOMNIA" << endl;
		continue;
		}
		set<int> s;
		
		int tempo = n;
		while(s.size() < 10){
			int temp = n;
			
			int r;
			while(temp > 0){
				r = temp % 10;
				temp = temp / 10;
				s.insert(r);
			}
			
			n += tempo;
		}
		
		n -= tempo;
		
		cout << "Case #" << j + 1 << ": " << n << endl;
		
	}
	
}