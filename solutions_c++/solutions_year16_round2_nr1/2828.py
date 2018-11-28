#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
#include <algorithm>


using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int main ()
{
	ifstream input;
	ofstream output;
	input.open("in.txt");
	output.open("out.txt");
	int test,tests;
	input >> tests;
	//printf("%d", tests);
	for (int test = 0; test < tests; test++)
	{	
		string word;
		input >>  word;
		int alp[26];
		for(int i = 0; i <26; i++)
			alp[i] = 0;
for(int i = 0; i <word.size(); i++)
		{
			printf("%c",word[i]);
			//char c = word[i];
			//printf("%d\n", c-'A');
			alp[word[i]-'A'] +=1;
		}
		//forn(i,26)
		//	printf("%d\n", alp[i]);
		int digit[10];
		forn(i,10)
			digit[i] = 0;
		digit[0] = alp['z'-'a'];
		alp['o'-'a'] -= alp['z'-'a'];
		digit[2] = alp['w'-'a'];
		alp['o'-'a'] -= alp['w'-'a'];
		alp['t'-'a'] -= digit[2];
		digit[4] = alp['u'-'a'];
		alp['o'-'a'] -= alp['u'-'a'];
		alp['f'-'a'] -= digit[4];
		digit[6] = alp['x'-'a'];
		digit[8] = alp['g'-'a'];
		alp['t'-'a'] -= digit[8];
		digit[1] = alp['o'-'a'];
		alp['n'-'a'] -=digit[1];
		digit[5] = alp['f'-'a'];
		alp['v'-'a'] -= digit[5];
		digit[7] = alp['v'-'a'];
		alp['n'-'a'] -= digit[7];
		digit[9] = alp['n'-'a']/2;
		
		digit[3] = alp['t'-'a'];
		forn(i,10)
			printf("%d\n", digit[i]);
		int index = 0;
		output << "Case #"<< test+1 << ": " ;
		for (int i=0; i <10; i++)
			for(int j=0; j<digit[i]; j++)
			{
				output << i;
				index++;
			}
		
		output << "\n";	
		
		
	}
}		
		
		
