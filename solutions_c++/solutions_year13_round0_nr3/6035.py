#include <iostream>
#include <sstream>
#include <cassert>
#include <string>
#include <cmath>

using namespace std;

int
is_palim(string s){
	int i=0, j=s.size()-1;
	int b=1, end=j-i+1;
	for(int k=0; k<=end/2 && b; k++){
		assert(k>=0 && end-k-1>=0 && k<s.size() && end-k-1<s.size());
		if(s[k+i]!=s[j-k]){
			b=0;
		}
	}

	return b;
}

string
int_to_string(int n){
	stringstream st;
	string s;
	st << n;
	s = st.str();
	return s;
}

int
is_square(int n){
	double d=sqrt(n);
	int x=floor(d), b=0;
	if(x==ceil(d)){
		b=1;
	}
	if(b){
		b= b && is_palim(int_to_string(x));
	}
	return b;
}

int
main(void){
	int t=0, a=0, b=0, counter=0;
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>a>>b;
		counter=0;
		for(int j=a; j<=b; j++){
			if(is_palim(int_to_string(j)) && is_square(j)){
				counter ++;
			}
		}
		cout << "Case #" << i+1 << ": " << counter << endl;
	}
	return 0;
}
