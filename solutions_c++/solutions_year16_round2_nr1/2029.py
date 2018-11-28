#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;


vector<int> exes;

string str;
map<char, int> mapstr;

#define HASKEY(x) mapstr.find(x)!= mapstr.end()
#define COUNT(x) mapstr[x]



void REMOVE( string str){
	for( int i = 0 ; i < str.size(); i++){
		if(HASKEY(str[i])){
			mapstr[ str[i]]-- ;
			if( mapstr[ str[i]] == 0 ){
				mapstr.erase( str[i] );	
			}
		} 
	}
}

int main(){
	int T;
	cin >> T;
	
	for( int t = 1 ; t <= T ; t++)
	{
		cin >> str;
		
		mapstr.clear();
		exes.clear();
		
		for( int i = 0 ; i < str.size(); i++){
			if(mapstr.find(str[i])!= mapstr.end()){
				mapstr[str[i]]++;	
			}else{
				mapstr[str[i]] = 1;
			}	
		}	
		while(HASKEY('Z')){
			exes.push_back(0);
			REMOVE("ZERO");
		}
		while(HASKEY('X')){
			exes.push_back(6);
			REMOVE("SIX");
		}
		while(HASKEY('W')){
			exes.push_back(2);
			REMOVE("TWO");
		}
		while(HASKEY('U')){
			exes.push_back(4);
			REMOVE("FOUR");
		}
		while(HASKEY('O')){
			exes.push_back(1);
			REMOVE("ONE");
		}
		while(HASKEY('F')){
			exes.push_back(5);
			REMOVE("FIVE");
		}
		while(HASKEY('V')){
			exes.push_back(7);
			REMOVE("SEVEN");
		}
		while(HASKEY('G')){
			exes.push_back(8);
			REMOVE("EIGHT");
		}
		while(HASKEY('N')){
			exes.push_back(9);
			REMOVE("NINE");
		}
		while(HASKEY('T')){
			exes.push_back(3);
			REMOVE("THREE");
		}
		
		cout << "Case #" << t << ": ";
		sort(exes.begin(), exes.end());
		for( int i = 0 ; i < exes.size(); i++ ){
			cout << exes[i];	
		}
		cout << "\n";	

	}
	
	return 0;
}