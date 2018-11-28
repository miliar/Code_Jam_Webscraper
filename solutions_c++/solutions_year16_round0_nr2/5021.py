#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream> 
#include <string> 

using namespace std;

bool all_happy(string& s){
	for(int i = 0; i < s.size(); i++){
		if(s[i] == '-') return false; 
	}
	return true; 
}

int find_first_difference(string& s){
	char k = s[0]; 
	int i = 0; 
	for(i = 1; i < s.size(); i++){
		if(s[i] != k) return i-1; 
	}
	return i; 
}

string flip(string& s, int n){
	string s_new; 
	for(int i = n; i >= 0; i--){
		if(s[i] == '-') s_new.push_back('+'); 
		else            s_new.push_back('-'); 
	}
	for(int i = n+1; i < s.size(); i++){
		s_new.push_back(s[i]); 
	}
	return s_new; 
}

int main(){
	ifstream cin("input.txt"); 
	int t; cin >> t; 
	int total_cases   = t; 

	while(t--){
		string s; cin >> s; 
		int counter = 0; 

		while(1){
			if(all_happy(s)){
				cout << "Case #" << total_cases-t << ": " << counter << endl; 
				break; 
			}
			int k = find_first_difference(s); 
			//cout << "k: " << k << endl; 

			if(k == s.size()){
				counter++; 
				cout << "Case #" << total_cases-t << ": " << counter << endl; 
				break; 
			}
			
			string s_new = flip(s, k); 
			counter++; 
			//cout << "s_new: " << s_new << endl; 
			s = s_new; 
		}
	}
	
	return 0; 
}
