#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

bool is_palindrome(long long x){
	stringstream ss;
	ss << x;
	string num = ss.str();
	string rnum = num;
	reverse(rnum.begin(), rnum.end());
	return num == rnum;	
}


vector<long long> fairs;
void pre(){
	long long x = 1;
	while(x * x <= 100000000000000ll){
		if(is_palindrome(x) && is_palindrome(x * x)) { 
			//cout << x * x << endl;
			fairs.push_back(x * x);
		}	
		x++;	
	}
}

int main(){
	int T;
	long long A, B;

	pre();
	
	cin >> T;
		
	for(int t = 1; t <= T; t++){
		cin >> A >> B;
		
		int ans = upper_bound(fairs.begin(), fairs.end(), B) - lower_bound(fairs.begin(), fairs.end(), A);
		
		cout << "Case #" << t << ": " << ans << "\n";
	}
}
