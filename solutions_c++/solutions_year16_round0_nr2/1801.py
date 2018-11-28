#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>


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
	forn (test,tests)
	{
		string text;
		input>>text;
		char first = text[0];
		char prev = text[0];
		int ans = 0;
		forn (i, text.length())
		{
			if (text[i] != prev)
			{
				ans +=1;
				prev = text[i];
			}
			
		}
		if (ans%2 ==0 & first == '-') ans+=1;
		if (ans%2 ==1 & first == '+') ans+=1;
		output << "Case #"<< test+1 <<": " << ans << "\n";
		printf("%d\n", ans);	
	}
} 
