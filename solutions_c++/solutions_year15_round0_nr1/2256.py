#include<iostream>
#include<string>
#include<fstream>
#define cin fin
#define cout fout
using namespace std;
int main()
{
	int num;
	int friends = 0;
	ifstream fin("haha.in");
	ofstream fout("hehe.out");
	cin >> num;
	string x;
	int smax;
	int now;
	int haha;
	int results[110];
	for (int i = 0; i < num; i++)
	{
		cin >> smax;
		cin >> x;
		now = 0;
		friends = 0;
		for (int j = 0; j <= smax; j++)
		{
			haha = x[j] - '0';
			if (now < j)
			{
				friends += j - now;
				now = j;
			}
			now += haha;
		}
		results[i] = friends;
		friends = 0;
	}
	for (int i = 0; i < num; i++)
	{
		cout << "Case #" << i + 1 << ": " << results[i] << endl;
	}
	fin.close();
	fout.close();
	return 0;
}