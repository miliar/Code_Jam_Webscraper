#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main(){
	ifstream fin ("A-large.in");
	ofstream fout ("output.txt");
	int i,j,t,test;
	fin >> t;
	for(test=1;test<=t;test++){
		string s;
		fin >> s;	
		string result;
		string one;
		string two;
		one = s[0];
		two = one;
		if (s.size()==1){
			fout<<"Case #" << test<< ": "<< s << endl;
		}else{
			for(i=1;i<s.size();i++){
				one = s[i] + one;
				two = two+s[i];
				if (two>one){
					one = two;
					result = two;
				}else{
					two = one;
					result = one;
				}
				//cout << "i=" << s[i]<< endl;
			}
			fout<<"Case #" << test<< ": "<< result << endl;
		}
		
		
		
		
		
		
	}
	
	
	
	
	
	
	
	
	
	
	return 0;
}
