#include <iostream>
#include <assert.h>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int t;
	string s, temp;
	string filename;
	cin >> filename;
	fstream myfile, output;
	myfile.open(filename, ios::in);
	output.open("output.txt", ios::out);
	myfile >> t;
	assert(t <= 100 && t >= 1);
	for (int j = 0; j < t;j++) {
		output << "Case #" << j + 1 << ": ";
		myfile >> s;
		temp = "";
		assert(s.size() <= 1000  && s.size() >= 1);
		temp += s[0];
		for (int i = 1; i < s.size();i++)
		{
			if (s[i] >= temp[0])
				temp = s[i]+ temp;
			else 
				temp += s[i];
		}
		output << temp << endl;
	}
}