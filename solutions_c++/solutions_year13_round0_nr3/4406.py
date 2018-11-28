#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <math.h>
#include <map>
using namespace std;

vector<int> getNumber(string str){
    vector<int> ret;
    string numS = "";
    for(int i=0; i<str.size(); i++){
	if(str[i] == ' ' && numS!=""){
	    ret.push_back( atoi(numS.c_str()) );
	    numS = "";
	}else
	    numS += str[i];
    }
    if(numS!="")
	ret.push_back( atoi(numS.c_str()) );

    return ret;
}

bool checkFair(long long val){
    string str = "";
    while(val > 0){
	int reminder = (int)(val - (val/10)*10);
	str += (char)(reminder + '0');
	val /= 10;
    }

    for(int i=0; i<str.size()/2; i++){
	if(str[i] != str[ str.size()-1 -i])
	    return false;
    }
    return true;
}

int main(){
    ifstream input_file("C-small-attempt0.in");
    ofstream output_file("C-small-attempt0.out");
    string buff;
    vector<string> text;

    getline(input_file, buff);
    int total = atoi(buff.c_str());
    int caseCount = 0;

    while(getline(input_file, buff)){
	caseCount++;
	vector<int> init = getNumber(buff);
	int min = (int)(sqrt(init[0]));
	if(min < sqrt(init[0]))
	    min++;
	int max = (int)(sqrt(init[1]));
	int result = 0;

	for(int val=min; val<=max; val++){

	    if(checkFair((long long)val)){
		long long powVal = pow(val, 2);
		if(checkFair(powVal))
		    result++;
	    }
	}

	output_file << "Case #" << caseCount << ": " << result << endl;
    }
    input_file.close();
    output_file.close();
    return 0;    
}
