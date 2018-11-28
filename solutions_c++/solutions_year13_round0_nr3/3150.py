#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

bool is_palindrome(int X){
	bool R;
	char tmp[4];
	sprintf(tmp,"%d",X);
	int size = strlen(tmp);
	if(size == 1)
		R =1;
	else{
		int F = size/2;
		for(int i=0;i<F;i++){
			if(tmp[i]==tmp[size-i-1])
				R = 1;
			else
				{R=0;break;}
		}
	}		
	return R;
}

int palindrome(int A, int B){
	int R=0;
	float i2;
	for(int i=A;i<=B;i++){
		i2 = sqrt(i);
		if( (is_palindrome(i) && is_palindrome(i2)) && (i2 == int(i2)))
			{R++;}
	}
	return R;

}

int main(){
	
	ifstream input("C-small-attempt0.in");
	ofstream output("output");
	string s,out;
	int tours,A,B,Result;
	input>>tours;
	for(int z=1;z<=tours;z++) {
		input>>A>>B;
		Result = palindrome(A,B);
		output<<"Case #"<<z<<": "<<Result<<endl;
	}
	return 0;
	
}
