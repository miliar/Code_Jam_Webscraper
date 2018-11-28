#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string.h>
#include <vector>

using namespace std;

void print(vector<int> v){
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}

vector<int> translate(string s){
	vector<int> v;
	
	for (int i = 0; i < s.length(); i++){
		if (s[i] == '-')
			v.push_back(0);
		else
			v.push_back(1);
	}
	
	return v;
}

vector<int> trim(vector<int> v){
	while (v.size() > 0 && v[v.size() - 1] == 1)
		v.pop_back();
	
	return v;
}

int flipTop(vector<int> &v){
	int temp = 0;
	while (v[temp] == 1 && temp < v.size()){
		v[temp] = 0;
		temp++;
	}
	
	return temp;
}

vector<int> flipAll(vector<int> v){
	vector<int> temp;
	
	while (v.size() > 0){
		if (v.back() == 0)
			temp.push_back(1);
		else
			temp.push_back(0);
		
		v.pop_back();
	}
	
	return temp;
}

int flipThem(vector<int> v)
{
	int flip = 0;
	
	while(1){	
		v = trim(v);
		if (v.size() == 0)
			break;
	
		if (flipTop(v) > 0)
			flip++;
	
		v = trim(flipAll(v));
		flip++;
	}
		
	return flip;
}



int main() {	
	ifstream input("B-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
		
			string stack;
			int flips = -1;
			input >> stack;
			
			vector<int> v = translate(stack);
			
			cout << "Case #" << n << ": " << flipThem(translate(stack)) << "\n";
			output << "Case #" << n << ": " << flipThem(translate(stack)) << "\n";
			
		
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
