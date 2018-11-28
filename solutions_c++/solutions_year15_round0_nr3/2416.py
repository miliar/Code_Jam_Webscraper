#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

#define ONE 1
#define I 2
#define J 3
#define K 4



long long multArray[5][5] = { { 0,  0,       0,       0,       0 },
						{ 0,  1,       I,       J,       K },
						{ 0,  I,      -1,       K,  -1 * J },
						{ 0,  J,  -1 * K,      -1,       I },
						{ 0,  K,       J,  -1 * I,      -1 } };

long long numProblems;
bool canSolve;

long long numChars;
long long reps;
string s;

ifstream fin;
ofstream fout;


void Initialize();
void ReadProblem();
void SolveProblem();
void OutputProblem(long long n);

long long Quat(long long a, long long b);
bool ReducesToNegOne();
bool CanMakeI();
bool CanMakeK();
long long GetQuatFromChar(char c);

int main()
{
	Initialize();

	for (long long i = 1; i <= numProblems; i++)
	{
		ReadProblem();
		SolveProblem();
		OutputProblem(i);
		//system("PAUSE");
	}
}

void Initialize()
{
	numProblems = 0;

	fin = ifstream("input.txt");
	fout = ofstream("output.txt");

	fin >> numProblems;
}

void ReadProblem(void)
{
	fin >> numChars;
	fin >> reps;

	char* c = new char[numChars];

	fin >> c;

	s = (string)c;

}

void SolveProblem()
{
	canSolve = false;
	if (ReducesToNegOne())
		if (CanMakeI())
		{
			if (CanMakeK())
			{
				canSolve = true;
			}
			else
			{
				canSolve = false;
			}
		}
		else
		{
			canSolve = false;
		}
	else
	{
		canSolve = false;
	}
}

void OutputProblem(long long n)
{
	fout << "Case #" << n << ": ";

	if (canSolve)
	{
		fout << "YES";
	}
	else
	{
		fout << "NO";
	}

	fout << endl;
}

long long Quat(long long a, long long b)
{
	long long sign = 1;
	
	if (a < 0)
	{
		a *= -1;
		sign *= -1;
	}
	if (b < 0)
	{
		b *= -1;
		sign *= -1;
	}

	return sign * multArray[a][b];
}


bool ReducesToNegOne()
{
	// First, find out what one substring equals
	long long baseS = ONE;

	// Do an extra check here
	// Not quite in line with the function name
	if (numChars == 1)
	{
		// Cannot make any other characters
		return false;
	}

	for (long long i = 0; i < numChars; i++)
	{
		char c = s[(long)i];
		long long quat = GetQuatFromChar(c);
		baseS = Quat(baseS, quat);
	}

	long long extras = reps - 1;

	// Separate the first sub-string from the rest
	long long frontS = baseS;

	// These files are going to be large
	// Need to continually shrink
	while (extras > 0)
	{
		if (extras % 2 == 0)
		{
			// Can combine every two substrings long longo an equal one 
			// Will change every single sub-string long longo the same string
			extras /= 2;
			baseS = Quat(baseS, baseS);
		}
		else
		{
			// Have an even number, plus one in front
			// Merge the first one with the 'front' substring
			extras--;
			frontS = Quat(frontS, baseS);
		}
	}

	// In the last iteration, the 1 extra will me merged long longo FrontS
	// Now make sure it reduces to -1 like IJK does
	return (frontS == -1 * ONE);
}

bool CanMakeI()
{
	// This variable is under testing
	// Set a limit of substrings to test
	// Idea: if you have looked at a lot of substrings, probably none of them will create the right value
	//  but the program might now have exited because none change the front value to 'i', or any untested prefix value
	long long limit = 500;


	long long current = ONE;

	long long start;

	bool withOne = false;
	bool withI = false;
	bool withJ = false;
	bool withK = false;

	// May need to look through every substring
	for (long long i = 0; i < reps; i++)
	{
		// Keep track of what the 'prefix' is
		// Since each substring is the same, if substrings are added on to each and every possible prefix,
		//  one, or none must be able to change it to a factor of i
		// check this one through each substring
		start = current;
		if (start < 0)
			start *= -1;

		// May need to search through every chracter in the substring
		for (long long j = 0; j < numChars; j++)
		{
			char c = s[j];
			long long quat = GetQuatFromChar(c);
			current = Quat(current, quat);

			if (current == I || current == -1 * I)
			{
				long long leftInSubstring = numChars - j - 1;

				if ((leftInSubstring >= 2) ||
					((reps - i - 1) * numChars > 1)
					)
				{
					return true;
				}
				else
				{
					return false;
				}
			}
		}

		// Now check to see what combinations have been tried
		if (start == ONE)
		{
			withOne = true;
		}
		else if (start == I)
		{
			withI = true;
		}
		else if (start == J)
		{
			withI = true;
		}
		else if (start == K)
		{
			withI = true;
		}

		// If all prefixes have been tried, impossible
		if (withOne && withI && withJ && withK)
		{
			return false;
		}


		if (i > limit)
		{
			return false;
		}
	}

	return false;
}

bool CanMakeK()
{
	// This variable is under testing
	// Set a limit of substrings to test
	// Idea: if you have looked at a lot of substrings, probably none of them will create the right value
	//  but the program might now have exited because none change the front value to 'i', or any untested prefix value
	long long limit = 500;


	long long current = ONE;

	long long start;

	bool withOne = false;
	bool withI = false;
	bool withJ = false;
	bool withK = false;

	// May need to look through every substring
	for (long long i = 0; i < reps; i++)
	{
		// Keep track of what the 'prefix' is
		// Since each substring is the same, if substrings are added on to each and every possible prefix,
		//  one, or none must be able to change it to a factor of i
		// check this one through each substring
		start = current;
		if (start < 0)
			start *= -1;

		// May need to search through every chracter in the substring
		for (long long j = numChars - 1; j >= 0; j--)
		{
			char c = s[j];
			long long quat = GetQuatFromChar(c);
			current = Quat(quat, current);

			if (current == K || current == -1 * K)
			{
				long long leftInSubstring = j;

				if ((leftInSubstring >= 2) ||
					((reps - i - 1) * numChars > 1)
					)
				{
					return true;
				}
				else
				{
					return false;
				}
			}
		}

		// Now check to see what combinations have been tried
		if (start == ONE)
		{
			withOne = true;
		}
		else if (start == I)
		{
			withI = true;
		}
		else if (start == J)
		{
			withI = true;
		}
		else if (start == K)
		{
			withI = true;
		}

		// If all prefixes have been tried, impossible
		if (withOne && withI && withJ && withK)
		{
			return false;
		}


		if (i > limit)
		{
			return false;
		}
	}

	return false;
}

long long GetQuatFromChar(char c)
{
	if (c == 'i')
		return I;
	else if (c == 'j')
		return J;
	else if (c == 'k')
		return K;

	cout << "Got bad char" << endl;
	system("PAUSE");
}