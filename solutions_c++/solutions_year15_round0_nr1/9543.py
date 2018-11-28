#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("A-large-attempt0.in");
ofstream fout("p1out.txt");

int T;
int solveCase(int S, string audience){
	int shyCount[1002] = { 0 };
	int shyAggregate[1002] = { 0 };
	for (int i = audience.length(); i--;){
		shyCount[i] = audience[i] - '0';
	}
	shyAggregate[0] = shyCount[0];
	for (int i = 1; i <= S; i++){
		shyAggregate[i] = shyAggregate[i - 1] + shyCount[i];
	}
	int peopleNeeded = 0;
	for (int i = 1; i <= S; i++){
		int clappers = shyAggregate[i - 1] + peopleNeeded;
		if (clappers < i){
			peopleNeeded += i - clappers;
		}
	}

	return peopleNeeded;
}
int main(){
	fin >> T;
	for (int i = 0; i < T; i++){
		int S; 
		string aud;
		fin >> S >> aud;
		fout << "Case #" << i+1 << ": " << solveCase(S, aud) << endl;
	}
	fin >> T;
	return 0;
}