#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
	ifstream myfile("A-large.in");
	ofstream outfile;
	outfile.open("result.out", ios::out | ios::trunc);

	string tests;
	myfile >> tests;

	int testsNumber = atoi(tests.c_str());
	int pos = 0;

	while(pos++ < testsNumber)
	{
		string str;
		str.clear();
		myfile >> str;

		int maxShyness = atoi(str.c_str());

		myfile >> str;
		int neededFriends = 0;
		int audience = 0;

		for(int i = 0; i < str.size(); i++)
		{
			if(audience + neededFriends < i)
			{
				neededFriends = i - audience;
			}

			string temp;
			temp.clear();
			temp.push_back(str[i]);
			audience += atoi(temp.c_str());
		}
		outfile << "Case #" << pos << ": " << neededFriends << endl;
	}

	return 0;
}
