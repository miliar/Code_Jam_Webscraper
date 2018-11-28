#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;


int accIndex[1010] = { 0, };
void printNode()
{
	for (int i = 1; i < 10; i++)
	{
		cout << accIndex[i] << " ";
	}
	cout << endl;
}
int dfs(int turn,int top)
{
	if (accIndex[top] == 0)
		return dfs(turn, top - 1);

	int answer = turn + top;
	int tTop = 0;
	int tVal = 0;

	//cout << turn << "_Turn	" << top <<"	";
	//printNode();

	for (int i = 2; i < top; i++)
	{
		tTop = accIndex[top];
		accIndex[i] += accIndex[top];
		accIndex[top-i] += accIndex[top];
		accIndex[top] = 0;

		tVal = dfs(turn + tTop, top - 1);
		answer = min(answer,
			tVal
			);
		accIndex[top] = tTop;
		accIndex[i] -= accIndex[top];
		accIndex[top - i] -= accIndex[top];

	}

	return answer;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output21.txt", "w", stdout);

	int nTestCase = 0;
	cin >> nTestCase;

	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++)
	{
		int n, tc = 0;
		int answer = 0;
		int top = 0;
		memset(accIndex, 0, sizeof(accIndex));
		cin >> n;

		for (int i = 0; i < n; i++){
			cin >> tc;
			accIndex[tc]++;
		}
		

		cout << "Case #" << iTestCase + 1 << ": " << dfs(0, 1000) << endl;
	}

	return 0;
}