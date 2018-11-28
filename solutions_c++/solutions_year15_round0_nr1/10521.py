#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
void zhuanhuan(string str, vector<int> &shyval)
{
	for (int i = 0; i != str.size(); ++i)
	{
		switch (str[i])
		{
		case'0':
		{
			shyval.push_back(0);
			break;
		}
		case'1':
		{
			shyval.push_back(1);
			break;
		}
		case'2':
		{
			shyval.push_back(2);
			break;
		}
		case'3':
		{
			shyval.push_back(3);
			break;
		}
		case'4':
		{
			shyval.push_back(4);
			break;
		}
		case'5':
		{
			shyval.push_back(5);
			break;
		}
		case'6':
		{
			shyval.push_back(6);
			break;
		}
		case'7':
		{
			shyval.push_back(7);
			break;
		}
		case'8':
		{
			shyval.push_back(8);
			break;
		}
		case'9':
		{
			shyval.push_back(9);
			break;
		}
		}
	}
}
int main()
{
	ofstream fout("A-small-attempt0.out");
	ifstream fin("A-small-attempt3.in");
	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int Smax;
		fin >> Smax;
		vector<int> shyval;
		string str;
		fin >> str;
		zhuanhuan(str, shyval);
		int upnum;
		int adnum;
		adnum = 0;
		upnum = 0;
		for (int j = 0; j != shyval.size(); ++j)
		{
			if (upnum>=j)
			    upnum += shyval[j];
			else
			{
				if (shyval[j] == 0)continue;
				else
				{
					adnum += j - upnum;
					upnum += adnum + shyval[j];
				}
			}
		}
		fout << "Case #" << i << ": " << adnum << endl;
	}
	return 0;
}