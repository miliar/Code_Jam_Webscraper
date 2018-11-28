#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T, case_no = 1;
	cin >> T;
	cin.get();
	while(T--){
		string s; int count = 0;
		getline(cin, s);
		size_t n = s.size(); 
		while(n--){
			if(s[n] == '+') continue;
			else{
				for(size_t i = 0; i <= n; i++){
					if(s[i] == '+') s[i] = '-';
					else s[i] = '+';
				}
				count++;
			}
		}
		printf("Case #%d: %d\n", case_no++, count);
	}
    return 0;
}
