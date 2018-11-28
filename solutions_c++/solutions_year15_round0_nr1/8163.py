#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <iomanip>
#include <cmath>
#include <fstream>

using namespace std;

int main() {
	ifstream fin("A-large.in"); ofstream fout("A-large.out");
	int Smax, T;
	string str;
	
	fin >> T;
	vector<int> ans(T);
	for (int test=1; test<=T; test++) {
		fin >> Smax >> str;
		int sum=0;
		ans[test-1]=0;
		for (int i=0; i<=Smax; i++) {
			if (sum<i) {ans[test-1]+=i-sum; sum+=i-sum;}
			string ch;
			ch=str[i];
			sum+=stoi(ch.c_str());
		}
	}

	for (int i=1; i<=T; i++)
		fout << "Case #" << i << ": " << ans[i-1] << endl;
	
	//system("pause");
}
