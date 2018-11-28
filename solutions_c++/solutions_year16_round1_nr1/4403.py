#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert> 
#include <set> 
#include <map>
#include <fstream> 
#include <string> 
#include <list> 

using namespace std;

ifstream fin("input.txt"); 

int main(){
	int t; fin >> t; 
	int total_t = t; 
	while(t--){
		string s; 
		fin >> s; 

		list<char> l; 
		l.push_front(s[0]); 
		for(int i = 1; i < s.size(); i++){
			if(s[i] >= l.front()){
				l.push_front(s[i]); 
			}
			else{
				l.push_back(s[i]); 
			}
		}
		cout << "Case #" << total_t - t << ": "; 
		for(list<char>::iterator itr = l.begin(); itr != l.end(); itr++){
			cout << *itr; 
		}
		cout << endl; 

	}

	return 0; 
}
