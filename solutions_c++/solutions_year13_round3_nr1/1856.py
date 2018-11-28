#include <fstream>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

//priority_

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("Atestoutput.txt");

	int T;
	fin >> T;
	for(int t=1 ; t<=T ; t++){
		string str;
		fin >> str;
		int N, length, ans=0;
		fin >> N;
		length = str.length();
		int *u = new int[length];
		int *v = new int[length];
		for(int i=0 ; i<length ; i++){
			u[i] = 0;
			v[i] = 0;
		}
		if(str.at(0) != 'a'&& str.at(0) != 'i' && str.at(0) != 'e' && str.at(0) != 'o' && str.at(0) != 'u'){
			u[0]++;
		}
		if(u[0]==N){
			v[0] = 1;
		}
		for(int i=1 ; i<length ; i++){
			if(str.at(i) != 'a'&& str.at(i) != 'i' && str.at(i) != 'e' && str.at(i) != 'o' && str.at(i) != 'u'){
				u[i]+= (u[i-1]==N)? N : u[i-1]+1;
			}
			if(u[i] == N){
				v[i] = i-N+2;
			}else{
				v[i] = v[i-1];
			}
		}

		for(int i=0 ; i<length ; i++){
			ans += v[i];
		}
		fout << "Case #" << t << ": " << ans << endl;
	}
}