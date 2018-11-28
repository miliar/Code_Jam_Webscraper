#include<iostream>
#include<fstream>
#include<string>
#include<deque>
using namespace std;
#define cin fin
#define cout fout
int *result1;
int *result2;
int main()
{
	ifstream fin("haha.in");
	ofstream fout("haha.out");
	int T;
	cin >> T;
	int result1[3001];
	int result2[3001];
	int m; int n;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		deque<int> num;
		for (int j = 0; j < n; j++)
		{
			cin >> m;
			num.push_back(m);
		}
		int maxinterv = 0;
		int temp1 = 0;
		for (int j = 0; j < num.size()-1; j++)
		{
			if (num[j + 1] < num[j])
			{
				temp1 += num[j] - num[j+1];
				if ((num[j] - num[j + 1]) > maxinterv)
				{
					maxinterv = num[j] - num[j + 1];
				}
			}
		}
		result1[i] = temp1;
		int temp2 = 0;
		for (int j = 0; j < num.size() - 1; j++)
		{
			if (num[j]>maxinterv)
				temp2 += maxinterv;
			else
				temp2 += num[j];
		}
		result2[i] = temp2;
	}
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": " << result1[i] << ' ' << result2[i] << endl;
	}
	fin.close();
	fout.close();
	system("Pause");
	return 0;
}