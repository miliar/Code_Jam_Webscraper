#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	int c = 1;
	int in1 = 0, t = 0;
	ifstream inputfile("test.txt");
	fstream outfile;
	outfile.open("out.txt", ios::out);
	inputfile >> t;
	while (t--) {
		inputfile >> in1;
		int out1 = in1;
		bool check[10] = {};
		fill(check, check + 10, false);
		while (1) {
			bool temp = true;
			int temp1 = out1;
			if (temp1 == 0)
				break;
			while (temp1) {
				check[temp1 % 10] = true;
				temp1 /= 10;
			}
			for (int i = 0; i < 10; i++) {
				if (check[i] == false) {
					temp = false;
					break;
				}
			}
			if (temp == true)
				break;
			out1 += in1;
		}
		if (in1 != 0) {
			outfile << "Case #" << c++ << ": " << out1 << endl;
		}
		else {
			outfile << "Case #" << c++ << ": INSOMNIA"<< endl;
		}
	}
	return 0;
}