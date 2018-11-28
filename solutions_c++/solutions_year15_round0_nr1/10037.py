#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
	ifstream fin("b.in");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	int s;
	string b;
	int a[10];
	int c = 1;
	while (t--)
	{
		int x = 0;
		fin >> s;
		fin >> b; 
		string z;
		if (b.size() < s + 1)
		{
			for (int g = 0; g < s + 1 - b.size(); g++)
				z = z + '0';
			b = b + z;
		}
		//check length of string as it might be lesser than s+1
		//implies add next consecutive 0s or decrease s-value
		for (int i = 0; i <= s; i++)
		{
			a[i]=int(b[i]-'0');
			//get values from string
		}
		//fout << b<<endl;
		int tot = 0;
		for (int i = 1; i <= s; i++)
		{
			tot = tot + a[i-1];
			if (tot < i&&a[i]!=0)
			{
				//go back to 0
				//fout << x<<endl;
				x = x + i - tot;
				//fout << x<<endl;
				tot = tot + x;
				//fout << tot << endl;
				//problem: if > 9 :won't happen
			}
			else
				continue;
		}
		fout << "Case #"<<c<<": "<<x << endl;
		c++;
	}
	return 0;
}