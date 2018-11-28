#include<iostream>
#include<sstream>
#include<string>
#include<cmath>

using namespace std;

bool isfair(unsigned long long n){
	string s;
	stringstream ss;
	ss << n;
	ss >> s;

	for(int i=0;i<s.length()/2+1;i++){
		if (s.at(i) != s.at(s.length() - 1 - i)) {
			return false;
		}
	}
	return true;
}

bool issquare(unsigned long long n){
	unsigned long long s = (unsigned long long)sqrt((double)n);
	return isfair(s) && (floor(s * s) == (double)n);
}

bool isfairandsquare(unsigned long long n){
	return isfair(n) && issquare(n);
}

int main(int argc, char* argv[]){
	long T;
	cin >> T;

	for (long t=1;t<=T;t++){
		string s;
		cin >> s;
		unsigned long long a = stoull(s);
		cin >> s;
		unsigned long long b = stoull(s);
		int count = 0;
		for(int i=a;i<=b;i++){
			if(isfairandsquare(i))count++;
		}
		cout << "Case #" << t << ": " << count << endl;
	}

	return 0;
}