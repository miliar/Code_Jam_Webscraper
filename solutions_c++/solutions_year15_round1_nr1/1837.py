#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<stdio.h>
#include<fstream>
using namespace std;


int main() {
	int t;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>t;
	for(int k = 1; k <= t; k++) {
		int ans1 = 0, ans2 = 0;
		int maxc = 0;
		int m[10001];
		int n;
		fin>>n;
		for(int i = 0; i < n; i++)
			fin>>m[i];
		for(int i = 1; i < n; i++) {
			ans1 += max(0, m[i-1] - m[i]);
			maxc = max(maxc, m[i-1] - m[i]);
		}
		for(int i = 0; i < n-1; i++) {
			ans2 += min(maxc, m[i]);
		}
		//printf("Case #%d: %d %d\n", k, ans1, ans2);
		fout<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}