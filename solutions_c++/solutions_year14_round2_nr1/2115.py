#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

typedef unsigned int u32;


string strip(string const & from)
{
	u32 const SIZE = from.length();
	char * result = new char[SIZE+1];
	u32 j = 0;
	for (u32 i = 0; i < SIZE; ++i)
	{
		if (0 == i || from[i] != from[i - 1])
		{
			result[j++] = from[i];
		}
	}
	result[j] = 0;
	return result;
}

int _round(float x)
{
	return static_cast<u32>(floor(x + 0.5f));
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("input.in");
	out.open("output.out");

	u32 T;
	in >> T;
	++T;

	for (u32 i = 1; i < T; ++i)
	{
		u32 N;
		in >> N;

		vector<string> words(N);
		string stripped;
		for (auto & word : words)
		{
			in >> word;
			if (0 == stripped.length())
			{
				stripped = strip(word);
			}
			else if (stripped != strip(word))
			{
				stripped.clear();
				break;
			}
		}

		if (0 == stripped.length())
		{
			cout << "Case #" << i << ": " << "Fegla Won" << endl;
			out << "Case #" << i << ": " << "Fegla Won" << endl;
		}
		else
		{
			u32 const SIZE = stripped.length();
			u32 result = 0;
			for (u32 j = 0; j < SIZE; ++j)
			{
				vector<u32> count(N, 0);
				u32 avg = 0;
				for (u32 k = 0; k < N; ++k)
				{
					count[k] = words[k].find_first_not_of(words[k][0]);
					if (string::npos == count[k])
					{
						count[k] = words[k].length();
					}
					else
					{
						words[k] = words[k].substr(count[k], words[k].length() - count[k]);
					}
					avg += count[k];
				}
				avg = _round(avg / N);
				for (auto n : count)
				{
					result += abs(static_cast<int>(n - avg));
				}
			}
			cout << "Case #" << i << ": " << result << endl;
			out << "Case #" << i << ": " << result << endl;
		}
	}

	out.close();
	in.close();
	getchar();
	return 0;
}