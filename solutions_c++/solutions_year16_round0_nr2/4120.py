
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
//official solution

using namespace std;

ifstream fin("..//B-large.in");
ofstream fout("..//B-large.out");

int T;
char S[105];


int main()
{
	fin >> T;

	for (int i = 1; i <= T; i++)
	{
		int count_turn=1;		
		fout << "Case #" << i << ": ";
		fin >> S;
		int s_length=strlen(S);
		char last_char = S[0];
		for (int j = 1; j < s_length; j++)
		{
			if (S[j] != last_char)
			{
				count_turn++;
				last_char = S[j];
			}
		}
		if (S[s_length - 1] == '+')
			count_turn--;
		fout << count_turn << endl;

	}


	return 0;
}




