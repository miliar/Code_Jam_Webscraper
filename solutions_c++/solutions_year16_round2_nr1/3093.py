//============================================================================
// Name        : 1BProblem1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;

	int a[26];
	char output[1000];
	int temp;

	for(int nt=0; nt <t; nt ++)
	{
		char str[2200];
		cin>>str;

		strcpy(output,"");
		temp = 0;

		int count = 0;

		int len = strlen(str);

		for(int i=0; i<26; i++)
		{
			a[i] = 0;
		}

		for(int i=0; i<len; i++)
		{
			a[str[i] - 'A']++;
		}

		while(count < len)
		{
			if(a['Z' - 'A'] > 0)
			{
				a['Z' - 'A']--;
				a['E' - 'A']--;
				a['R' - 'A']--;
				a['O' - 'A']--;
				count+=4;
				output[temp++]= '0';

			}
			else if(a['W' - 'A'] > 0)
			{
				a['T' - 'A']--;
				a['W' - 'A']--;
				a['O' - 'A']--;
				count+=3;
				output[temp++]= '2';
			}
			else if(a['U' - 'A'] > 0)
			{
				a['F' - 'A']--;
				a['U' - 'A']--;
				a['O' - 'A']--;
				a['R' - 'A']--;
				count+=4;
				output[temp++]= '4';
			}
			else if(a['X' - 'A'] > 0)
			{
				a['S' - 'A']--;
				a['I' - 'A']--;
				a['X' - 'A']--;
				count+=3;
				output[temp++]= '6';
			}
			else if(a['G' - 'A'] > 0)
			{
				a['E' - 'A']--;
				a['I' - 'A']--;
				a['G' - 'A']--;
				a['H' - 'A']--;
				a['T' - 'A']--;
				count+=5;
				output[temp++]= '8';
			}
			else if(a['S' - 'A'] > 0 && a['V' - 'A'] > 0)
			{
				a['S' - 'A']--;
				a['E' - 'A']--;
				a['V' - 'A']--;
				a['E' - 'A']--;
				a['N' - 'A']--;
				count+=5;
				output[temp++]= '7';
			}
			else if(a['V' - 'A'] > 0)
			{
				a['F' - 'A']--;
				a['I' - 'A']--;
				a['V' - 'A']--;
				a['E' - 'A']--;
				count+=4;
				output[temp++]= '5';
			}
			else if(a['N' - 'A'] > 1 && a['I' - 'A']>0)
			{
				a['N' - 'A']--;
				a['I' - 'A']--;
				a['N' - 'A']--;
				a['E' - 'A']--;
				count+=4;
				output[temp++]= '9';
			}
			else if(a['N' - 'A'] > 0 )
			{
				a['O' - 'A']--;
				a['N' - 'A']--;
				a['E' - 'A']--;
				count+=3;
				output[temp++]= '1';
			}
			else if(a['T' - 'A'] > 0 && a['H' - 'A'] > 0 && a['R' - 'A'] > 0 && a['E' - 'A'] > 1)
			{
				a['T' - 'A']--;
				a['H' - 'A']--;
				a['R' - 'A']--;
				a['E' - 'A']--;
				a['E' - 'A']--;
				count+=5;
				output[temp++]= '3';
			}
		}

		for(int j=0; j<26; j++)
		{
			if(a[j] > 0)
				cout<<j<<endl;
		}

		output[temp]= '\0';
		int res[9];

//		cout<<output<<endl;

		for(int j=0; j<9; j++)
		{
			res[j] = 0;
		}

		for(int j=0; j<temp; j++)
		{
			res[output[j] - '0'] ++;
		}

		cout<<"Case #"<<nt+1<<": ";

		for(int j=0; j<=9; j++)
		{
//			cout<<"res[j] = "<<res[j]<<" ";

			for(int k=0; k<res[j]; k++)
			{
				cout<<j;
			}
		}

		if(nt < 99)
		{
			cout<<endl;
		}

	}



	return 0;
}
