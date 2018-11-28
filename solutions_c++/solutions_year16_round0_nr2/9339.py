#include<iostream>
#include<string>
#include<math.h>
#include<set>
#include<vector>
#include<fstream>

using namespace std;

string flip(string S, int tail)
{
	string s2 = "";
	for (int i = 0; i<=tail; i++)
	{
		if(S[i]=='+')
			S[i]='-';
		else
			S[i]='+';
		s2.push_back(S[i]);
	}
	return s2;
}

int main()
{
	int T = 0;
	fstream fin("B.in");
	fstream fout("B.out");
	fin>>T;
	int counter = 1;
	
	while (counter <= T)
	{
		int result = 0;
		string S;
		fin>>S;
		for(int i = S.length(); i>=0; i--)
		{
			if(S[i]=='-')
			{
				S = flip(S,i);
				result++;
			}
		}

		fout<<"Case #"<<counter<<": "<<result<<endl;
		counter++;
	}
	return 0;
}