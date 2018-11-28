
#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;


int main()
{
	
	ofstream mf;
	ifstream rf;
	rf.open("test.txt");
	mf.open("output.txt");

	int t;
	string s;
	getline(rf, s);
	t = stoi(s, nullptr, 10);
	for (int x = 0; x < t;x++) {
		if (x)mf << endl;
	    int n;
		getline(rf, s);
		n = 0;
		for (int i = 0; s[i] != ' '; i++) {
			if (i)n = n * 10;
			n += (s[i] - 48);
		}
		mf << "Case #" << x+1 << ":";
		for (int i = 0; i < n; i++) {
			mf << " " << i + 1;
		}


	}
	rf.close();
	mf.close();

	return 0;

}