#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<int> vector_from_one_line(string line){
	vector<int> v; 
	stringstream ss(line);
	string s;
	getline(ss, s, ' ');
	string s_v;
	getline(ss, s_v, ' ');
	for(int i = 0 ; i<=stoi(s); i++){
		int curr = s_v[i] - '0';
		v.push_back(curr);
	}
	return v;
}

int solve(vector<int> &v){
	int max = v.size();
	int count = 0;
	int standing = 0;
	int curr = 0;	
	for(int i = 0; i < max; i++){
		if(v[i]==0){
			continue;
		}
		while(standing<i){
			count++;
			standing++;
		}
		standing+=v[i];
	}

	return count;
}


void ovation_main(int cases, ifstream &f){
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
	ifstream f("large.in");
	string line;
	if(f.is_open()){
		getline(f,line);
		int cases = stoi(line);		
		ovation_main(cases, f);
		f.close();
	}
	return 0;
}