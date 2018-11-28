#include<iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream in ("B-large.in");
	ofstream out ("output.txt");
	int n;
	in>>n;
	string line;
	for (int i = 1; i <= n; i++)
	{
		in>>line;
		vector<char> s;
		for(int j = 0; j<line.length(); j++) s.push_back(line[j]);
		int count = 0;
		bool flag = true;
		while(flag)
		{
			for (int j = 0; j < s.size()-1; j++)
			{
				if (s[j] != s[j+1])
				{
					for (int k = 0; k <= j; k++)
					{
						if (s[k] == '+') s[k] = '-'; else s[k] = '+';
					}
					count++;
					break;
				}
				if (j == s.size()-2) flag = false;
			}
			cout<<count<<endl;
			if (s.size() == 1) flag = false;
		}
		if (s[0] == '-') count ++;
		out<<"Case #"<<i<<": "<<count<<'\n';
	}
	return 0;
}
//out<<"Case #"<<i<<": "<<number<<'\n';
