#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
public:
	string calculate(string str)
	{
		if (str == "")
		return str;
		int sym = 0;
		if (str[0] == '-')

		{
			sym = 1-sym;
			if (str.length() == 2)
				return str;
			str = str.substr(1);
		}
		if (str.length() == 1)
			return str;
		char now = str[0];
		str = str.substr(1);
		for (int i = 0; i < str.length(); i++)
		{

			if (now == '1')
			{
				now = str[i];
			}
			else if (now == 'i')
			{
				if (str[i] == 'i')
				{
					now = '1';
					sym = 1 - sym;
				}
				else
				if (str[i] == 'j')
				{
					now = 'k';
				}
				else
				if (str[i] == 'k')
				{
					now = 'j';
					sym = 1 - sym;
				}
			}
			else if (now == 'j')
			{
				if (str[i] == 'i')
				{
					now = 'k';
					sym = 1 - sym;
				}
				else
				if (str[i] == 'j')
				{
					now = '1';
					sym = 1 - sym;
				}
				else
				if (str[i] == 'k')
				{
					now = 'i';
				}
			}
			else if (now == 'k')
			{
				if (str[i] == 'i')
				{
					now = 'j';
				}
				else
				if (str[i] == 'j')
				{
					now = 'i';
					sym = 1 - sym;
				}
				else
				if (str[i] == 'k')
				{
					now = '1';
					sym = 1 - sym;
				}
			}
		}
		string finalstr = "";
		if (sym)
			finalstr = "-" + finalstr;
		finalstr = finalstr + now;
		return finalstr;
	}
	string Solve(string str){
		string first = "";
		string last = "";
		vector<int> fir;
		vector<int> las;
		for (int i = 0; i < str.length()-2; i++)
		{
			first = first + str[i];
			first = calculate(first);
			if (first == "i")
			{
				fir.push_back(i+1);
			}
		}
		if (fir.size() == 0)
			return "NO";
		for (int i = fir[0]+1; i < str.length(); i++)
		{

			if (calculate(str.substr(i)) == "k")
			{
				las.push_back(i);
			}
		}
		for (int i = fir.size()-1; i >=0; i--)
		{
			string lasttry = "";
			int lastchar = fir[i];
			for (int j = 0; j < las.size(); j++)
				{
				if (fir[i] >= las[j])
					continue;
				lasttry = lasttry + str.substr(lastchar, las[j] - lastchar);
				lasttry=calculate(lasttry);
				lastchar = las[j];
				if (lasttry == "j")
						return "YES";

				}
		}

		return "NO";
	}
};
void main()
{
	ifstream input("C-small-attempt1.in");
	ofstream output("output.txt");
	int casenum, L;
	string X;
	string finalX = "";
	input >> casenum;
	cout << casenum;
	for (int i = 0; i < casenum; i++)
	{
		finalX = "";
		input >> L;
		input >> L;
		input >> X;
		for (int j = 0; j < L; j++)
		{
			finalX = finalX + X;
		}
		if (X.length() <= 1)
		{
			output << "Case #" << i + 1 << ": " << "NO" << endl;
			cout << i << endl;
			continue;
		}
		Solution sol;
		output << "Case #" << i + 1 << ": " << sol.Solve(finalX) << endl;
		cout << i << endl;
	}

}