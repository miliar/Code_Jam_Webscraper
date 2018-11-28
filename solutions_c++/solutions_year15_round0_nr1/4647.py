#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int toint(char a){
	return int(a)-48;
}

int solve(int a, string b){
	int tot = toint(b[0]), add = 0;
	for(int i = 1; i < a; ++i){
		if(!toint(b[i])) continue;
		if(tot < i) { add += (i-tot); tot = i; }
		tot += toint(b[i]);
	}
	if(tot < a) add += a-tot;
	return add;
}

int main(){
	ifstream fin("ovation.in"); ofstream fout("ovation.out");

	int T;
	fin >> T;
	for(int i = 1; i <= T; ++i){
		int a; string b;
		fin >> a >> b;
		fout << "Case #" << i << ": " << solve(a, b) << "\n";
	}
	return 0;
}
