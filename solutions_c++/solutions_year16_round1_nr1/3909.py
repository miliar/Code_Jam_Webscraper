#include<bits/stdc++.h>
using namespace std;

int main()
{
	ifstream in;
	ofstream op;
	op.open("outputa.txt");
	in.open("A-large (1).in");
	deque<char> d;
	int t;
	in>>t;
	for(int j=1;j<=t;j++)
	{
		d.clear();
		string str;
		in>>str;
		int l =str.length();
		int prev;
		d.push_back(str[0]);
		prev=str[0]-'A';
		for(int i=1;i<l;i++)
		{
			if((str[i]-'A')<prev)
			{
				d.push_back(str[i]);
			}
			else
			{
				d.push_front(str[i]);
				prev=str[i]-'A';
			}
			
		}
		op<<"Case #"<<j<<": ";
		for(int i=0;i<d.size();i++)
		{
			op<<d[i];
		}
		op<<"\n";
	}
}
