#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

//#define _DEBUG_
#ifdef _DEBUG_
#define fin cin
#define fout cout
#else

//ifstream fin("A-small-attempt0.in.txt");
//ofstream fout("A-small-attemp0.out.txt");
ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");
#endif

int main()
{

    int T; fin >> T;
    for (int c = 1; c <= T; ++c)
    {
	string S; fin >> S;
	vector<int> numbers;
	map<char, int> charMap;
	for (int i = 0; i < S.size(); ++i) charMap[S[i]]++;
	// check Zero
	auto iter = charMap.find('Z');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['Z']; ++i) numbers.push_back(0);
	    charMap['E'] -= charMap['Z'];
	    charMap['R'] -= charMap['Z'];
	    charMap['O'] -= charMap['Z'];
	    charMap['Z'] = 0;
	}
	// chack Two
	iter = charMap.find('W');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['W']; ++i) numbers.push_back(2);
	    charMap['T'] -= charMap['W'];
	    charMap['O'] -= charMap['W'];
	    charMap['W'] = 0;
	}
	// check Six
	iter = charMap.find('X');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['X']; ++i) numbers.push_back(6);
	    charMap['S'] -= charMap['X'];
	    charMap['I'] -= charMap['X'];
	    charMap['X'] = 0;
	}
	// check Eight
	iter = charMap.find('G');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['G']; ++i) numbers.push_back(8);
	    charMap['E'] -= charMap['G'];
	    charMap['I'] -= charMap['G'];
	    charMap['H'] -= charMap['G'];
	    charMap['T'] -= charMap['G'];
	    charMap['G'] = 0;
	}
	// check Three
	iter = charMap.find('T');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['T']; ++i) numbers.push_back(3);
	    charMap['H'] -= charMap['T'];
	    charMap['R'] -= charMap['T'];
	    charMap['E'] -= charMap['T'];
	    charMap['E'] -= charMap['T'];
	    charMap['T'] = 0;
	}
	// check Four
	iter = charMap.find('R');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['R']; ++i) numbers.push_back(4);
	    charMap['F'] -= charMap['R'];
	    charMap['O'] -= charMap['R'];
	    charMap['U'] -= charMap['R'];
	    charMap['R'] = 0;
	}
	// check Five
	iter = charMap.find('F');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['F']; ++i) numbers.push_back(5);
	    charMap['I'] -= charMap['F'];
	    charMap['V'] -= charMap['F'];
	    charMap['E'] -= charMap['F'];
	    charMap['F'] = 0;
	}
	// check Seven
	iter = charMap.find('S');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['S']; ++i) numbers.push_back(7);
	    charMap['E'] -= charMap['S'];
	    charMap['V'] -= charMap['S'];
	    charMap['E'] -= charMap['S'];
	    charMap['N'] -= charMap['S'];
	    charMap['S'] = 0;
	}

	// Nine
	iter = charMap.find('I');
	if (iter != charMap.end())
	{
	    for (int i = 0; i < charMap['I']; ++i) numbers.push_back(9);
	    charMap['N'] -= charMap['I'];
	    charMap['N'] -= charMap['I'];
	    charMap['E'] -= charMap['I'];
	    charMap['I'] = 0;
	}

	// One
	for (int i = 0; i < charMap['O']; ++i) numbers.push_back(1);

	sort(numbers.begin(), numbers.end());
	fout << "Case #" << c << ": ";
	for (int i = 0; i < numbers.size(); ++i) fout << numbers[i];
	fout << endl;
    }
    return 0;
}
