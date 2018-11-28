#include <vector>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int solve(unsigned mx, const string & s)
{
	int cumsum = 0;
	int need = 0;
	for (int i = 1; i <= mx; ++i)
	{
		cumsum += s[i - 1] - '0';
		if (i - cumsum > need) need = i - cumsum;
	}
	return need;
}

void run() {
	//ifstream fin("A-small-in.txt");
	ifstream fin("A-large-in.txt");
	//ofstream fout("A-small-out.txt");
	ofstream fout("A-large-out.txt");

	unsigned LINE;
	fin >> LINE;

	unsigned mx; string str;
	//cout << LINE;
	for (unsigned line = 0; line != LINE; ++line)
	{
		fin >> mx;
		fin >> str;
		//cout << mx;
		fout << "Case #" << line + 1 << ": " << solve(mx, str) << endl;
	}
	fout.close();
}

int main(){
	run();
	return 0;

}