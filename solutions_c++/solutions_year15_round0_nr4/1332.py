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
	int results[110];
	cin >> T;
	int min;
	for (int i = 0; i < T; i++)
	{
		int X, R, C;
		cin >> X >> R >> C;
		if ((R*C) % X != 0)
		{
			results[i] = 0;
			continue;
		}
		switch (X)
		{
		case 1:
			results[i] = 1;
			break;
		case 2:
			results[i] = 1;
			break;
		case 3:
			min = (R>C) ? C : R;
			if (min > X - 2)
				results[i] = 1;
			else
				results[i] = 0;
			break;
		case 4:
			min = (R>C) ? C : R;
			if (min > X - 2)
				results[i] = 1;
			else
				results[i] = 0;
		}
	}
	for (int i = 0; i < T; i++)
	{
		if (results[i] == 0)
			cout << "Case #"<<i+1<<": RICHARD" << endl;
		else
			cout << "Case #" << i + 1 << ": GABRIEL" << endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}