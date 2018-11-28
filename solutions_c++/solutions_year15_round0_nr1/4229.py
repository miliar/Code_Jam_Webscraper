#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(){

	int CASE = 1;
	int T ;
	cin >> T;
	while(T--){
		int s_max;
		string digit;
		
		cin >> s_max >> digit;
		int sum = digit[0] - '0';
		int ans = 0;
		for(int i = 1; i <= s_max; ++i){
			if( digit[i] == '0')	continue;
			else{
				int cur = digit[i] - '0';
				if( sum < i ){
					ans = ans + (i - sum);
					sum = sum + (i - sum);
				}
				sum = sum + cur;	
			}
		}
		cout << "Case #" << CASE++ << ": " << ans << endl;
	}

	return 0;
}
