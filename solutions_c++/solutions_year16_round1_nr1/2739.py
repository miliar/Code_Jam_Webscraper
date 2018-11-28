#include<bits/stdc++.h>
using namespace std;
ifstream fin ("in.txt");

int main()
{
	freopen("out.txt", "w" ,stdout);
	int t;
	fin >> t;
	for(int g=1;g<=t;g++)
	{
		string str, str2;
		fin >> str;
		str2=str[0];
		for(int i=1;i<str.size();i++)
		{
			if(int(str[i])>=int(str2[0])) str2=str[i]+str2;
			else str2=str2+str[i];
		}
		cout << "Case #" << g << ": " << str2 << endl;
	}
	return 0;
}
