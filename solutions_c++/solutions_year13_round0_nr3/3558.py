#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <math.h>
using namespace std;

ifstream input("in.in");
ofstream output("out");

bool palindrom(int x){
	string temp;
	ostringstream ss;
	ss << x;
	temp = ss.str();
	if(temp.size()==1)return true;
	
	int size2=(temp.size()/2)+1;
	for(int a(0);a<size2;a++){
		int od_zadaj=temp.size()-1-a;
		if(temp[a]!=temp[od_zadaj])return false;
	}
	return true;
}



int main(){	
	int ponovi, A, B;
	input >> ponovi;
	
	for(int a(0);a<ponovi;a++){
		int koliko(0);
		input >> A >> B;
		for(int b(A);b<B+1;b++){
			int koren=sqrt(b);
			if(sqrt(b)!=koren){
				continue;
			}
			if(palindrom(b) and palindrom(koren)){
				koliko++;
			}
		}
		output << "Case #" << a+1 << ": " << koliko << endl;
	}
	return 0;	
}
