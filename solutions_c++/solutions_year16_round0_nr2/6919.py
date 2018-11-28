#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

int tc;
string st;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input_b.txt");
	fout.open("output_b.txt");
	
	fin >> tc;
	for(int t = 1; t <= tc; t++)
	{
		fin >> st;
		
		int cnt = 1;
		char bf = st[0];
		for(int i = 1; i < st.size(); i++)
		{
			if(st[i] != bf)
			{
				cnt++;
				bf = st[i];
			}
		}
		if(st[st.size() - 1] == '+')
		{
			fout << "Case #" << t << ": " << cnt - 1 << endl;
		}
		else
		{
			fout << "Case #" << t << ": " << cnt << endl;
		}
	}
}
