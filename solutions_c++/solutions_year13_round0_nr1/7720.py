#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int sum = 0, che = 0;

void check(char c1, char c2, char c3, char c4)
{// 1 X, 2 O, 0 full, 1000 has.
	if (c1=='X')
		if (c2=='X' || c2=='T')
			if (c3=='X' || c3=='T')
				if (c4=='X' || c4=='T')
					che = 1;
	if (c1=='O')
		if (c2=='O' || c2=='T')
			if (c3=='O' || c3=='T')
				if (c4=='O' || c4=='T')
					che = 2;
	if (c1=='T')
		if (c2=='X')
		{
			if (c3=='X' || c3=='T')
				if (c4=='X' || c4=='T')
					che = 1;
		}
		else
		{
			if (c3=='O' || c3=='T')
				if (c4=='O' || c4=='T')
					che = 2;
		}

	if (c1=='.' || c2=='.' || c3=='.' || c4=='.')
		sum += 50;
	else
		sum += 0;
}

void main()
{
	fstream fs, fs_out;
	fs.open("input.txt", ios::in);
	fs_out.open("output.txt", ios::out);
	int n;
	string s1, s2, s3, s4;
	char c;
	fs>>n;
	for (int loop=0; loop<n; loop++)
	{
		sum = 0, che = 0;
		fs>>s1;
		fs>>s2;
		fs>>s3;
		fs>>s4;
		
		check(s1[0], s1[1], s1[2], s1[3]);
		check(s2[0], s2[1], s2[2], s2[3]);
		check(s3[0], s3[1], s3[2], s3[3]);
		check(s4[0], s4[1], s4[2], s4[3]);

		check(s1[0], s2[0], s3[0], s4[0]);
		check(s1[1], s2[1], s3[1], s4[1]);
		check(s1[2], s2[2], s3[2], s4[2]);
		check(s1[3], s2[3], s3[3], s4[3]);

		check(s1[0], s2[1], s3[2], s4[3]);
		check(s1[3], s2[2], s3[1], s4[0]);


		if (che == 1)
		{
			fs_out<<"Case #"<<loop+1<<": X won"<<endl;
			continue;
		}
		else if (che == 2)
		{
			fs_out<<"Case #"<<loop+1<<": O won"<<endl;
			continue;
		}
		else if(sum > 30)
		{
			fs_out<<"Case #"<<loop+1<<": Game has not completed"<<endl;
			continue;
		}
		else
		{
			fs_out<<"Case #"<<loop+1<<": Draw"<<endl;
			continue;
		}
	}

	fs.close();
	fs_out.close();
}