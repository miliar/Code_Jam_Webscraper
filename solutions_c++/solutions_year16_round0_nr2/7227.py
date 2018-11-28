/*
 * pancake.cc
 *
 *  Created on: Apr 9, 2016
 *      Author: Terrence
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<bool> shrink(vector<bool> pancake){
	int all = pancake.size();
	int i = 0;
	vector<bool> shrink;
	shrink.push_back(pancake[0]);
	while(i<all-1){
		if(pancake[i]!=pancake[i+1]){
			shrink.push_back(pancake[i+1]);
		}
		i++;
	}
	return shrink;
}

int rolltimes(vector<bool> pancake){
	pancake = shrink(pancake);
	int countings = 0;
	if(pancake[0] == false){
		for(vector<bool>::iterator it = pancake.begin();it!=pancake.end();++it){
			if(*it == false){
				countings++;
			}
		}
		return 2*countings-1;
	}
	else{
		for(vector<bool>::iterator it = pancake.begin();it!=pancake.end();++it){
			if(*it == false){
				countings++;
			}
		}
		return 2*countings;
	}

}

int main(){
	ifstream in("B-large.in.txt");
	ofstream out("output.txt");
	string line;
	int num;
	int i = 1;
	in>>num;
	while(in>>line){
		vector<bool> pancake;
		const char* str = line.c_str();
		for(int i = 0;i<line.length();i++){
			if(str[i] - '+' == 0 ){
				pancake.push_back(true);
			}
			else{
				pancake.push_back(false);
			}

		}
		out<<"Case #"<<i++<<": "<<rolltimes(pancake)<<endl;
		pancake.clear();

	}
}



