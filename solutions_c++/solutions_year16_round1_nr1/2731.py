#include <iostream>

using namespace std;

int main()
{
	int num;
	cin >> num;
	cin.ignore();
	for (int i = 1; i <= num; i++)
	{
		string line;
		getline(cin, line);

		cout << "Case #" << i << ": ";
		string answer;
		answer += line[0];
		for (unsigned int j = 1; j < line.length(); j++)
		{
			if (line[j] >= answer[0])
			{
				answer.insert(answer.begin(), line[j]);
			}
			else
			{
				answer += line[j];
			}
		}

		cout << answer << endl;
	}

	return 0;
}