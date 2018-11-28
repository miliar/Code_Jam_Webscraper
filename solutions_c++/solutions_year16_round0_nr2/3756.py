#include <stdio.h>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int x = 0;

int Compute(const string& stack)
{
	int changes = 0;
	size_t i = 1;
	for (; i < stack.size(); i++)
		if (stack[i] != stack[i - 1])
			changes++;
	
	if (stack[i - 1] == '-')
		changes++;

	return changes;
}

int main(int argc, char** argv)
{
	fstream fin;

	fin.open("B-large.in", std::ios::in);

	if (!fin.is_open())
		return -1;

	fstream fout;
	fout.open("B-large.out", std::ios::out);

	if (!fout.is_open())
		return -1;

	int T;

	fin >> T;

	for (int i = 0; i < T; i++)
	{
		string stack;
		fin >> stack;

		fout << "Case #" << (i + 1) << ": " << Compute(stack) << std::endl;
	}

	fin.close();
	fout.close();

	return 0;
}