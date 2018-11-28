#include <iostream> 
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <time.h>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
using namespace std;

void fn();

int
main(){
	srand(time(NULL));
	int nTest; 

	cin >> nTest;

	for(int i = 1; i <= nTest; i++){
		cout << "Case #" << i << ": ";
		fn();
	}

	return 0;
}

vector <pair <char, int>> decompose(string s){
	vector <pair <char, int>> ans;

	int count = 0;
	char c = '\0';
	while (!s.empty()){
		c = s[0]; 
		count++;
		s.erase(0, 1);

		if (s.empty() || s[0] != c){
			ans.push_back(pair <char,int>(c, count));
			count = 0;
		}
	}

	return ans;
}

void fn(){
	int N; // Number of Strings

	cin >> N;

	vector <vector <pair<char, int>>> sets;

	// Read strings
	for(int i = 0; i < N; i++){
		string temp; 

		cin >> temp; 

		// Decompose
		sets.push_back(decompose(temp));
	}

	// Check Equality of Size and Chars
	int size = sets[0].size();
	for(int i = 0; i < sets.size(); i++){
		if(sets[i].size() != size){
			cout << "Fegla Won\n";
			return;
		}
	}
	for(int i = 0; i < sets[0].size(); i++){
		char c = sets[0][i].first;
		for(int j = 0; j < sets.size(); j++){
			if(sets[j][i].first != c){
				cout << "Fegla Won\n";
				return;
			}
		}
	}

	// Start computing
	int moves = 0;
	for(int i = 0; i < sets[0].size(); i++){
		int target = 0; 

		// Calculate target value
		for(int j = 0; j < sets.size(); j++){
			target += sets[j][i].second;
		}
		target = (double) target / (double) sets.size();

		// Calculate moves 
		for(int j = 0; j < sets.size(); j++){
			moves += abs(sets[j][i].second - target);
		}
	}
	
	cout << moves << endl;

	return;
}
