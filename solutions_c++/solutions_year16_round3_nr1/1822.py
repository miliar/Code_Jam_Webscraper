#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
	int casses;
	cin >> casses;
	for(int caseNum = 1; caseNum <= casses; caseNum++)
	{
		int senators;
		cin >> senators;
		int sum = 0;
		vector<int> data;
		vector<int> val;
		for(int i = 0; i < senators; i++)
		{
			int temp;
			cin >> temp;
			data.push_back(temp);
			val.push_back(i);
		}
		cout << "Case #" << caseNum << ": ";
		vector<char> answer;
		while(data.size() > 0)
		{
			int max = 0;
			int loc;
			for(int i = 0; i < data.size(); i++)
			{
				if(data.at(i) > max)
				{
					max = data.at(i);
					loc = i;
				}
			}
			answer.push_back((char)(val[loc] + 'A'));
			if(data.at(loc) <= 1)
			{
				data.erase(data.begin() + loc);
				val.erase(val.begin() + loc);
			}else
			{
				data.at(loc)--;
			}
		}
		int i = 0;
		if(answer.size() % 2 == 1)
		{
			cout << answer.at(i) << " ";
			i++;
		}
		for(; i < answer.size() - 2; i+=2)
		{
			cout << answer.at(i) << answer.at(i + 1) << " ";
		}
		cout << answer.at(answer.size() - 2);
		cout << answer.at(answer.size() - 1);
		cout << endl;
	}
	return 0;
}
