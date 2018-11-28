#include<iostream>
#include<cmath>
#include<string>
#include<string.h>
#include<list>
#include<vector>
using namespace std;
#define min(a,b) ((a<=b)?a:b)
list <char> clist;	
int main()
{
	string *s1;
	int T;
	int k;
	cin >> T;
	k = T;
	while (T)
	{
		cout << "Case #"<<k-T+1<<": ";
		int n;
		cin >> n;
		s1 = new string[n];
		for (int i = 0; i < n; i++)
		{
			cin >> s1[i];
		}
		int min = 0;
		for (int i = 1; i < n; i++)
		{
			if (s1[min].length()>s1[i].length())
				min = i;
		}
		string *s2;
		s2 = new string[n];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < s1[i].length(); j++)
			if (s1[i][j] != s1[i][j + 1])
			{
				s2[i].push_back(s1[i][j]);
			}
		}
		bool f = true;

		if (s2[0].compare(s2[1]) != 0)
		{
			f = false;

		}


		if (f)
		{
			vector<int> a, b;
			int ctr1 = 0, ctr2 = 0;
			int q1 = 0, q2 = 0;
			for (int j = 0; j < s2[0].length(); j++)
			{
				while (s1[0][ctr1 + q1] == s1[0][ctr1 + 1 + q1])
				{
					ctr1++;
				}
				while (s1[1][ctr2 + q2] == s1[1][ctr2 + 1 + q2])
				{
					ctr2++;
				}
				//cout << ctr1 << " " << ctr2 << endl;
				a.push_back(ctr1);
				b.push_back(ctr2);
				q1 += ctr1 + 1;
				q2 += ctr2 + 1;
				ctr1 = 0;
				ctr2 = 0;
			}
			int moves = 0;
			for (int i = 0; i < a.size(); i++)
			{
				moves +=
					abs(a[i] - b[i]);
			}
			cout << moves<<endl;
		}
		else
			cout << "Fegla Won"<<endl;
		T--;
	//	getch();
	}
}
