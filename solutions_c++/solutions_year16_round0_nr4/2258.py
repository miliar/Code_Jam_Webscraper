#include<fstream>

using namespace std;

int main(){
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1;ca<=t;ca++){
		int k,c,s;
		fin>>k>>c>>s;
		fout<<"Case #"<<ca<<": ";
		for(int i=1;i<=k;i++)
			fout<<i<<" ";
		fout<<"\n";
	}
}