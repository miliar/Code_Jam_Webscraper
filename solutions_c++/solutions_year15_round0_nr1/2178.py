#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(){
 	int T;
 	cin >> T;
 	freopen("a.out","wt",stdout);
 	for (int I = 0; I < T; I++) {       
 		int smax;
		string s;
		cin >> smax >> s;
		int up = s[0]-'0';
		int inv = 0;
		for(int i = 1; i <= smax; i++) {
			if(up < i) {
				inv += i - up;
				up += i - up;	      			
		 	}	
			up += s[i]-'0';
		}

 		cout << "Case #" << I+1 << ": ";
 		cout << inv << '\n';
 	}
 	return 0;
}