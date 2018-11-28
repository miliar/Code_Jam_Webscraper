#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("siii.txt");

int main(){
	int T=0;
	fin >> T;
	
	for(int t=0;t<T;t++){
		int smax;
		fin >> smax;
		string s;
		fin >> s;
		
		int f=0;
		int a=0;
		for(int i=0;i<=smax;i++){
			if(a<i){
				f++;
				a++;
			}
			a+=s[i]-'0';
		}
		
		fout << "Case #" << t+1 << ": " << f << endl;
	}	
	
	return 0;
}
