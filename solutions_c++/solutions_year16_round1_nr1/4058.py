#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
	
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int n;
	fin >> n;
	
	
	for(int o = 0; o < n; o++){
		
		string input;
		fin >> input;
		string result = "";
		result += input[0];
		
		
		for(int i = 1; i < input.length(); i++){
			
			if(input[i] >= result[0]){
				result = input[i] + result;
				
			}
			else{
				result += input[i];
			}
			
		}
		fout << "Case #" << o+1 << ": " << result << endl;
		
	}
	return 0;
	
}
