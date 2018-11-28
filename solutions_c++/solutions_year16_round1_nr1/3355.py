#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

int main()
{
	int casses;
	cin >> casses;
	string word;
	for(int i = 1; i <= casses; i++)
	{
		cin >> word;
		string answer;
		for(int j = 0; j < word.size(); j++)
		{
			if(j == 0)
			{
				answer += word.at(j);
				continue;
			}
			if(word.at(j) >= answer.at(0))
			{
				string s;
				s += word.at(j);
				answer.insert(0, s);
		  }else
			{
				answer += word.at(j);
			}
			//cout << "Ans: " << answer << endl;
		}
		
		cout << "Case #" << i << ": " << answer << endl;
	}
	return 0;
}
