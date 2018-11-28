#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
		string inp;
		int s;
		fin>>s;
		fin>>inp;
		int ans = 0, standing = 0;
		for(int j=0;j<inp.size();j++){
			int n = (int)inp[j] - 48;
			if(n==0)
				continue;
			if(standing<j){
				ans+=(j-standing);
				standing = j;
			}
			standing+=n;
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
		//cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
}