#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

bool find(string &S, string f){
	string temp = S;
	for (int i = 0; i < f.length(); i++){
		int pos = temp.find(f.at(i));
		if (pos == string::npos)
			return false;
		temp.erase(pos, 1);
	}
	
	S = temp;
	return true;
}

string intToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}

void sort(vector<int> &v){
	for (int i = 0; i < v.size(); i++){
		for (int j = i; j < v.size(); j++){
			if (v[i] > v[j]){
				int temp = v[i];
				v[i] = v[j];
				v[j] = temp;
			}
		}
	}
}


string solve(string S){
	string numbers[] = {"SIX", "TWO", "FOUR", "ZERO", "ONE", "THREE", "FIVE", "SEVEN", "EIGHT", "NINE"};
	int nums[] = {6, 2, 4, 0, 1, 3, 5, 7, 8, 9};
	int i = 0;
	vector<int> v;
	string result = "";
	
	while (S.length() > 0){
		if (find(S, numbers[i]))
			v.push_back(nums[i]);
		else
			i++;
	}
	
	sort(v);
	for (i = 0; i < v.size(); i++)
		result += intToString(v[i]);
	
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
					
			
			cout << "Case #" << n << ": " << solve(S) << "\n";
			output << "Case #" << n << ": " << solve(S) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
