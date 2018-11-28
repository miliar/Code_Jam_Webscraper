#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include<vector>
#include <sstream>
#include <algorithm>
using namespace std;


void split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
}

int readNextInt(ifstream *file) {
	string str;
	getline(*file, str);
	return(atoi(str.c_str()));
}
void dec(int* letters, int* nums, string s, int count) {
	int len = s.length(), i;
	for (i=0; i<len; i++) {
			letters[(s[i]-'A')] -= count;
	}
}

void solve(string s) {
	int len = s.length();
	int letters[26]={0}, nums[10]={0}, i=0,j=0;

	for (i=0; i<len; i++) {
		letters[(s[i]-'A')] ++;
	}
	//8's
	nums[8] = letters[('G'-'A')];//g
	dec(letters, nums, "EIGHT",nums[8]);

	//6's'
	nums[6] = letters[('X'-'A')];//x
	dec(letters, nums, "SIX",nums[6]);

	//4s
	nums[4] = letters[('U'-'A')];//u
	dec(letters, nums, "FOUR",nums[4]);

	//2s
	nums[2] = letters[('W'-'A')];//w
	dec(letters, nums, "TWO",nums[2]);

	//0s
	nums[0] = letters[('Z'-'A')];//Z
	dec(letters, nums, "ZERO",nums[0]);

	//7
	nums[7] = letters[('S'-'A')];//s
	dec(letters, nums, "SEVEN",nums[7]);

	//5
	nums[5] = letters[('V'-'A')];//v
	dec(letters, nums, "FIVE",nums[5]);

	//9
	nums[9] = letters[('I'-'A')];//I
	dec(letters, nums, "NINE",nums[9]);

	//3s
	nums[3] = letters[('H'-'A')];//h
	dec(letters, nums, "THREE",nums[3]);

	//1s
	nums[1] = letters[('O'-'A')];//o
	dec(letters, nums, "ONE", nums[1]);
	for(i=0;i<10;i++) {
		for(j=0;j<nums[i];j++) {
			cout<<i;
		}
	}
	int sum =0;
	for(i=0;i<26;i++) {
		sum+=letters[i];
		}
	if(sum!=0) {
		cout<<"ERROR:"<<sum;
	}
	cout <<"\n";
	return;
}

int main() {
	ifstream input;
	input.open("test.txt");
	int  n=0, T = 0;
	string s;
		input>>T;
    for(n=0; n<T;n++) {
    	input >> s;
    	cout<<"Case #"<<(n+1)<<": ";
    	solve(s);
    }
    return 0;
}
