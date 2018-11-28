#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>

#include "BigIntegerLibrary.hh"
//from https://mattmccutchen.net/bigint/

using namespace std;

string findImage(string& f){

	int i;
	string res = f;
	int mid = (int)floor(f.size()/2);
	for(i=0;i<mid;i++){
		res[res.size() - i - 1] = res[i];
	}
	return res;
}

bool isGreater(string &a, string& b){

	size_t sz = a.size();

	int i;

	i = 0;
	bool done = false;
	while(!done && i<sz){
		if((a[i]-'0') > (b[i] - '0')) return done = true;
		else if(a[i] - '0' == b[i] - '0') i++;
		else break;
	}

	
	return done;

}

void propagateOne(string &str, int pos){

	if(str[pos] - '0' < 9){
		str[pos] =  (str[pos]) + 1;
		return;
	}

	else{
		if(pos == 0){
			str[pos] =  '0';
			str = "1" + str;
			return;
		}
		else{
			str[pos] = '0';
			propagateOne(str, pos-1);
		}
	}
}

void incrOdd(string & str){

	int pos = str.size()/2;

	if((str[pos] - '0') < 9){
		str[pos] = str[pos] + 1;
	}
	else{
		propagateOne(str, pos);
	}
}

void incrEven(string &str){

	int pos = str.size()/2;
	if((str[pos] - '0') < 9){
		str[pos] = str[pos] + 1;
		str[pos-1] = str[pos-1] + 1;
	}
	else{
		propagateOne(str, pos);
	}

}


string nextPal(string startStr){

	//find image

	string afterImage = findImage(startStr);
	
	//if new number is greater return the result
	if(isGreater(afterImage, startStr)) return afterImage;
	else{
		//depending on whether we have even or odd numbers we make the appropriate changes

		if(startStr.size() % 2 != 0){
			//odd case
			incrOdd(afterImage);
		}
		else{
			//even case
			incrEven(afterImage);
		}

		if(isGreater(afterImage, startStr)) return afterImage;
		return nextPal(afterImage);
	}

	return "";
	
}

string findMult(string &num, int pos){

	string res;
	res.resize(num.size());

	int i;
	int extra = 0;
	int mult;
	int counter = 0;
	for(i=num.size() - 1; i> 0; i--){
		
		mult = (num[pos] - '0') * (num[i] - '0');
		if(mult < 10){
			res[i] = mult + extra + '0';
			extra = 0;
		}
		else{
			
			mult = mult + extra;

			int a = mult/10;
			int b = mult%10;
			extra = a;
			res[i] = b + '0';
		}
	}

	mult = (num[pos] - '0') * (num[i] - '0');

	if(extra == 0){
		res[i] = mult + '0';
	}
	else{
		mult = mult + extra;

		int a = mult/10;
		int b = mult%10;
		extra = a;
		res[i] = b + '0';
		stringstream ss;
		ss << extra;
		string str = ss.str();
		res = str + res;

	}

	return res;
}

string findSquare(string num){

	string res;
	int sz = num.size();
	res.resize(sz);

	int i,j;
	string totalRes = findMult(num, num.size()-1);

	for(i=num.size()-2;i>=0;i--){
		string res = findMult(num, i);

		
	}

	return "";
}

bool isPal(string c){

	if(c == string(c.rbegin(), c.rend())) return true;
	return false;

}

int main(void){

	int N;
	int i;
	
	ifstream fin;
	fin.open("C-small-attempt0.in",ios_base::in);
	ofstream fout;
	fout.open("output.txt",ios_base::out);

	fin>>N;
	for(int test=0;test<N;test++){
			
		string from, to;

		fin>>from;
		fin>>to;
		int total = 0;
		string newPal = "1"; //the palindromes will be saved here
		BigInteger s = stringToBigInteger(newPal);
		s = s*s;
		BigInteger fromB = stringToBigInteger(from);
		BigInteger toB = stringToBigInteger(to);
		
		string palCheck;

		while(s.compareTo(toB) <=0){
			if(s.compareTo(fromB) >= 0 && isPal(palCheck)){
				total++;
			}
			//find next pal number
			newPal = nextPal(newPal);
			s = stringToBigInteger(newPal);
			s = s*s;
			palCheck = bigIntegerToString(s);
			
		}
		
		fout<<"Case #"<<test+1<<": "<<total<<endl;
		
	}

	fin.close();
	fout.close();


}