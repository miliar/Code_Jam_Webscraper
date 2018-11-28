#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("a1.in");
	ofstream fout("out.out");
	int t,shy,res,sum,count = 1;
	fin >> t;
	string str;
	while(t--){
		sum = 0;
		res = 0;
		fin >> shy;
		fin >> str;
		for(int i = 0; i < str.length();i++){
			if(sum < i){
				res += i - sum;
				sum++;
			}
			sum += str[i] - '0';
			
		}		
	fout << "Case #"<<count <<": "<<res << '\n'; 
	count++;
	}
	fin.close();
	fout.close();
	return 0;
}
