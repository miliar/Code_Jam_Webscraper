#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdint.h>

using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int cas = 0; cas < t; cas++){
		string s;
		vector<int> answer;
		cin >> s;
		int i = 0;
		while (i < s.length()){
			if (s[i] == 'Z')
			{
				answer.push_back(0);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("R"), s.begin() + s.find("R") + 1);
				s.erase(s.begin() + s.find("O"), s.begin() + s.find("O") + 1);
				i = 0;
			}
			else if (s[i] == 'W')
			{
				answer.push_back(2);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("T"), s.begin() + s.find("T") + 1);
				s.erase(s.begin() + s.find("O"), s.begin() + s.find("O") + 1);
				i = 0;
			}
			else if (s[i] == 'U')
			{
				answer.push_back(4);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("F"), s.begin() + s.find("F") + 1);
				s.erase(s.begin() + s.find("O"), s.begin() + s.find("O") + 1);
				s.erase(s.begin() + s.find("R"), s.begin() + s.find("R") + 1);
				i = 0;
			}
			else if (s[i] == 'X')
			{
				answer.push_back(6);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("I"), s.begin() + s.find("I") + 1);
				s.erase(s.begin() + s.find("S"), s.begin() + s.find("S") + 1);
				i = 0;
			}
			else if (s[i] == 'G')
			{
				answer.push_back(8);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("I"), s.begin() + s.find("I") + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("H"), s.begin() + s.find("H") + 1);
				s.erase(s.begin() + s.find("T"), s.begin() + s.find("T") + 1);
				i = 0;
			}
			else
				i++;
		}
		i = 0;
		while (i < s.length()){
			if (s[i] == 'O')
			{
				answer.push_back(1);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("N"), s.begin() + s.find("N") + 1);
				i = 0;
			}
			else if (s[i] == 'T')
			{
				answer.push_back(3);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("H"), s.begin() + s.find("H") + 1);
				s.erase(s.begin() + s.find("R"), s.begin() + s.find("R") + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				i = 0;
			}
			else if (s[i] == 'F')
			{
				answer.push_back(5);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("I"), s.begin() + s.find("I") + 1);
				s.erase(s.begin() + s.find("V"), s.begin() + s.find("V") + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				i = 0;
			}
			else if (s[i] == 'S')
			{
				answer.push_back(7);
				s.erase(s.begin() + i, s.begin() + i + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("E"), s.begin() + s.find("E") + 1);
				s.erase(s.begin() + s.find("V"), s.begin() + s.find("V") + 1);
				s.erase(s.begin() + s.find("N"), s.begin() + s.find("N") + 1);
				i = 0;
			}
			else
				i++;
		}
		int k = 0;
		if (s.length() > 0)
			k = s.length() / 4;
		for (int j = 0; j < k; j++)
			answer.push_back(9);
		sort(answer.begin(), answer.end());
		cout << "CASE #" << cas+1 << ": ";
		for (int j = 0; j < answer.size(); j++)
			cout << answer[j];
		cout << endl;
	}
	return 0;
}