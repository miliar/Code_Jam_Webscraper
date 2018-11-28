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
	string *x;
	int T;
	int k;
	cin >> T;
	k = T;
	while (T)
	{
		cout << "Case #"<<k-T+1<<": ";
		int n;
		cin >> n;
		x = new string[n];
		for (int i = 0; i < n; i++)
		{
			cin >> x[i];
		}
		int min = 0;
		for (int i = 1; i < n; i++)
		{
			if (x[min].length()>x[i].length())
				min = i;
		}
		string *s2;
		s2 = new string[n];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < x[i].length(); j++)
			if (x[i][j] != x[i][j + 1])
			{
				s2[i].push_back(x[i][j]);
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
			int y = 0, z = 0;
			int q1 = 0, q2 = 0;
			for (int j = 0; j < s2[0].length(); j++)
			{
				while (x[0][y + q1] == x[0][y + 1 + q1])
				{
					y++;
				}
				while (x[1][z + q2] == x[1][z + 1 + q2])
				{
					z++;
				}
				//cout << y << " " << z << endl;
				a.push_back(y);
				b.push_back(z);
				q1 += y + 1;
				q2 += z + 1;
				y = 0;
				z = 0;
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
			cout << "Fegla Won\n";
		T--;
	//	getch();
	}
}