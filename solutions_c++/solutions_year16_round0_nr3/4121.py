#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream> 
#include <string> 
#include <list> 

using namespace std;
int divisor = 0; 

bool is_prime(long long n){
	long long limit = (long long int)sqrt(n*1.0); 
	for(int i = 2; i <= limit; i++){
		if((n % i) == 0){ divisor = i; return false; }
	}
	return true; 
}

long long convert(string& s, int base){
	long long k = 0; 
	int curr_power = 0; 
	for(int i = s.size()-1; i >= 0; i--){
		int val = (s[i] - '0'); 
		if(val == 0){ curr_power ++; continue; }
		k = k + (val * (long long)pow(base*1.0, curr_power)); 
		curr_power ++; 
	}
	return k; 
}

string int_to_bin(long long int n){
	string ans; 
	if(n == 0){ ans = "0"; return ans; }
	while(n != 0){
		int r = n % 2; 
		ans.push_back(r + '0'); 
		n /= 2; 
	}
	reverse(ans.begin(), ans.end()); 
	return ans;
}

string make_jamcoin_of_given_length(string& s, int size){
	if(s.size()+2 > size) return string(); 

	string ans; ans.push_back('1'); 
	int length = s.size(); 

	for(int i = 0; i < size - 2 - length; i++){
		ans.push_back('0'); 
	}
	for(int i = 0; i < s.size(); i++) ans.push_back(s[i]); 
	ans.push_back('1'); 

	return ans; 
}

int main(){
	ifstream cin("input.txt"); 
	int t; cin >> t; 
	int total_cases   = t; 

	string s = "1001"; 

	//cout << make_jamcoin_of_given_length(string("11"), 5) << endl; 

	/*for(int i = 2; i <= 10; i++){
		long long int val = convert(s, i); 
		cout << val; 
		if(is_prime(val)) cout << " prime" << endl; else cout << " not prime " << endl; 
	}
	return 0; */

	while(t--){
		int n, j; cin >> n >> j; 
		cout << "Case #" << total_cases-t << ":" << endl; 

		int jamcoin_counter = 0; 
		int curr_val = 0; 
		vector<int> l; 

		while(1){
			if(jamcoin_counter == j) break; 

			//cout << "curr_val: " << curr_val << endl; 

			string s1 = int_to_bin(curr_val); 
			string s2 = make_jamcoin_of_given_length(s1, n); 
			//cout << "s2: " << s2 << endl; 

			for(int base = 2; base <= 10; base++){
				long long int val = convert(s2, base); 
				//cout << "base: " << base << " val: " << val << endl; 

				bool flag = is_prime(val); 
				if(flag == false){
					l.push_back(divisor); 
				}
				else{
					/* One of the interpretation with a base between 2 and 10 is not prime. */
					//cout << base << " --> prime" << endl; 
					l.clear(); 
					break; 
				}
			}
			if(l.size() == 9){
				jamcoin_counter ++; 
				cout << s2 << " "; 
				for(int i = 0; i < l.size(); i++) cout << l[i] << " "; cout << endl; 
				l.clear(); 
			}

			curr_val ++; 
		}
		

	}
	
		
	
	return 0; 
}
