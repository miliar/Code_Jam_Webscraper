#include <iostream>
#include <cmath>
#include <string>

using namespace std;

typedef long long ll;

int main()
{
	int casses;
	cin >> casses;
	for(int caseNum = 1; caseNum <= casses; caseNum++)
	{
		string data;
		cin >> data;
		int answer = 0;
		char prev = data.at(0);
		for(int i = 1; i < data.size(); i++)
		{
			if(data.at(i) != prev)
			{
				prev = data.at(i);
				answer++;
			}
		}
		if(prev == '-')
			answer++;
		cout << "Case #" << caseNum << ": " << answer << endl;
	}
	return 0;
}
