#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <set>
using namespace std;

bool allplus(string s)
{
	bool ret = true;
	for(int i = 0;(i<s.size())&& ret ;i++)
	{
		if(s[i]!='+') ret = false;
	}
	return ret;
}

int firstminusright(string s)
{
	int l = s.size()-1;
	while(s[l]!='-')
	{
		l--;
	}
	return l;
}


int solve(string line)
{
	int count = 0;

	while(!allplus(line))
	{
		cout<<"line"<<line<<endl;
		int firstright = firstminusright(line);
		for(int i = 0;i<=firstright;i++)
		{
			if(line[i]=='+')
			{
				line[i]='-';
			}else
			{
				line[i]='+';
			}
		}
		count++;
	}
	return count;
}


int main() {
	ifstream infile("small.in");
	ofstream outfile("small.out");

	if(!infile.is_open() || !outfile.is_open())
	{
		cout<<"file error"<<endl;
		exit(1);
	}

	int cases = 0, i=0;
	string line = "";

	infile>>cases;

	getline(infile,line);
	while(i<cases)
	{
		getline(infile,line);
		cout<<line<<endl;
		int alma = solve(line);
		outfile << "Case #" << i+1 << ": "<< alma <<endl;
		i++;
	}
	return 0;
}
