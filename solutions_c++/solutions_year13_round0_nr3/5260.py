#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
bool ifPalindrom(int i){
	string s = to_string(i);
	for(int j=0;j<s.size()/2;j++){
		if(s[j]!=s[s.size()-j-1]) return false;
	}
	return true;
}
bool ifSqr(int i ){
	int j = sqrt(i);
	if(j*j==i) return true;
	return false;
}
int numberOfFairPalindrom(int start,int end){
	int num = 0;
	for(int i = start ; i <= end ; i++){
		if(ifSqr(i)){
			if(ifPalindrom(i)){
				if(ifPalindrom(sqrt(i))){
				num++;
				}
			}
		}
	}
	return num;
}
int main(int argc, char *argv[]){

	ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int  testcases;
	int start,end;
	in >> testcases;
	char temp;
	
	for(int i=0;i<testcases;i++){
		in >> start >> end;
		out<<"Case #"<<i+1<<": "<< numberOfFairPalindrom(start,end)<<endl;
	}
	return 1;
}