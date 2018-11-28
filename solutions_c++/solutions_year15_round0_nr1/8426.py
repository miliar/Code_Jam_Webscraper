#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
	int T,Smax,i,j;
	string shyness;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin>>T;
	for(i=1;i<=T;i++){
		fin>>Smax>>shyness;
		int result = 0,upto = shyness[0]-'0';
		for(j=1;j<=Smax;j++){
			if(upto < j){
				result += (j - upto);
				upto = j;
			}
			upto += (shyness[j] - '0');
		}
		fout<<"Case #"<<i<<": "<<result<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
