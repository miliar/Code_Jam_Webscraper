#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <iomanip>

#define S               second
#define pi  		2 * acos(0.0)
#define sz(a)   	int((a).size()) 
#define pb 		push_back 
#define tr(c,i) 	for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) 	(find(all(c),x) != (c).end()) 

using namespace std;
bool con(char a){
	if(a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') return false;
	return true;
}

int main(){
	int t, cs = 0;string s;int n;
	cin >> t;
	while(t--){cs++;//cout << "Case #" <<cs <<": Draw" << endl;
		cin >> s;cin >> n;
		long long int ans = 0;
		int len = s.length();
		int c = 0;long long st = 0, a = 0, b = 0, d = 0;
		for(int i = 0; i < len; i++){
			if(con(s[i]) == true){
				c++;
				if(c >= n){
					b = len - i;
					a = i - n;
					a++;
					 d = a-st;
					d++;
					ans += d*b;
					st = i-n;
					st += 2;c--;
				}
				continue;
			}
			c  = 0;
		}
		cout << "Case #" <<cs <<": " <<ans << endl;
	}
        
	return 0;
}

