#include <iostream>
#include <vector>
#include <string>
#include<map>
#include <unordered_map>
#include <fstream>
#include <istream>
#include <ostream>
#include <sstream>
#include<set>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


int main(){

int T,t = 0;

cin >> T;

while(t < T){
	string str;
	
	cin >> str;
	int sz = str.size();
	map<char,int> um;
	vector<int> count(10,0);
	for(char x = 'A' ; x <= 'Z' ; x++){
		um[x] = 0;
	}
	
	for(int i = 0 ; i < sz ; i++){
		um[str[i]]++;
	}
	int zcount = 0;
	auto iter = um.find('Z');
	if(iter != um.end()){
		zcount = um['Z'];
	}
	count[0] = zcount;
	
	while(zcount > 0){
		um['E']--;
		um['R']--;
		um['O']--;
		zcount--;
	}
	
	int xcount = 0;
	iter = um.find('X');
	if(iter != um.end()){
		xcount = um['X'];
	}
	count[6] = xcount;
	
	while(xcount > 0){
			um['S']--;
			um['I']--;
			um['X']--;
			xcount--;
	}
	
	int wcount = 0;
	iter = um.find('W');
	if(iter != um.end()){
		wcount = um['W'];
	}
	count[2] = wcount;
	
	while(wcount > 0){
			um['T']--;
			um['W']--;
			um['O']--;
			wcount--;
	}
	
	int ucount = 0;
	iter = um.find('U');
	if(iter != um.end()){
		ucount = um['U'];
	}
	count[4] = ucount;
	
	while(ucount > 0){
			um['F']--;
			um['O']--;
			um['U']--;
			um['R']--;
			ucount--;
	}
	
	int gcount = 0;
	iter = um.find('G');
	if(iter != um.end()){
		gcount = um['G'];
	}
	count[8] = gcount;
	
	while(gcount > 0){
			um['E']--;
			um['I']--;
			um['G']--;
			um['H']--;
			um['T']--;
			gcount--;
	}
	
	int fivecount = 0;
	iter = um.find('F');
	if(iter != um.end()){
		fivecount = um['F'];
	}
	count[5] = fivecount;
	while(fivecount > 0 ){
		um['F']--;
		um['I']--;
		um['V']--;
		um['E']--;
		fivecount--;
	}
	
	int sevencount = 0;
	iter = um.find('V');
	if(iter != um.end()){
		sevencount = um['V'];
	}
	count[7] = sevencount;
	while(sevencount > 0 ){
		um['S']--;
		um['E']--;
		um['V']--;
		um['E']--;
		um['N']--;
		sevencount--;
	}
	
	int onecount = 0;
	iter = um.find('O');
	if(iter != um.end()){
		onecount = um['O'];
	}
	count[1] = onecount;
	while(onecount > 0 ){
		um['O']--;
		um['N']--;
		um['E']--;
		onecount--;
	}
	
	int ninecount = 0;
	iter = um.find('N');
	if(iter != um.end()){
		ninecount = um['N']/2;
	}
	count[9] = ninecount;
	while(ninecount > 0 ){
		um['N']--;
		um['I']--;
		um['N']--;
		um['E']--;
		ninecount--;
	}
	
	count[3] = um['T'];
	
	cout << "Case #"<< t+1<< ": ";
	for(int i = 0; i < 10; i++){
		for(int j = count[i] ; j > 0 ; j--){
			cout << i ;
		}
	}
	cout << endl;
	
	//cout << "Case #"<< t+1<< ": " << res << endl;
	t++;
}

return 1;
}

