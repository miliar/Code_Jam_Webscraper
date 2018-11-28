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

vector<int> translate(long N){
	vector<int> v;
	
	do{
		v.insert(v.begin(), N % 10);
		N /= 10;
	}
	while (N > 0);
	
	return v;
}

vector<int> addVectors(vector<int> v1, vector<int> v2){
	if (v1.size() < v2.size())
		v1.swap(v2);
		
	v1.insert(v1.begin(), 0); 
	while (v2.size() < v1.size())
		v2.insert(v2.begin(), 0); 	
	
	int temp = 0;
	for (int i = v1.size() - 1; i >= 0 ; i--){
		temp += v1[i] + v2[i];
		v1[i] = temp % 10;
		temp /= 10;
	}
	
	while (v1.size() > 1 && v1[0] == 0)
		v1.erase(v1.begin());
	
	return v1;
}

void countDigits(vector<int> v1, vector<int> &d){
	for (int i = 0; i < v1.size(); i++)
		d[v1[i]]++;
}

bool areAllDigitsThere(vector<int> &d){
	for (int i = 0; i < d.size(); i++)
		if (d[i] == 0)
			return false;
			
	return true;
}

string toString(vector<int> v){
	string result = "";
	for (int i = 0; i < v.size(); i++){
		result = result + char(v[i] + 48);
	}
	return result;
}

string solve(long N){
	if (N == 0)
		return "INSOMNIA";
	
	vector<int> v1, v2;
	vector<int> d(10, 0);
	int steps = 0;
	
	v1 = translate(N);
	while (!areAllDigitsThere(d)){
		v2 = addVectors(v1, v2);
		countDigits(v2, d);
		steps++;
	}
			
	string result = "";
	for (int i = 0; i < v2.size(); i++){
		result = result + char(v2[i] + 48);
	}
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
			long N;
			input >> N;
					
			
			cout << "Case #" << n << ": " << solve(N) << "\n";
			output << "Case #" << n << ": " << solve(N) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
