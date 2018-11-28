#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

vector<bool> nums(10);

void clear(){
	for(int i = 0; i < 10; i++) nums[i] = false;
}

bool check(){
	for(int i = 0; i < 10; i++){
		if(!nums[i]) return false;
	}
	return true;
}

void make(long long now){
	stringstream ss;
	ss << now;
	string s = ss.str();
	
	for(int i = 0; i < s.length(); i++){
		int index = s[i] - '0';
		nums[index] = true;
	}
}

int solve(int T){
	long long n, now; cin >> n;
	cout << "Case #" << T << ": ";
	
	if(n == 0){
		cout << "INSOMNIA" << endl;
		return 1;
	}
	
	clear();
	
	for(long long i = 1; true;i++){
		now = n * i;
		
		make(now);
		
		if(check()){
			cout << now << endl;
			return 0;
		}
	}
}

int main() {
	int T; cin >> T;
	
	for(int i = 1; i <= T; i++) solve(i);
	
	return 0;
}
