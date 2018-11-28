#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;


int main(){
	ifstream fin("a.txt");
	ofstream fout("a_out.txt");
	int t;
	fin >> t;
	for (int i=0; i<t; i++){
		string s;
		string ans="";
		fin >> s;
		for (int j = 0; j<s.length(); j++){
			char c = s[j];
			if (ans[0]<=c){
				ans=c+ans;
			}
			else{
				ans=ans+c;
			}
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
}
