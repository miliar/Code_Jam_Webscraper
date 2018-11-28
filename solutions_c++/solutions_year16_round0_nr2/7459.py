#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int T,i,j,len,count;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>T;
	for(i=1;i<=T;i++){
		count=0;
		string str;
		fin>>str;
		len = str.length();
		for(j=len-1;j>=0 && str[j] == '+';j--);
		if(j == len-1) count = 1;
		while(j >= 0){
			if(j < len-1 && str[j] != str[j+1]) count++;
			j--;
		}
		fout<<"Case #"<<i<<": "<<count<<endl;	
	}
	return 0;
}

