#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;
int getDigit (const long number, int pos){
    return (pos == 0) ? number % 10 : getDigit (number/10, --pos);
}
int toDigit ( const char s ){
	if( s == '0' ){
		return 0;
	}else{
		return s - '0';
	}
}
int main(){
	std::ifstream in("A-large.in");
	std::ofstream out;
	out.open("A-large.out");
	string content;
	
	int numCases;	//Number of testcases
	int m_s;		//Maximum shyness
	int f;			//Friends that are invited
	int s_up;		//The people who stood up
	int aud;		//The audience
	int n;
	
	getline(in, content);
	numCases = atoi(content.c_str());
	
	for (int i=1; i<=numCases; i++ ){
		
		f=0;
		s_up=0;
		
		getline(in, content, ' ');
		m_s = atoi(content.c_str());
		getline(in, content);
		
		for(int a=0; a<=m_s; a++ ){
			
			n = toDigit(content[a]);
			
			if( n == 0 ){
				if( s_up < a+1 ){
					f++;
					s_up++;
				}
			}else{
				s_up = s_up + n;
			}
		
		}
		
		out << "Case #" << i << ": " << f << "\n";
	
	}
	in.close();
	out.close();
	return 0;
}