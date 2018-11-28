#include <iostream>
#include <fstream>
using namespace std;

string getPhoneNumber(string str){
	int chars[26],i,len=str.length();
	int digit[10];
	for(i=0;i<26;i++) chars[i] = 0;
	for(i=0;i<10;i++) digit[i] = 0;
	string result="";
	for(i=0;i<len;i++){
		chars[str[i]-'A']++;
	}
	while(chars['Z'-'A'] > 0){
		chars['Z'-'A']--;
		chars['E'-'A']--;
		chars['R'-'A']--;
		chars['O'-'A']--;
		digit[0]++;
	}
	while(chars['U'-'A'] > 0){
		chars['F'-'A']--;
		chars['O'-'A']--;
		chars['U'-'A']--;
		chars['R'-'A']--;
		digit[4]++;
	}
	while(chars['F'-'A'] > 0){
		chars['F'-'A']--;
		chars['I'-'A']--;
		chars['V'-'A']--;
		chars['E'-'A']--;
		digit[5]++;
	}
	while(chars['V'-'A'] > 0){
		chars['S'-'A']--;
		chars['E'-'A']-=2;
		chars['V'-'A']--;
		chars['N'-'A']--;
		digit[7]++;
	}
	while(chars['S'-'A'] > 0){
		chars['S'-'A']--;
		chars['I'-'A']--;
		chars['X'-'A']--;
		digit[6]++;
	}
	while(chars['W'-'A'] > 0){
		chars['T'-'A']--;
		chars['W'-'A']--;
		chars['O'-'A']--;
		digit[2]++;
	}
	while(chars['R'-'A'] > 0){
		chars['T'-'A']--;
		chars['H'-'A']--;
		chars['R'-'A']--;
		chars['E'-'A']-=2;
		digit[3]++;
	}
	while(chars['O'-'A'] > 0){
		chars['O'-'A']--;
		chars['N'-'A']--;
		chars['E'-'A']--;
		digit[1]++;
	}
	while(chars['T'-'A'] > 0){
		chars['E'-'A']--;
		chars['I'-'A']--;
		chars['G'-'A']--;
		chars['H'-'A']--;
		chars['T'-'A']--;
		digit[8]++;
	}
	while(chars['N'-'A'] > 0){
		chars['N'-'A']-=2;
		chars['I'-'A']--;
		chars['E'-'A']--;
		digit[9]++;
	}
	for(i=0;i<10;i++){
		while(digit[i] > 0){
			char ch = '0' + i;
			result.append(1,ch);
			digit[i]--;
		}
	}
	return result;
}

int main() {
	int i,T;
	string S;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>T;
	for(i=1;i<=T;i++){
		fin>>S;
		fout<<"Case #"<<i<<": "<<getPhoneNumber(S)<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
