#include <iostream>
#include <stdio.h>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;
int main(){

	ofstream myfile;
	myfile.open("example.txt");

	freopen("in.txt", "r", stdin);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		int m;
		cin >> m;
		int people = 0;
		int add = 0;
		string dat;
		cin >> dat;
		for (int j = 0; j <= m; j++){
			char n = dat[j];
			int ad = 0;
			if (people < j){
				ad = j - people;
				add += ad;
			}
			people += ad + (n - '0');
		}
		myfile << "Case #" << i << ": " << add << "\n";
	}
	myfile.close();
	return 0;
}