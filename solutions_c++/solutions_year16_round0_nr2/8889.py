#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

char flip(string &input, int index)
{
	for (int i = 0; i < index; i++)
	{
		if(input.at(i) == '-') input.at(i) = '+';
		else input.at(i) = '-';
	}
	return input.at(0);
}

int getGreedyMoves(string input)
{
	int moves = 0;
	char last;
	for (int i = 0; i < input.length(); i++)
	{
		last = input.at(0);
		if(input.at(i) != last)
		{
			last = flip(input, i);
			moves++;
		}
	}
	if(moves == 0 && input.at(0) == '+') return 0;
	else if(moves == 0 && input.at(0) == '-') return 1;
	else if(last == '-') moves++;
	return moves;
}

int main()
{
	ifstream fin("pancakes.txt");
	ofstream fout("output-Pancake.txt");

	int testcases;
	fin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		string input;
		fin >> input;
		fout << "Case #" << i+1 << ": " << getGreedyMoves(input) << endl;
	}
	return 0;
}