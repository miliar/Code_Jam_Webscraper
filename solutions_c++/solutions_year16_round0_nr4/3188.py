#include<cstdio>
#include<fstream>
using namespace std;
int T,K,C,S;
int main(){
	ifstream fin;
	fin.open("D-small.in");
	ofstream fout;
	fout.open("D-small.out");
	
	fin>>T;
	
	for(int i=0;i<T;++i){
		fin>>K>>C>>S;
		fout<<"Case #"<<(i+1)<<":";
		for(int j=1;j<=S;++j) fout<<" "<<j;
		fout<<endl;
	}
	
	return 0;
}
