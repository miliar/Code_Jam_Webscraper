#include<iostream>
#include<string>

#define ll long long
#pragma warning ( disable : 4996)
using namespace std;


char arr[100];
char tarr[100];
void printarr()
{
	if (false)
	{
		cout << '[';
		for (int j = 0; j < strlen(arr); j++)
		{
			cout << arr[j] << '|';
		}
		cout << ']';
	}
}
int findright()
{
	
	for (int i = strlen(arr); i >= 0; i--)
	{
		if (arr[i] == '-') return i;
	}
	return  -1;
}
pair<int,int> findleft()
{
	int flag = 0;
	if (arr[0] == '+') flag = 1;
	else flag = 2;
	int i;
	int length = strlen(arr);
	
	for (i = 0; i <length; i++)
	{
		if (arr[i] == (flag == 1? '-' : '+')) return pair<int,int>(flag,i);
	}
	return  pair<int, int>(flag, i);
}

void stringrev(int s, int e)
{
	char temp[100] = { 0, };
	for (int i = s; i <= e; i++)
	{
		temp[i] = arr[e  + s - i];
		if (temp[i] == '+') temp[i] = '-';
		else temp[i] = '+';
	}
	for (int i = s; i <= e; i++)
	{
		arr[i] = temp[i];
	}
}
int main()
{
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);
	
	ll T;

	cin >> T;
	for (int testcase = 0; testcase < T; testcase++)
	{
		cin >> arr;
		

		int counter = 0;
		while (true)
		{

			int right = findright();
			pair<int, int> tpair = findleft();
			int left = tpair.second -1;
			int flag = tpair.first;
			//cout << right << " | " << left << endl;
			if (right == -1)  break;
			if (flag == 1) // [+ /      / -] 의 경우
			{
				printarr();
				stringrev(0, left);
				printarr();
				stringrev(0, right);
				counter += 2;
				printarr();

			}
			else// [ -/       /-]의 경우
			{
				printarr();
				stringrev(0, right);
				printarr();
				counter += 1;
			}
		}
		cout << "Case #" << testcase + 1 << ": " << counter << endl;


	}



}