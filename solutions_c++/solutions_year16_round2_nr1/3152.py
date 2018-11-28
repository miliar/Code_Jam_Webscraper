// CJIO_r21.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<vector>
#include<algorithm>
#include<stdio.h>
#include <string>
#include <iostream>
FILE* fpi, *fpo;

using namespace std;

//int main (void)
int _tmain(int argc, _TCHAR* argv[])
{
	//fopen_s(&fpi, "input.txt", "r");
	fopen_s(&fpo, "output.txt", "w");
	int t;

	
	vector<int> val;
	cin >> t;
	//fscanf_s(fpi, "%d", &t);
	for(int j = 1; j <= t; j++)
	{
		fprintf_s(fpo, "Case #%d: ",j);
		char s[2005];
		cin >> s;
		//int out = fscanf_s(fpi, "%s", s);
		int map[30];
		for(int i =0 ;i < 27; i++)
		{
			map[i] = 0;
		}
		val.clear();
		int l = strlen(s);
		for(int i =0 ; i < l; i++)
		{
			map[s[i]-'A']+=1;
		}

		//Z:0
		int v = map['Z'-'A'];
		map['Z'-'A']  = 0;
		map['E'-'A'] -= v;
		map['R'-'A'] -= v;
		map['O'-'A'] -= v;
		while(v--)
		{
			val.push_back(0);
		}

		//W:2
		v = map['W'-'A'];
		map['T'-'A'] -= v;
		map['W'-'A']  = 0;
		map['O'-'A'] -= v;
		while(v--)
		{
			val.push_back(2);
		}

		//U:4
		v = map['U'-'A'];
		map['F'-'A'] -= v;
		map['O'-'A'] -= v;
		map['U'-'A']  = 0;
		map['R'-'A'] -= v;
		while(v--)
		{
			val.push_back(4);
		}

		//G:8
		v = map['G'-'A'];
		map['E'-'A'] -= v;
		map['I'-'A'] -= v;
		map['G'-'A']  = 0;
		map['H'-'A'] -= v;
		map['T'-'A'] -= v;
		while(v--)
		{
			val.push_back(8);
		}

		//H:3
		v = map['H'-'A'];
		map['T'-'A'] -= v;
		map['H'-'A'] -= v;
		map['R'-'A'] -= v;
		map['E'-'A'] -= v;
		map['E'-'A'] -= v;
		while(v--)
		{
			val.push_back(3);
		}

		//F:5
		v = map['F'-'A'];
		map['F'-'A'] -= v;
		map['I'-'A'] -= v;
		map['V'-'A'] -= v;
		map['E'-'A'] -= v;
		while(v--)
		{
			val.push_back(5);
		}

		//O:1
		v = map['O'-'A'];
		map['O'-'A'] -= v;
		map['N'-'A'] -= v;
		map['E'-'A'] -= v;
		while(v--)
		{
			val.push_back(1);
		}

		//X:6
		v = map['X'-'A'];
		map['S'-'A'] -= v;
		map['I'-'A'] -= v;
		map['X'-'A'] -= v;
		while(v--)
		{
			val.push_back(6);
		}

		//V:7
		v = map['V'-'A'];
		map['S'-'A'] -= v;
		map['E'-'A'] -= v;
		map['V'-'A'] -= v;
		map['E'-'A'] -= v;
		map['N'-'A'] -= v;
		while(v--)
		{
			val.push_back(7);
		}
		
		//I:9
		v = map['I'-'A'];
		map['N'-'A'] -= v;
		map['I'-'A'] -= v;
		map['N'-'A'] -= v;
		map['E'-'A'] -= v;
		while(v--)
		{
			val.push_back(9);
		}

		sort(val.begin(), val.end());
		for(int i = 0; i < val.size(); i++)
		{
			//cout << val.at(i);
			fprintf_s(fpo, "%d", val.at(i));
		}
		//cout << endl;
		fprintf_s(fpo, "\n");
	}
	return 0;
}

