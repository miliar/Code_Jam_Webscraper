#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream file1("A-large.in");
	ofstream file2("file2.txt");
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		string str;
		file1>>str;
		int l=str.length();
		list<char> li;
		li.push_back(str[0]);
		for(int i=1;i<l;i++)
		{
			list<char>::iterator first=li.begin();
			if(str[i]>=*first) li.push_front(str[i]);
			else li.push_back(str[i]);
		}
		file2<<"Case #"<<j+1<<": ";
		for(list<char>::iterator i=li.begin();i!=li.end();i++) file2<<*i;
		file2<<endl;
	}
}
