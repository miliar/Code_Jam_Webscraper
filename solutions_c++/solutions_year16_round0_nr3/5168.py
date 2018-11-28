

#include <fstream>;
#include <string>;

using namespace std;



bool allDigitsPresent(bool digitCount[10])
{
	bool allPresent = true;
	for (int x = 0; x < 10; x++)
	{
		if (!digitCount[x])
		{
			allPresent = false;
		}
	}
	return allPresent;
}

bool causesInsomnia(long long N)
{
	bool causesInsomnia = false;
	if (N == 0)
	{
		causesInsomnia = true;
	}
	return causesInsomnia;
}

bool doStuff(long long N, ofstream* writer)
{
	if (causesInsomnia(N))
	{
		*writer << "INSOMNIA";
	}
	else
	{
		long long currNum = N;
		bool allDigitsFound = false;
		bool digitCount[10];
		for (int x = 0; x < 10; x++)
		{
			digitCount[x] = false;
		}
		while (!allDigitsPresent(digitCount))
		{
			for (char x : to_string(currNum))
			{
				digitCount[x - 48] = true;
			}
			if (allDigitsPresent(digitCount))
			{
				*writer << to_string(currNum);
				return true;
			}
			currNum = currNum + N;
		}
	}
}



int main()
{
	ifstream reader;
	ofstream writer;
	string line;
	reader.open("A-large.in");
	writer.open("outputA.txt");
	getline(reader, line);
	int T = stoi(line);
	for (int x = 1; x <= T; x++)
	{
		writer << "Case #" + to_string(x);
		writer << ": ";
		getline(reader, line);
		doStuff(stoll(line), &writer);
		writer << "\r\n";
	}
	reader.close();
	writer.close();
	return 1;
}