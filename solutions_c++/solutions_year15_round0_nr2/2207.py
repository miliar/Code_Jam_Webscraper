#include<iostream>
#include<fstream>
using namespace std;
#define cin fin
#define cout fout
int main()
{
	ifstream fin("haha.in");
	ofstream fout("haha.out");
	int T;
	cin >> T;
	int results[110];
	int pie[1100];
	for (int i = 0; i < T; i++)
	{
		int num;
		int k = 0;
		int max = 0;
		int totalmin = 9999999;
		cin >> num;
		for (int i = 0; i < num; i++)
		{
			cin >> pie[i];
			if (pie[i]>max)
				max = pie[i];
		}
		for (int ai = 1; ai <= max; ai++)
		{
			int time = 0;
			for (int i = 0; i < num; i++)
			{
				int temp = pie[i] / ai;
				if (pie[i] % ai == 0)
					temp--;
				time += temp;
			}
			time += ai;
			if (time < totalmin)
			{
				totalmin = time;
			}
		}
		results[i] = totalmin;
	}
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": " << results[i] << endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}