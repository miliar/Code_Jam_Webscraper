#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string strNumber[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

void remove(int idx, vector<unsigned>& count, int n)
{
	for(int i=0; i<strNumber[idx].length(); ++i) 
		count[strNumber[idx][i] - 'A'] -= n;
}

string solve(string& S)
{
	string ret;

	vector<unsigned> count;
	count.resize(26, 0);

	for (size_t i = 0 ; i < S.length(); ++i)
	{
		int idx = static_cast<int>(S[i] - 'A');
		++count[idx];
	}

	// zero
	for (unsigned i = 0; i < count['Z' - 'A']; ++i)
		ret += '0';
	remove(0, count, count['Z' - 'A']);

	// two
	for (unsigned i = 0; i < count['W' - 'A']; ++i)
		ret += '2';
	remove(2, count, count['W' - 'A']);

	// 4
	for (unsigned i = 0; i < count['U' - 'A']; ++i)
		ret += '4';
	remove(4, count, count['U' - 'A']);

	// 6
	for (unsigned i = 0; i < count['X' - 'A']; ++i)
		ret += '6';
	remove(6, count, count['X' - 'A']);

	// 8
	for (unsigned i = 0; i < count['G' - 'A']; ++i)
		ret += '8';
	remove(8, count, count['G' - 'A']);

	// 3
	for (unsigned i = 0; i < count['R' - 'A']; ++i)
		ret += '3';
	remove(3, count, count['R' - 'A']);

	// 5
	for (unsigned i = 0; i < count['F' - 'A']; ++i)
		ret += '5';
	remove(5, count, count['F' - 'A']);
	
	// 7
	for (unsigned i = 0; i < count['V' - 'A']; ++i)
		ret += '7';
	remove(7, count, count['V' - 'A']);

	// 9
	for (unsigned i = 0; i < count['I' - 'A']; ++i)
		ret += '9';
	remove(9, count, count['I' - 'A']);

	// 1
	for (unsigned i = 0; i < count['O' - 'A']; ++i)
		ret += '1';
	remove(1, count, count['O' - 'A']);


	for (int i = 0 ; i < 26; ++i)
		if (count[i] > 0)
			cerr << "wrong answer" << endl;


	sort(ret.begin(), ret.end());

	return ret;
}


int main()
{
	unsigned numInputs = 0;

	cin >> numInputs;

	for (size_t i=0; i< numInputs; ++i)
	{
		string S;

		cin >> S;

		cout << "Case #" << i + 1 << ": " << solve(S) << endl;
	}
	return 0;
}

