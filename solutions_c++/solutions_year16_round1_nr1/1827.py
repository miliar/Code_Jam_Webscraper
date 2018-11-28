#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

void print(vector<int> v){
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}

string solve(string S){
	string result = "";
	result = result + S.at(0);
	
	
	for (int i = 1; i < S.length(); i++)
		if (S.at(i) >= result.at(0))
			result = S.at(i) + result;
		else
			result = result + S.at(i);
	
	return result;
}


int main() {	
	ifstream input("A-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			string S;
			input >> S;
					
			
			//cout << "Case #" << n << ": " << solve(S) << "\n";
			output << "Case #" << n << ": " << solve(S) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
