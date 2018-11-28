#include <string>
#include <fstream>
#include <vector>
#include <algorithm>


std::string GetStr(int i)
{
	std::string subWord;
	switch (i)
	{
	case 0:
		subWord = "ZERO";
		break;
	case 1:
		subWord = "ONE";
		break;
	case 2:
		subWord = "TWO";
		break;
	case 3:
		subWord = "THREE";
		break;
	case 4:
		subWord = "FOUR";
		break;
	case 5:
		subWord = "FIVE";
		break;
	case 6:
		subWord = "SIX";
		break;
	case 7:
		subWord = "SEVEN";
		break;
	case 8:
		subWord = "EIGHT";
		break;
	case 9:
		subWord = "NINE";
		break;
	}
	return subWord;
}


bool RemoveStr(std::string& s, const std::string& r)
{
	std::string tempS = s;

	for each(char c in r)
	{
		if (tempS.find(c) == tempS.npos)
			return false;
		tempS.erase(tempS.find(c), 1);
	}

	s = tempS;
	return true;
}


std::string DFS(std::string S)
{
	std::string output;
	for (unsigned int i = 0; i <= 9; i++)
	{
		if (S.size() == 0)
			return output;

		std::string subWord = GetStr(i);
		if (RemoveStr(S, subWord))
		{
			output += (char)(i + 48);
			if (S.size() == 0)
				return output;
			std::string x = DFS(S);
			if (x.size() != 0)
			{
				output += x;
				return output;
			}
			else
			{
				S += subWord;
				output.pop_back();
				continue; //Try next digit
			}
		}
		else
		{
			continue; //Try next digit
		}
	}

	if(S.size() == 0)
		return output;
	else return std::string();
}


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	unsigned int numCases = 0;
	in >> numCases;
	in.ignore();
	for (unsigned int _case = 1; _case <= numCases; _case++)
	{
		out << "Case #" << _case << ": ";

		std::string s;
		std::getline(in, s);

		out << DFS(s);
		out << std::endl;
	}

	return 0;
}


