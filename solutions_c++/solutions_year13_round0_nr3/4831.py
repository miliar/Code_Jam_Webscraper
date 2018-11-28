#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int vecCompare(vector<char>& vec1, vector<char>& vec2)
{
	if (vec1.size() < vec2.size())
	{
		return -1;
	}
	else if (vec1.size() > vec2.size())
	{
		return 1;
	}
	for (size_t i = 0; i < vec1.size(); i++)
	{
		if (vec1[i] < vec2[i])
		{
			return -1;
		}
		else if (vec1[i] > vec2[i])
		{
			return 1;
		}
	}
	return 0;
}

void incrRes(vector<char>& res, int num, unsigned pos)
{
	if (pos >= res.size())
	{
		res.push_back(num);
	}
	else
	{
		res[pos] += num;
	}
	for (size_t i = pos; i < res.size(); i++)
	{
		char curVal = res[i];
		if (curVal >= 10)
		{
			res[i] = curVal % 10;
			if (i + 1 == res.size())
			{
				res.push_back(0);
			}
			res[i+1] += (curVal - res[i]) / 10;
		}
	}
}

void vecMult(const vector<char>& num1, const vector<char>& num2, vector<char>& res)
{
	unsigned sumPos = 0;
	char ost = 0;
	for (vector<char>::const_reverse_iterator iter = num1.rbegin(); iter != num1.rend(); ++iter)
	{
		char num1 = *iter;
		unsigned sumPos2 = sumPos;
		for (vector<char>::const_reverse_iterator iter2 = num2.rbegin(); iter2 != num2.rend(); ++iter2)
		{
			char num2 = *iter2;
			incrRes(res, num1*num2, sumPos2);
			sumPos2++;
		}
		sumPos++;
	}
}

void getNextFairNum(vector<char>& num)
{
	size_t center = static_cast<int>(floor(num.size() / 2.0));
	bool needExtend = true;
	for (size_t i = 0; i <= center; i++)
	{
		if (num[i] != 9)
		{
			needExtend = false;
			break;
		}
	}
	if (needExtend)
	{
		size_t newSize = num.size() + 1;
		num.clear();
		num.resize(newSize, 0);
		num[0] = 1;
		num[num.size() - 1] = 1;
	}
	else
	{
		size_t center2 = center;
		if (!(num.size() % 2))
		{
			center--;
		}
		num[center2]++;
		for (size_t i = center2; i < num.size(); i++)
		{
			size_t leftIdx = center - i + center2;
			if (num[i] < 10)
			{
				num[leftIdx] = num[i];
				return;
			}
			char curVal = num[i];
			num[i] = curVal % 10;
			num[i+1] += (curVal - num[i]) / 10;

			num[leftIdx] = num[i];
			num[leftIdx-1] = num[i+1];
		}
	}
}

bool isFair(vector<char>& num)
{
	for (size_t i = 0; i < num.size(); i++)
	{
		size_t idx = num.size() - 1 - i;
		if (num[i] != num[idx])
		{
			return false;
		}
		if (idx <= i)
		{
			break;
		}
	}
	return true;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("data.dat");
	outputFile.open("data.res");
	if (inputFile.is_open() && outputFile.is_open())
	{
		int T;

		inputFile >> T;
		for (int t = 0; t < T; t++)
		{
			string A, B;
			inputFile >> A >> B;

			vector<char> lowerRange;
			vector<char> upperRange;
			for (string::iterator iter = A.begin(); iter != A.end(); ++iter)
			{
				lowerRange.push_back(*iter - '0');
			}
			for (string::iterator iter = B.begin(); iter != B.end(); ++iter)
			{
				upperRange.push_back(*iter - '0');
			}

			vector<char> startNum;
			int startNumSize = static_cast<int>(ceil(lowerRange.size() / 2.0));
			startNum.resize(startNumSize, 9);
			startNum[0] = 1;
			startNum[startNum.size() - 1] = 1;

			vector<char> res;
			int num = 0;
			do 
			{
				res.clear();
				vecMult(startNum, startNum, res);
				if (vecCompare(res, lowerRange) != -1 && isFair(res))
				{
					if (vecCompare(res, upperRange) == 1)
					{
						break;
					}
					num++;
				}
				getNextFairNum(startNum);
			} while (vecCompare(res, upperRange) != 1);
			
			outputFile << "Case #" << (t + 1) << ": " << num << endl;
		}
	}
	inputFile.close();
	outputFile.close();
	return 0;
}