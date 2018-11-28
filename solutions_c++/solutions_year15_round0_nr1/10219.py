#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <fstream>
#include <map>
using namespace std;

void getLine(std::fstream& in, std::string& line, std::istringstream& iss){
	iss.clear();
	getline(in, line);
	iss.str(line);
}

long long T, Sm; 

int main(){
	freopen("output.txt", "w", stdout);
	std::fstream in("input.txt");
	std::istringstream iss;
	std::string line;
	std::string delimiter = " ";
	
	getLine(in, line, iss);
	iss >> T;
	int pos = 0;
	for(int i = 1; i <= T; i++){
		getLine(in, line, iss);
		iss >> Sm;
		pos = line.find(delimiter);
		line = line.substr(pos+1, string::npos);
		
		int sum = 0;
		int min = 0;
		for(int k = 0; k < line.size() ;k++){
			if (static_cast<int>(line[k])-48 == 0)
				continue;
				
			if( sum < k ){
				min += k - sum;
				sum += min;
			}
			sum += static_cast<int>(line[k])-48;
		}
		
		cout << "Case #" <<i <<": "<< min<<endl;
		sum = 0;
		min = 0;
	}
	
	return 1;
}