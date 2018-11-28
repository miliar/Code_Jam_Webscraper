#include<iostream>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;

int main() {
	ifstream fin("F:\\A-large.in");
	ofstream fout("out.txt");
	int k;
	fin>>k;
	for(int kk = 1; kk <= k; kk++) {
		int smax;
		string ss;
		fin>>smax>>ss;
		int ans = 0;
		int count = 0;
		for(int i = 0; i < ss.length(); i++) {
			if(count < i) {
				ans += i - count;
				count = i;
			}
			count += ss[i]-'0';
		}
		//cout<<"Case #"<<kk<<": "<<ans<<endl;
		fout<<"Case #"<<kk<<": "<<ans<<endl;
	}
	fout.close();
	fin.close();

	return 0;
}