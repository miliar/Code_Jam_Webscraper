#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <array>
using namespace std;
char ccc[]={'i','j','k'};

std::array<std::array<char, 4>, 4> a {{
	{'h','i','j','k'},
	{'i','h','k','j'},
	{'j','k','h','i'},
	{'k','j','i','h'}
}};

std::array<std::array<int, 4>,4> negative {{
	{0,0,0,0},
	{0,1,0,1},
	{0,1,1,0},
	{0,0,1,1}
}};

void showVec(const vector<char> &v){
	for(auto &c: v){
		cout<<c;
	}
}


void reduce(vector<char> &v, vector<int> &s){
	char term1 = v.back();
	v.pop_back();
	char sign1 = s.back();
	s.pop_back();
	
	char term2 = v.back();
	v.pop_back();
	char sign2 = s.back();
	s.pop_back();
	
	char newTerm = a[term2-'h'][term1-'h'];
	int  newSign = negative[term2-'h'][term1-'h'];
	v.push_back(newTerm);
	// must invert sign
	if((sign1 == 0 && sign2 == 1) || (sign1 == 1 && sign2 == 0)){
		newSign = newSign==1?0:1;
	}
	s.push_back(newSign);
}

int main(int argc, char *argv[]) {
	int nTestCases;
	//auto &input = cin;
	ifstream input("C-small-attempt0.in");
	
	input>>nTestCases;

	for(int i = 0; i < nTestCases; i++){
		int strSize;
		int mult;
		string strstr;
		
		bool isNegative = false;
		input>>strSize;
		input>>mult;
		input>>strstr;
		vector<char> str(strSize*mult);
		vector<int> sign(strSize*mult);
		int cont = 0;
		for(int j = 0; j < mult; j++){
			for(int k = 0; k < strSize; k++){
				str[cont] = strstr[k];
				sign[cont] = 0;
				++cont;
			}
		}
		//showVec(str);
		//cout<<endl;
		
		bool foundK = false;
		bool foundJ = false;
		
		
		while(str.size() > 1)
		{
			char back = str.back();
			if(back=='k' && !foundK){
				foundK = true;
				str.pop_back();
				int sig = sign.back();
				sign.pop_back();
				
				// must invert the sign of the remaining chain
				if(sig == 1){
					int sig2 = sign.back();
					sign.pop_back();
					sign.push_back(sig2==0?1:0);
				}
			}else if(back=='j' && !foundJ && foundK){
				foundJ = true;
				str.pop_back();
				int sig = sign.back();
				sign.pop_back();
				if(sig == 1){
					int sig2 = sign.back();
					sign.pop_back();
					sign.push_back(sig2==0?1:0);
				}
			}else{
				reduce(str, sign);
			}
		}
		cout<<"Case #"<<i+1<<": "<<(str[0]=='i' && sign[0]==0 && foundJ && foundK?"YES":"NO")<<endl;
		
	}
	
	return 0;
}

