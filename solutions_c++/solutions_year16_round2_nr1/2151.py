#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<long long> vll;

#define forn(i,n) for(int i=0;i<(int)n;i++)

int num_letter(char c,string s){
	int count=0;
	forn(i,s.size()){
		if(s[i]==c) count++;
	}
	return count;
}

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int main(){
	int T;
	string s;

	fin >> T;
	forn(t,T){
		fin >> s;
		vi nums(10,0);
		nums[0]=num_letter('Z',s);
		nums[2]=num_letter('W',s);
		nums[4]=num_letter('U',s);
		nums[6]=num_letter('X',s);
		nums[8]=num_letter('G',s);

		nums[1]=num_letter('O',s)-nums[2]-nums[4]-nums[0];
		nums[3]=num_letter('H',s)-nums[8];
		nums[5]=num_letter('F',s)-nums[4];
		nums[7]=num_letter('S',s)-nums[6];
		nums[9]=num_letter('I',s)-nums[8]-nums[6]-nums[5];

		fout << "Case #" << t+1 << ": ";
		forn(i,10){
			forn(j,nums[i]) fout << i;
		}
		fout << endl;
	}

	//cout << "hola";

	return 0;
}
