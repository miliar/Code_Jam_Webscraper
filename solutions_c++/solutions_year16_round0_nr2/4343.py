#include <iostream>
#include <string>
#include <fstream>

using namespace std;

bool allUp(string s,int j)
{
	for (int i = 0; i < j; i++)
	{
		if (s[i] == '-')
			return false;
	}
	return true;
}

int flip(string s)
{
	int c = 0;
	int j = s.length();
	int l=j;
	
	if (!allUp(s,j))
	{
		for (int i = j-1; i >=0 ; i--)
		{
			if (s[i] == '-')
			{
				string temp = s;
				for (int k = 0; k < l; k++)
				{
					if (temp[k] == '+')
						temp[k] = '-';
					else
						temp[k] = '+';

					s[k] = temp[k];
				}
				c++;
			}
			l--;
		}
	}
	return c;
}

int main()
{
	int cases,count = 0;
	string s;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	fin >> cases;
	fin.ignore();

	for (int i = 1; i <= cases; i++)
	{
		getline(fin, s);
	
		count = flip(s);
		fout << "Case #" << i << ": " << count<< endl;
	}
	fout.close();
	fin.close();
	return 0;
}