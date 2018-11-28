#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;

int main(){
	ofstream output;
	output.open("first.txt");
	int t;
	cin >> t;
	for(int T=1;T<=t;T++){
		output << "Case #" << T << ": ";
		string in;
		cin >> in;
		map<char,int> map1;
		map<char,int>::iterator it;
		for(int i=0;i<in.size();i++){
			it = map1.find(in[i]);
			if(it!=map1.end()){
				(it->second)++;
			}
			else{
				map1[in[i]] = 1;
			}
		}
		vector<char> v1; 
		for(it=map1.begin();it!=map1.end();it++){
			if(it->first=='W'){
				for(int j=0;j<it->second;j++){
					v1.push_back('2');
				    map1['T']--;
				    map1['O']--;
				}	
				map1.erase('W');		
			}
			if(it->first=='U'){
				for(int j=0;j<it->second;j++){
					v1.push_back('4');
					map1['F']--;
					map1['O']--;
					map1['R']--;
				}
				map1.erase('U'); 
			}
			if(it->first=='Z'){
				for(int j=0;j<it->second;j++) {
					v1.push_back('0');
					map1['E']--;
					map1['R']--;
					map1['O']--;
				}
				map1.erase('Z');
			}
			if(it->first=='X'){
				for(int j=0;j<it->second;j++) {
					v1.push_back('6');
					map1['S']--;
					map1['I']--;
				}
				map1.erase('X');
			}
			if(it->first=='G'){
				for(int j=0;j<it->second;j++) {
					v1.push_back('8');
					map1['E']--;
					map1['I']--;
					map1['H']--;
					map1['T']--;
				}
				map1.erase('G');
			}
		}

		it = map1.find('H');
		if(it!=map1.end()){
			if(it->second!=0){
				for(int j=0;j<it->second;j++){
					v1.push_back('3');
					map1['T']--;
					map1['R']--;
					map1['E']= map1['E']-2;
				}
				map1.erase('H');
			}
		}
		it = map1.find('S');
		if(it!=map1.end()){
			if(it->second!=0){
				for(int j=0;j<it->second;j++){
					v1.push_back('7');
					map1['E']=map1['E']-2;
					map1['V']--;
					map1['N']--;
				}
			}
		}
		it = map1.find('V');
		if(it!=map1.end()){
			if(it->second!=0){
				for(int j=0;j<it->second;j++){
					v1.push_back('5');
					map1['F']--;
					map1['I']--;
					map1['E']--;
				}
			}
		}

		it = map1.find('I');
		if(it!=map1.end() && it->second!=0){
			for(int j=0;j<it->second;j++){
				v1.push_back('9');
				map1['N'] = map1['N']-2;
				map1['E']--;
			}
		}
		it = map1.find('O');
		if(it!=map1.end() && it->second!=0){
			for(int j=0;j<it->second;j++){
				v1.push_back('1');
				map1['N']--;
				map1['E']--;
			}
		} 


		
		sort(v1.begin(),v1.end());
		vector<char>::iterator it1;
		for(it1=v1.begin();it1!=v1.end();it1++){
			output << *it1;
		}
		output << endl;
	}
	return 0;
}