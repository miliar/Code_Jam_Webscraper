#include <iostream>
#include <cstdio>
#include <fstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

string getLastWord(const string& words)
{
	string curr = words.substr(0, 1);
	for (int i = 1; i < words.length(); i++)
	{
		if (curr[0] <= words[i])
			curr = words.substr(i, 1) + curr;
		else
			curr.push_back(words[i]);
	}
	return curr;
}

void problemA()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		string words;
		in >> words;
		string res = getLastWord(words);
		out << "Case #" << t << ": " << res << endl;
	}
}


int main(int argc, char** argv)
{
	problemA();
	return 0;
}