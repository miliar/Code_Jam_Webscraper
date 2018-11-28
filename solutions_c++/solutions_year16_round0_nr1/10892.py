#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

bool Check(int number, vector<int> &checkList)
{
	if (checkList.empty())
		return true;
	int temp, div;

	if (number < 0)
		number = number * -1;

	while (number != 0)
	{
		div = number / 10;
		temp = number - div * 10;
		number = div;
		for (int i = 0; i < checkList.size(); i++)
		{
			if (checkList[i] == temp)
			{
				checkList.erase(checkList.begin() + i);
				break;
			}
				
		}
		if (checkList.empty())
			return true;
	}
	if (checkList.empty())
		return true;
	else
		return false;
}


void main()
{
	ios::sync_with_stdio(false);
	int num = 0, temp1, temp2;
	bool flag = true;
	fstream f, f1;
	
	string temp;
	getline(cin, temp);
	freopen(temp.c_str(), "rt", stdin);
	freopen("out.txt", "wt", stdout);
	cin >> num;
	if (num < 0)
		return;

	vector <int> list;
	vector <string> result;
	for (int i = 0; i < num; i++)
	{
		cin >> temp1;
		list.push_back(temp1);
	}
	
	for (int i = 0; i < num; i++)
	{
		vector<int>	checkList = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		int count = 1;
		flag = true;
		temp1 = list[i];
		temp2 = temp1;
		while (!Check(temp1, checkList))
		{
			++count;
			temp1 = list[i]*count;
			if (temp2 == temp1)
			{
				flag = false;
				break;
			}
			else
				temp2 = temp1;
		}
		
		if (flag)
			temp = "Case #" + to_string(i+1) + ": " + to_string(temp1) + "\n";
		else
			temp = "Case #" + to_string(i + 1) + ": INSOMNIA" + "\n";
		printf(temp.c_str());
	}
	fclose(stdout);

}