#define _CRT_SECURE_NO_WARNINGS
 
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

vector <int> vi;
priority_queue<int> pqi;

int mapp[1001][1001] = { 0, };

void printState(int tx, int ty)
{
	for (int i = 0; i < tx; i++)
	{
		for (int j = 0; j < ty; j++)
		{
			cout << mapp[i][j];
		}
		cout << endl;
	}
	cout << endl;

}
void printState(int tx)
{
	for (int i = 0; i < tx; i++)
	{
			//cout << mapp[i][j];
	}
	cout << endl;

}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output11.txt", "w", stdout);

	int nTestCase = 0;
	cin >> nTestCase;
	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++)
	{
			
		int n;
		int s[1010] = { 0, };
		int accs[1010] = { 0, };
		int tc,answer = 0;
		string tstr;
		cin >> n >> tstr;

		s[0] = tstr[0] - '0';
		accs[0] = s[0];

		for (int i = 1; i <= n; i++){
			s[i] = tstr[i] - '0';
			if (i>accs[i - 1]){
				answer += (i - accs[i - 1]);
				accs[i] = accs[i - 1] + s[i] + (i - accs[i - 1]);
			}
			else 
				accs[i] = accs[i-1] + s[i];
 		}

		cout << "Case #" << iTestCase + 1 << ": " << answer << endl;
	}

	return 0;
}