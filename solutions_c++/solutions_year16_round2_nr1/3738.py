
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>
#include <map>

using namespace std;

static int T,I;
static string S;
ifstream input;
ofstream output;

typedef unsigned long long ull;


bool hasNum(int counter['Z'+1], int d) {

	if(d==0) {
		return counter['Z'] >0 &&
			   counter['E'] >0 &&
			   counter['R']>0 &&
			   counter['O']>0;
	} else if (d==1) {
		return counter['O']>0 &&
			   counter['N'] >0 &&
			   counter['E'] >0;
	} else if (d==2) {
		return counter['T'] >0 &&
			   counter['W'] >0 &&
			   counter['O'] >0;
	} else if (d==3) {
		return counter['T'] >0 &&
			   counter['H'] >0 &&
			   counter['R'] >0 &&
			   counter['E'] >= 2;
	} else if (d==4) {
		return counter['F'] >0 &&
			   counter['O'] >0 &&
			   counter['U'] >0 &&
			   counter['R'] >0;
	} else if (d==5) {
		return counter['F'] >0 &&
			   counter['I'] >0 &&
			   counter['V'] >0 &&
			   counter['E'] >0;
	} else if (d==6) {
		return counter['S'] >0 &&
			   counter['I'] >0 &&
			   counter['X'] >0;
	} else if (d==7) {
		return counter['S'] >0 &&
			   counter['V'] >0 &&
			   counter['N'] >0 &&
			   counter['E'] >= 2;
	} else if (d==8){
		return counter['E'] >0 &&
			   counter['I'] >0 &&
			   counter['G'] >0 &&
			   counter['H'] >0 &&
			   counter['T'] >0;
	} else if(d==9){ //9
		return counter['I'] >0 &&
			   counter['E'] >0 &&
     		   counter['N'] >= 2;
	}

	return false;
}

void decreaseNum(int counter['Z'+1], int d) {

	if(d==0) {
		counter['Z']--;
		counter['E']--;
		counter['R']--;
		counter['O']--;
	} else if (d==1) {
		counter['O']--;
		counter['N']--;
		counter['E']--;
	} else if (d==2) {
		counter['T']--;
		counter['W']--;
		counter['O']--;
	} else if (d==3) {
		counter['T']--;
		counter['H']--;
		counter['R']--;
		counter['E'] = counter['E']-2;
	} else if (d==4) {
		counter['F']--;
		counter['O']--;
		counter['U']--;
		counter['R']--;
	} else if (d==5) {
		counter['F']--;
		counter['I']--;
 	    counter['V']--;
	    counter['E']--;
	} else if (d==6) {
		counter['S']--;
		counter['I']--;
		counter['X']--;
	} else if (d==7) {
		counter['S']--;
		counter['V']--;
		counter['N']--;
		counter['E'] = counter['E']-2;
	} else if (d==8){
		counter['E']--;
		counter['I']--;
		counter['G']--;
		counter['H']--;
		counter['T']--;

	} else if (d==9) { //9
		counter['I']--;
		counter['E']--;
		counter['N'] = counter['N'] -2;
	}

}


void solve() {

	int counter ['Z'+1];

	for(char a='A';a<='Z';++a){
		counter[a] = 0;
	}

	for(unsigned int i=0;i<S.length();++i){
		counter[S[i]] = counter[S[i]]+1;
	}

	output << "Case #" << I << ": ";

	int arr[10];
	arr[0] = 0;
	arr[1] = 6;
	arr[2] = 7;
	arr[3] = 2;
	arr[4] = 5;
	arr[5] = 4;
	arr[6] = 9;
	arr[7] = 1;
	arr[8] = 8;
	arr[9] = 3;

	int c[10];
	for(int i=0;i<10;i++){
		c[i]=0;
	}


	for(int i=0;i<=9;++i) {
		while(hasNum(counter,arr[i])) {
			decreaseNum(counter,arr[i]);
			c[arr[i]] = c[arr[i]] +1;
		}
	}
	for(int i=0;i<10;i++){
		while(c[i]-- >0) {
			output << i;
		}
	}



	output << endl;

}



int main(){
	input.open("A-small-attempt5.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(I=1;I<=T;++I){
		input >> S;
		cout << T << endl;
		solve();
		//output << "Case #" << i << ": " << sol << endl;
	}


	input.close();
	output.close();


	return 0;
}




