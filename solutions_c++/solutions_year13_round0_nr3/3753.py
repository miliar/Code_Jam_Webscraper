//
// april 2013
// vladh (vladh.net)
// all right reserved
//

#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<sstream>
using namespace std;

int isPalindrome(int x){
	stringstream ss;
	ss << x;
	string str = ss.str();
	if(str == string(str.rbegin(), str.rend())){
		return true;
	}
	return false;
}

int main(){
	ifstream in("C-small-attempt3.in");
	ofstream out("data.out");
	string line;
	long int cases, a, b, k, i, results=0;
	double rt;

	getline(in,line);
	cases = atoi(line.c_str());

	for(k=1; k<=cases; k++){
		results=0;
		in>>a;
		in>>b;

		for(i=a; i<=b; i++){
			if(isPalindrome(i)){
				rt = sqrt(i);
				if(((int)rt == rt) && isPalindrome((int)rt)){
					results++;
				}
			}
		}

		out<<"Case #"<<k<<": "<<results<<endl;
	}
	
	return 0;
}
