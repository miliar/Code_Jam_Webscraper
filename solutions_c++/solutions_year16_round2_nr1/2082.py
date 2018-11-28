#include <iostream>
#include <string>
#include <vector>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void subtractWord(string word, vector<int> &letters)
{
	for (int i = 0; i < word.size(); ++i)
	{
		--letters[word[i] - 'A'];
	}
}

void run()
{
	string S;
	cin >> S;

	vector<int> letters(26, 0);
	vector<int> numbers(10, 0);

	for (int i = 0; i < S.size(); ++i)
	{
		++letters[S[i] - 'A'];
	}

	// Remove words
	while (letters['Z' - 'A'] > 0)
	{
		subtractWord("ZERO", letters);
		++numbers[0];
	}

	while (letters['W' - 'A'] > 0)
	{
		subtractWord("TWO", letters);
		++numbers[2];
	}

	while (letters['U' - 'A'] > 0)
	{
		subtractWord("FOUR", letters);
		++numbers[4];
	}

	while (letters['X' - 'A'] > 0)
	{
		subtractWord("SIX", letters);
		++numbers[6];
	}

	while (letters['G' - 'A'] > 0)
	{
		subtractWord("EIGHT", letters);
		++numbers[8];
	}

	while (letters['F' - 'A'] > 0)
	{
		subtractWord("FIVE", letters);
		++numbers[5];
	}

	numbers[1] = letters['O' - 'A'];
	numbers[3] = letters['H' - 'A'];
	numbers[7] = letters['V' - 'A'];
	numbers[9] = letters['I' - 'A'];


	for (int i = 0; i < numbers.size(); ++i)
	{
		cout << string(numbers[i], i + '0');
	}
	cout << endl;
}