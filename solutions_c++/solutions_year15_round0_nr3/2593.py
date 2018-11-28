#include<iostream>
#include<string>
#include <fstream>

using namespace std;

string matrix[9][9] = {
						{"0","1","i","j","k","-1","-i","-j","-k"},
						{"1","1","i","j","k","-1","-i","-j","-k"},
						{"i","i","-1","k","-j","-i","1","-k","j"},
						{"j","j","-k","-1","i","-j","k","1","-i"},
						{"k","k","j","-i","-1","-k","-j","i","1"},
						{"-1","-1","-i","-j","-k","1","i","j","k"},
						{"-i","-i","1","-k","j","i","-1","k","-j"},
						{"-j","-j","k","1","-i","j","-k","-1","i"},
						{"-k","-k","-j","i","1","k","j","-i","-1"}
						};

string getValue(string row, string col)
{
	for(int i=0; i<9; i++)
	{
		if(matrix[i][0] == row)
		{
			for(int j=0; j<9; j++)
			{
				if(matrix[0][j] == col)
					return matrix[i][j];
			}
		}
	}
	return "";
}
bool getCertainChar(string &_case, char ch)
{
	bool result = false;
	int lengthBefore, lengthAfter;
	string row, col;
	
	for(int i=0; i<_case.length(); i++)
	{
		row = col = "";
		if(ch == _case[i])
		{
			_case.erase(0,1);
			result = true;
			break;
		}
		else
		{
			if(_case[i] == '-' && _case.length() - i >= 3)
			{
				row += _case[i];
				row += _case[i+1];
				col += _case[i+2];

				lengthBefore = _case.length();
				_case.insert(0, getValue(row, col));
				lengthAfter = _case.length();

				_case.erase(lengthAfter - lengthBefore,3);
				i--;
			}
			else if(_case[i] != '-' && _case.length() - i >= 2)
			{
				row += _case[i];
				col += _case[i+1];

				lengthBefore = _case.length();
				_case.insert(0, getValue(row, col));
				lengthAfter = _case.length();

				_case.erase(lengthAfter - lengthBefore,2);
				i--;
			}
			
		}
	}
	return result;
}
bool found(string _case)
{
	bool result = false;
	int i = 0, j = 0, k = 0, z = 0, mainCounter = 0;

	if(getCertainChar(_case, 'i'))
		i = 1;
	if(getCertainChar(_case, 'j'))
		j = 1;
	if(getCertainChar(_case, 'k'))
		k = 1;

	if(getCertainChar(_case, 'z'))
		z = 1;

	if(_case.length() == 1 && _case[0] == '1' && i && j && k || _case.length() == 0 && i && j && k)
		result = true;

	return result;
}

//int main()
//{
//	std::ifstream infile("NotDijkstra.in");
//	ofstream myfile("NotDijkstra.out");
//	
//	long long input, L, X, t_c;
//	string _case, last = "";
//	infile >> t_c;
//	for(int i=1; i <= t_c; i++)
//	{
//		last = "";
//		infile >> L >> X >> _case;
//		for(int j=0; j<X; j++)
//		{
//			last.append(_case);
//		}
//		if(found(last))
//			myfile << "Case #"<< i << ": " << "YES" << endl;
//		else
//			myfile << "Case #"<< i << ": " << "NO" << endl;
//	}
//	infile.close();
//	myfile.close();
//	return 0;
//}

int main()
{
	long long input, L, X, t_c;
	string _case, last = "";
	cin >> t_c;
	for(int i=1; i <= t_c; i++)
	{
		last = "";
		cin >> L >> X >> _case;
		for(int j=0; j<X; j++)
		{
			last.append(_case);
		}
		if(found(last))
			cout << "Case #"<< i << ": " << "YES" << endl;
		else
			cout << "Case #"<< i << ": " << "NO" << endl;
	}
	return 0;
}