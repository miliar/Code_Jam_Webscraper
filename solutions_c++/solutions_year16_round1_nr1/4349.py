#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string insertAtFirst(string a, char x)
{
	a = a + 'g';
	//cout << a << endl;
	int n = a.length();
	for (int i = n; i >= 1; i--)
	{
		a[i] = a[i - 1];
	}
	a[0] = x;
	return a;
}
string insertAtMiddle(string a, char x)
{
	a = a + 'g';
	int n = a.length();
	for (int i = n-1; i >= 1; i--)
	{
		a[i] = a[i - 1];
	}
	a[1] = x;
	return a;
}
string insertAtLast(string a, char x)
{
	a = a + x;
	return a;
}

void main()
{
	string s;
	string x;
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");
	getline(infile, s);
	int n = stoi(s, 0);
	//cout << n << endl;

	//cout << insertAtFirst("", 'z')<<endl;
	//cout << insertAtFirst("", 'z') << endl;
	//cout << insertAtMiddle("abc", 'a');
	//system("pause");
	if (infile.is_open())
	{

		for (int i = 0; i < n; i++) //case loop
		{
			getline(infile, s);
			int l = s.length();
			string x = "";
			x = x + s[0];
			for (int j = 1; j <= l; j++)
			{
				if (s[j] > x[0])
				{
					x = insertAtFirst(x, s[j]);
				}
				else if (s[j] < x[0])
				{
					x = insertAtLast(x, s[j]);
				}
				else
				{
					x = insertAtMiddle(x, s[j]);
				}
			}
			int lx = x.length();
			string xx;
			outfile << "Case #" << i + 1 << ": ";
			for (int j = 0; j <= lx - 2; j++)
			{
				outfile << x[j];
			}
			outfile << endl;

		}

		infile.close();
	}
}