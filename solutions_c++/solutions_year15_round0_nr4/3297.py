#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<int> vector_from_one_line(string line){
	vector<int> v; 
	stringstream ss(line);
	string each;
	while(getline(ss, each, ' ')){
		v.push_back(stoi(each));
	}
	return v;
}

string solve(vector<int> &v){
	int X = v[0];
	int R = v[1];
	int C = v[2];
	int size = R*C;
	if(size == X){
		if(size == 1 || size == 2){
			return "GABRIEL";
		}
		else{
			return "RICHARD";
		}
	}
	if(size % X == 0){
		if(X > 2){
			if(R == 1 || C == 1){
				return "RICHARD";
			}
			if(X>3 && X>=size/2){
				return "RICHARD";
			}
		}
		if(X > 3){
			if(R == 2 || C ==2){
				return "RICHARD";				
			}
		}
		return "GABRIEL";
	}
	else{
		return "RICHARD";
	}
}


void ominous_main(int cases, ifstream &f){
	vector<int> v;
	for(int i = 0; i<cases; i++){
		string line;
		getline(f,line);
		v.clear();
		v = vector_from_one_line(line);
		cout<< "Case #"<< i+1 << ": " << solve(v) << endl;
	}
}

int main(){
	ifstream f("5.in");
	string line;
	if(f.is_open()){
		getline(f,line);
		int cases = stoi(line);		
		ominous_main(cases, f);
		f.close();
	}
	return 0;
}