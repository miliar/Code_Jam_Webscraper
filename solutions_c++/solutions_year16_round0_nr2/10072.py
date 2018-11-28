#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
using namespace std;

int T;
string str;
int minCost = 100000000;

void invert(string& s){
	for(int i =0; i < s.size(); i++){
		if(s[i] == '-'){ s[i] = '+';}
		else{ s[i] = '-';}
	}
}

int recurive( string str, int cost){
	if(cost > minCost){ return cost;}

	if(str.size() == 1){
		if( str[0] == '+'){ return cost;}
		else{return cost+1;}
	}
	
	bool foundNeg = false;
	for(int i =0; i < str.size(); i++){
		if( str[i] == '-'){ foundNeg = true; break;}
	}
	if(!foundNeg ){ return cost;}

	int i = str.size();
	while( str[i-1] == '+'){ i--; }
	str = str.substr(0, i);

	string s_ = str;
	reverse(s_.begin(), s_.end());
	string s__ = s_;
	invert(s_);

	int cost1=  recurive(s__, cost+ 1);
	if(cost == 0){ minCost = cost1;}

	int cost2 = recurive( s_ ,cost+1);
	
	cost1= min(cost1, cost2);
	if(cost == 0){ minCost = cost1;}

	return cost1;
}

int main(){
	ifstream in("input");
	ofstream out("output");

	in >> T;
	for(int i =1; i <=T; i++){
		out << "Case #" << i << ": ";
		in >> str;
		minCost = str.size();

		out << recurive(str, 0) << endl;
	}
}