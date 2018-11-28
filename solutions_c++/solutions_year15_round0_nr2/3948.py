#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

vector<int> _PancakesNumber;
int _DinersNumber;
int _Max, _MaxIndex, _Diffrence, _MinutesTillNow, _LastMax, _BestMinutes;
int GetMinimum()
{
	_Max = _Diffrence = _LastMax = 0;
	for(int i=0; i<_PancakesNumber.size(); i++)
	{
		_Diffrence += _PancakesNumber[i];

		if(_PancakesNumber[i] > _Max)
		{
			_Max = _PancakesNumber[i];
			_MaxIndex = i;
		}
	}

	for(int i=0; i<_PancakesNumber.size(); i++)
	{
		if(_PancakesNumber[i] > _LastMax && i != _MaxIndex)
		{
			_LastMax = _PancakesNumber[i];
		}
	}

	if(_Max < 2)
		return 0;
	else
	{
		if(_BestMinutes > _Max + _MinutesTillNow)
			_BestMinutes = _Max + _MinutesTillNow;

		_MinutesTillNow++;
		if(_PancakesNumber[_MaxIndex] % 2 == 1)
		{
			if(_PancakesNumber[_MaxIndex] == 9)
			{
				if(_LastMax <= 3 || _LastMax == 6)
				{
					_PancakesNumber[_MaxIndex] = 6;
					_PancakesNumber.push_back(3);
				}
				else
				{
					_PancakesNumber[_MaxIndex] = (_PancakesNumber[_MaxIndex] / 2) + 1;
					_PancakesNumber.push_back(_PancakesNumber[_MaxIndex] - 1);
				}
			}
			else
			{
				_PancakesNumber[_MaxIndex] = (_PancakesNumber[_MaxIndex] / 2) + 1;
				_PancakesNumber.push_back(_PancakesNumber[_MaxIndex] - 1);
			}
		}
		else
		{
			_PancakesNumber[_MaxIndex] = _PancakesNumber[_MaxIndex] / 2;
			_PancakesNumber.push_back(_PancakesNumber[_MaxIndex]);
		}
		
		return GetMinimum();
	}

}
int GetMinutes()
{
	_MinutesTillNow = 0;
	int res = GetMinimum();

	_PancakesNumber.clear();

	return _BestMinutes;
}

//int main()
//{
//	std::ifstream infile("Pancakes.in");
//	ofstream myfile("Pancakes.out");
//	
//	long long D, P, t_c;
//	infile >> t_c;
//	int temp;
//	for(int i=1; i <= t_c; i++)
//	{
//		_BestMinutes = 0;
//		infile >> D;
//		_DinersNumber = D;
//		for(int j=0; j<D; j++)
//		{
//			 infile >> temp;
//			 if(temp > _BestMinutes)
//				 _BestMinutes = temp;
//
//			 _PancakesNumber.push_back(temp);
//		}
//		myfile << "Case #"<< i << ": " << GetMinutes() << endl;
//	}
//	return 0;
//	infile.close();
//	myfile.close();
//	return 0;
//}

int main()
{
	long long D, P, t_c;
	cin >> t_c;
	int temp;
	for(int i=1; i <= t_c; i++)
	{
		_BestMinutes = 0;
		cin >> D;
		_DinersNumber = D;
		for(int j=0; j<D; j++)
		{
			 cin >> temp;
			 if(temp > _BestMinutes)
				 _BestMinutes = temp;

			 _PancakesNumber.push_back(temp);
		}
		cout << "Case #"<< i << ": " << GetMinutes() << endl;
	}
	return 0;
}