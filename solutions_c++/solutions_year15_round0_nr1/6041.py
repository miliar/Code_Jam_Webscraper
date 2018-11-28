#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int t, l;
	char c;
	int sum;
	ofstream fout;
	fout.open("d:\\ans.txt");
	cout.rdbuf(fout.rdbuf());

	ifstream fin;
	fin.open("d:\\1.in");
	cin.rdbuf(fin.rdbuf());

	cin >> t;
	for (int test = 0; test < t; test++)
	{
		cin >> l;
		cin >> c;
		sum = c - '0';
		int ans = 0;
		for (int i = 1; i <= l; i++)
		{
			cin >> c;
			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}
			sum += (c - '0');
		}
		cout << "Case #" << (test+1) << ": " << ans << endl;
	}

	return 0;
}