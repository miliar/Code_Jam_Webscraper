#include<string>
#include<iostream>
#include<fstream>
using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("B_revenge.out");
	int N;
	fin>>N;
	for(int zzz=1; zzz<=N; zzz++){
		string in;
		fin>>in;
		char now = in[0];
		int cnt=0;
		for(int i=1; i<in.length(); i++){
			if(in[i] != now){
				cnt++;
				now = in[i];
			}
		}
		if(now=='-')
			cnt++;
		fout <<"Case #"<<zzz<<": "<<cnt<<endl;
	}
	return 0;
}
