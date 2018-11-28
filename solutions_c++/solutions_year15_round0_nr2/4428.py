#include <iostream>

using namespace std;

int dArry[1001];
int cost;

void solution(int idx, int special)
{
	if (idx == 0)
		return;

	if (idx + special < cost)
		cost = idx + special;

	if (special >= cost)
		return;

	for (int i = idx >> 1; i < idx; i++)
	{
		int j;
		dArry[idx - i] += dArry[idx];
		dArry[i] += dArry[idx];
		for (j = idx - 1; dArry[j] == 0 && j >= 1; j--)
			;
		special += dArry[idx];
		solution(j, special);
		special -= dArry[idx];
		dArry[idx - i] -= dArry[idx];
		dArry[i] -= dArry[idx];
	}
}

int main()
{
	int totalCase, caseIdx, numOfD, max, tmp;

	cin >> totalCase;

	for (caseIdx = 1; caseIdx <= totalCase; caseIdx++)
	{
		cin >> numOfD;

		for (int i = 0; i < 1000; i++)
			dArry[i] = 0;

		max = 0;
		for (int i = 0; i < numOfD; i++)
		{
			cin >> tmp;

			dArry[tmp]++;

			if (tmp > max)
				max = tmp;
		}

		cost = 1001;
		solution(max, 0);

		cout << "Case #" << caseIdx << ": " << cost << endl;
	}
	return 0;
}
