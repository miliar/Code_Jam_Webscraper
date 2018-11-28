#include <iostream>
#include <stdio.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include <fstream>
using namespace std;

int main() {
	ifstream cin1;
	cin1.open("A-small-attempt2.in");
	ofstream cout1;
	cout1.open("A-small-attempt0.out");
	int t;
	cin1 >> t;
	for (int l = 1; l <= t; l++)
	{
		int q1;
		cin1 >> q1;
		vector<vector<int>>v1(4, vector<int>(4));
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin1 >> v1[i][j];
			}
		}
		int q2;
		cin1 >> q2;
		vector<vector<int>>v2(4, vector<int>(4));
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin1 >> v2[i][j];
			}
		}
		int x;
		int c = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (v1[q1-1][i] == v2[q2-1][j])
				{
					c++;
					x = v1[q1-1][i];
				}
			}
		}
		if (c == 0)
			cout1 <<"Case #"<<l <<": Volunteer cheated!" << endl;
		else
		if (c == 1)
			cout1 << "Case #" << l <<": "<<x << endl;
		else
			cout1 << "Case #" << l << ": Bad magician!"<< endl;
	}
	return 0;
}












		/*string a,s;
		cin >> a>>s;
		int n = a.length();
		int m = s.length();
		char min = 0;
		char max = 0;
		for (int i = 1; i < n; i++)
		{
		if (a[min]>a[i])
		min = i;
		}
		for (int i = 1; i < m; i++)
		{
		if (s[max]<s[i])
		max = i;
		}
		if (s[max]>a[min])
		{
		a[min] = s[max];
		cout << a << endl;
		}
		else
		cout << a << endl;*/
	