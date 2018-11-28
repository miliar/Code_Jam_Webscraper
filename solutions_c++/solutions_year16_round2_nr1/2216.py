#include <cstdio>
#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	string priyanka;
	getline(cin, priyanka);

	for(int p=1;p<=t;p++)
	{
		string S;
		getline(cin, S);

		map<char, int> characters;
		for(int i=0;i<26;i++)
		{
			characters[(char)i+65] = 0;
		}
		for(int i=0;i<S.length();i++)
		{
			characters[S[i]]++;	
		}

		map<int, int> result;

		for(int i=0;i<=9;i++)
			result[i] = 0;

			result[0] += characters['Z'];
			characters['E'] -= characters['Z'];
			characters['R'] -= characters['Z'];
			characters['O'] -= characters['Z'];
			characters['Z'] -= characters['Z'];

			result[2] += characters['W'];
			characters['T'] -= characters['W'];
			characters['O'] -= characters['W'];
			characters['W'] -= characters['W'];

			result[4] += characters['U'];
			characters['F'] -= characters['U'];
			characters['O'] -= characters['U'];
			characters['R'] -= characters['U'];
			characters['U'] -= characters['U'];

			result[6] += characters['X'];
			characters['S'] -= characters['X'];
			characters['I'] -= characters['X'];
			characters['X'] -= characters['X'];
			
			result[8] += characters['G'];
			characters['E'] -= characters['G'];
			characters['I'] -= characters['G'];
			characters['H'] -= characters['G'];
			characters['T'] -= characters['G'];
			characters['G'] -= characters['G'];

			result[1] += characters['O'];
			characters['E'] -= characters['O'];
			characters['N'] -= characters['O'];
			characters['O'] -= characters['O'];

			result[3] += characters['R'];
			characters['T'] -= characters['R'];
			characters['H'] -= characters['R'];
			characters['E'] -= 2*characters['R'];
			characters['R'] -= characters['R'];

			result[5] += characters['F'];
			characters['I'] -= characters['F'];
			characters['V'] -= characters['F'];
			characters['E'] -= characters['F'];
			characters['F'] -= characters['F'];

			result[7] += characters['V'];
			characters['S'] -= characters['V'];
			characters['E'] -= 2*characters['V'];
			characters['N'] -= characters['V'];
			characters['V'] -= characters['V'];

			result[9] += characters['I'];
			characters['N'] -= 2*characters['I'];
			characters['E'] -= characters['I'];
			characters['I'] -= characters['I'];


		cout<<"Case #"<<p<<": ";
		for(int i=0;i<=9;i++)
		{
			for(int j=0;j<result[i];j++)
				cout<<i;
		}
		cout<<endl;
	}
}