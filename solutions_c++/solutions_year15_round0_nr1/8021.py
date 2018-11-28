#include <stdio.h>

//#define ENABLE_ALGORITHM_TEST
#define INPUT_FILE  "A-large.in"
#define OUTPUT_FILE "A-large.out"

// Get number of testcases from input
// input: Input data
// cnt  : Global index counter
int testCases(char* input, int* cnt)
{
	// Initialize output to 0
	int testcases = 0;

	// Parse input data
	for (; input[*cnt] != '\n'; (*cnt)++)
	{
		testcases *= 10;
		testcases += input[*cnt] - '0';
	}

	// Go one step forward, to next data value
	(*cnt)++;

	// Return number of testcases
	return testcases;
}

// Get max shyness level for testcase from input
// input: Input data
// cnt  : Global index counter
int maxShyness(char* input, int* cnt)
{
	// Initialize output to 0
	int maxshyness = 0;

	// Parse input data
	for (; input[*cnt] != ' '; (*cnt)++)
	{
		maxshyness *= 10;
		maxshyness += input[*cnt] - '0';
	}

	// Go one step forward, to next data value
	(*cnt)++;

	// Return value of maxshyness
	return maxshyness;
}

// Solve one case
// maxShy: Max shyness level
// data  : Number of people/shynes level, starting from 0
// cnt   : Global index counter
int solveCase(int maxShy, char* data, int* cnt)
{
	// Initialize to 0
	int friensdtoinvite = 0;
	int standingpeople = 0;

	// Start algorithm
	for (int i = 0; i <= maxShy; i++)
	{
		// Check if to few people are standing
		if (standingpeople < i)
		{
			// Then invite a friend!
			// note: The friend must have a shyness level (s < i)
			friensdtoinvite++;
			standingpeople++;
		}

		// Add people for this shyness level
		standingpeople += data[*cnt] - '0';
		(*cnt)++;
	}

	// Go one step forward, to next data value
	(*cnt)++;

	// Return minimal numbers of friends you have to invite
	return friensdtoinvite;
}

// Read one line from input file
int readOneLine(FILE* lpFile, char* buffer)
{
	int cnt = 0;
	int read = fread_s(buffer, 1024, 1, 1, lpFile);
	while (read && buffer[cnt] != '\n')
	{
		cnt++;
		read = fread_s(&(buffer[cnt]), 1024-cnt, 1, 1, lpFile);
	}

	// Return true if error
	if (cnt == 0 && read == 0)
		return true;
	// Return false if successful
	return false;
}

int main()
{
#ifdef ENABLE_ALGORITHM_TEST
	// Test data from description
	char testinput[]  = "4\n4 11111\n1 09\n5 110011\n0 1";
	char testoutput[] = "Case #1: 0\nCase #2: 1\nCase #3: 2\nCase #4: 0";
	char myoutput[]   = "                                              \0\0\0\0\0";
	int cnt = 0;
	int nTestCases = testCases(testinput, &cnt);
	int cnt2 = 0;
	for (int i = 0; i != nTestCases; i++)
	{
		int maxShynessLevel = maxShyness(testinput, &cnt);
		int minFriend = solveCase(maxShynessLevel, testinput, &cnt);
		cnt2 += sprintf_s(&(myoutput[cnt2]), 52-cnt2, "Case #%d: %d", i+1, minFriend);
		if (i+1 != nTestCases)
			cnt2 += sprintf_s(&(myoutput[cnt2]), 52 - cnt2, "\n");
	}
	bool correct = true;
	for (int i = 0; i != 44; i++)
	{
		if(testoutput[i] != myoutput[i])
			correct = false;
	}
	if(correct)
	{
		printf_s("The solution is correct!");
	}
	else
	{
		printf_s("The solution is not correct...");
	}
	getchar();
#else
	// File pointers
	FILE* lpFile;
	FILE* lpFileOut;

	// Try to open the files
	if (!fopen_s(&lpFile, INPUT_FILE, "r"))
	{
		if (!fopen_s(&lpFileOut, OUTPUT_FILE, "w"))
		{
			// TODO: Solve problem
			char buffer[1024];// File read buffer
			if (!readOneLine(lpFile, buffer))
			{
				int cnt = 0;// Global index counter
				// Get number of test cases
				int nTestCases = testCases(buffer, &cnt);

				// Loop over all test cases
				for (int i = 0; i != nTestCases; i++)
				{
					// Read one line (one test case)
					if (!readOneLine(lpFile, buffer))
					{
						cnt = 0;// Reset index counter
						// Get maximum shyness level for test case
						int maxShynessLevel = maxShyness(buffer, &cnt);
						// Get the minimal number of friends you need to invite
						int minFriend = solveCase(maxShynessLevel, buffer, &cnt);

						// Print to output file (Case #%d: %d)
						fprintf_s(lpFileOut, "Case #%d: %d", i + 1, minFriend);
						if (i + 1 != nTestCases)
							fprintf_s(lpFileOut, "\n");// Add a new line if there are still cases to be solved
					}
				}
			}

			// Done, close result file
			fclose(lpFileOut);
		}

		// Done, close input file
		fclose(lpFile);
	}
#endif

	return 0;
}