#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;
int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int test=1;test<=t;test++){
		string s;
		fin >> s;
		string result;
		int res=0,num;
		int i,j;
		for(i=0;i<s.size();i++){
			if(string(result + s[i]) > string(s[i]+result)){
				result = result + s[i];
			} else {
				result = s[i]+result;
			}
		}
		
		
		fout << "Case #" << test << ": " << result << endl;
	}
	
	return 0;
}
