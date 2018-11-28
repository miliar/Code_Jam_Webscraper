#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define NOT_POSSIBLE "Fegla Won"

char *alphabet;

int countMoves(int ** occurs, int size, int groups)
{
	const int medianIndex = size / 2;
	int counter = 0;
	for (int n = 0; n < groups; ++n)
	{
		int * occ = new int[size];
		for (int i = 0; i < size; ++i)
		{
			occ[i] = occurs[i][n];
			//cerr << "occ[" << i << "]: " << occ[i] << "\n";
		}

		for (int i = size - 1; i > 0; --i)
			for (int j = 0; j < i; ++j)
				if (occ[j] > occ[j + 1])
				{
					int temp = occ[j];
					occ[j] = occ[j + 1];
					occ[j + 1] = temp;
				}

		int median = occ[medianIndex];
		//cerr << "median: " << median << endl;

		int sum = 0;
		for (int i = 0; i < size; ++i)
		{
			sum += abs(occ[i] - median);
		}
		counter += sum;
		delete[] occ;
	}
	return counter;
}

void buildAlphabet(char* alphabet, int groups, string s)
{
	int index = 1;
	alphabet[0] = s[0];
	for (size_t n = 1; n < s.length(); ++n)
	{
		if (s[n] != alphabet[index - 1])
		{
			alphabet[index] = s[n];
			++index;
		}
	}
}

int countGroups(string s)
{
	if (s.length() == 0)
		return 0;
	int retval = 1;
	char curr = s[0];
	for (size_t n = 1; n < s.length(); ++n)
	{
		if (curr != s[n])
		{
			++retval;
			curr = s[n];
		}
	}
	return retval;
}

bool correctOrder(string s, int ** occurs, int noInput, int groups)
{
	bool retval = true;
	int counter = 1;
	char curr = s[0];
	int index = 0;

	for (size_t n = 1; n < s.length(); ++n)
	{
		if (s[n] != curr)
		{
			occurs[noInput][index] = counter;
			counter = 0;
			if (curr != alphabet[index])
				return false;
			++index;
			curr = s[n];
		}
		++counter;
	}
	occurs[noInput][index] = counter;
	if (curr != alphabet[index])
		return false;

	return true;
}


int processOnce()
{
	int errorCode = 0;
	int count;
	cin >> count;

	string temp;
	cin >> temp;

	const int groups = countGroups(temp);
	alphabet = new char[groups];
	buildAlphabet(alphabet, groups, temp);

	int** occurs = new int*[count];
	for (int n = 0; n < count; ++n)
		occurs[n] = new int[groups];

	correctOrder(temp, occurs, 0, groups);
	for (int n = 1; n < count; ++n)
	{
		cin >> temp;
		int currGroups = countGroups(temp);
		if (groups != currGroups)
		{
			errorCode = -1;
			break;
		}

		if (!correctOrder(temp, occurs, n, groups))
		{
			errorCode = -2;
			break;
		}
	}

/*	cerr << "occurs" << endl;
	for (int i = 0; i < count; ++i)
	{
		for (int j = 0; j < groups; ++j)
			cerr << occurs[i][j] << "\t";
		cerr << endl;
	}*/

	int retval;

	if (errorCode == 0)
		retval = countMoves(occurs, count, groups);
	else
		retval = -1;

	for (int n = 0; n < count; ++n)
		delete[] occurs[n];
	delete[] occurs;

	return retval;
}

int main()
{
	std::ifstream in("A-small-attempt0.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int num = processOnce();
		cout << "Case #" << (i + 1) << ": ";
		if (num == -1)
			cout << NOT_POSSIBLE << endl;

		else
			cout << num << endl;
	}

	system("pause");
	return 0;
}