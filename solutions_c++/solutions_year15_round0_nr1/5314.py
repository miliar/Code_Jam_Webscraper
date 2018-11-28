#include <iostream>

using namespace std;

char sArry[1001];

int main()
{
	int totalCase, caseIdx, answer, numOfS, sum;

	cin >> totalCase;

	for (caseIdx = 1; caseIdx <= totalCase; caseIdx++)
	{
		cin >> numOfS;

		for (int i = 0; i <= numOfS; i++)
		{
			cin >> sArry[i];
		}

		answer = 0;
		sum = sArry[0] - 0x30;
		for (int i = 1; i <= numOfS; i++)
		{
			if (sum < i)
			{
				answer += (i - sum);
				sum = i;
			}
			sum += (sArry[i] - 0x30);
		}

		cout << "Case #" << caseIdx << ": " << answer << endl;
	}
	return 0;
}
